"""
    This Source Code Form is subject to the terms of the Mozilla Public
    License, v. 2.0. If a copy of the MPL was not distributed with this
    file, You can obtain one at http://mozilla.org/MPL/2.0/.


    Stand Alone GeoIP lookup service.

    This code is based off of the django.geoip lookup module:
    https://docs.djangoproject.com/en/dev/ref/contrib/gis/geoip/#module-django.contrib.gis.geoip

    Since this service will be installed to a distributed, production server
    and since updates may introduce corruption to the dataset that may
    cause the C API to segfault and kill the python app, this code creates
    a separate service that isolates such faults.

    By default, this application runs at localhost on port 5309

    send:
    GET <addr>\n

    receive:
    On success
    {'success': {<GeoIP information as JSON>}}\n

    On error:
    {'error': <Error description string>}\n

"""
import json
import logging
import re
from base import GeoIPException, GeoIP
from gevent.pool import Pool
from gevent.server import StreamServer
from statsd import statsd


def dotToInt(dottedIp):
    st = ''
    for octet in dottedIp.split('.'):
        st += "%02x" % int(octet)
    return int(st, 16)


class GeoServer(StreamServer):

    ipv4re = re.compile(r'(\d{1,3}\.){3}\d{1,3}')

    def __init__(self, listener, config, **kw):
        self.log = logging.getLogger()
        if listener is not None:
            super(GeoServer, self).__init__(listener, **kw)
        self.config = config
        try:
            self.geoip = GeoIP(path=config.GEOIP_PATH,
                cache=GeoIP.GEOIP_MEMORY_CACHE)
            self.log.info('GEOIP starting on port %s...' % config.PORT)
            self.log.info('GEOIP starting on port %s...' % config.PORT);
        except GeoIPException, e:
            self.log.error("Could not start GeoIP server: %s", str(e))

    def _error(self, errstr):
        self.log.error("GEOIP: %s" % errstr)
        return self._return('error', errstr)

    def _return(self, label='reply', obj={}):
        reply = json.dumps({label: obj})
        self.log.info("Returning: %s" % reply)
        return "%s\n" % reply

    def checkConnection(self, socket):
        try:
            if self.geoip.country_code('mozilla.org') == 'US':
                return "200 OK\n"
        except Exception, e:
            self.log.error("Failed Health Check: %s", str(e))
            return "500 Error\n"

    def handle(self, socket, address):
        if statsd is not None:
            timer = statsd.Timer('GeoIP')
            req_counter = statsd.counter('GeoIP.request')
            success_counter = statsd.counter('GeoIP.success')
            fail_counter = statsd.counter('GeoIP.failure')
            timer.start()
        else:
            timer = None
            req_counter = 0
            success_counter = 0
            fail_counter = 0
        try:
            sock = socket.makefile()
            line = sock.readline()
            req_counter += 1
            if ' ' not in line:
                return sock.write(self._error('Invalid request\nGET addr'))
            items = line.split(' ')
            cmd = items[0]
            addr = items[1].strip().replace('/', '')
            if cmd.upper() != 'GET':
                return sock.write(self._error('Invalid Command\nuse GET '))
            if addr is None:
                return sock.write(self._error('Missing address'))
            if 'monitor' in addr:
                sock.write(self.checkConnection(sock))
                return sock.flush()
            reply = self.geoip.city(addr)
            if reply is None:
                fail_counter += 1
                return sock.write(self._error('No information for site'))
            else:
                success_counter += 1
                return sock.write(self._return('success', reply))
        except Exception, e:
            return sock.write(self._error("Unknown error: %s %s" % (e, line)))
        finally:
            if timer:
                timer.stop('Request')
            sock.flush()

if __name__ == "__main__":
    try:
        import settings
        """
        Statsd is HEAVILY django dependent. The following
        work around attempts to address that.
        """
        import os
        for i in ['STATSD_HOST', 'STATSD_PORT', 'STATSD_PREFIX']:
            if hasattr(settings, i):
                print 'loading %s = %s' % (i, getattr(settings, i))
                os.environ[i] = str(getattr(settings, i))
    except ImportError, e:
        print "Cannot run. Terminating."
        print str(e)
        exit(-1)

    logging.basicConfig(stream=settings.LOG_STREAM, level=settings.LOG_LEVEL)
    pool = Pool(settings.MAX_CONNECTS)
    server = GeoServer((settings.HOST, settings.PORT),
                config=settings, spawn=pool)
    server.serve_forever()
