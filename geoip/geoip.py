import json
import logging
import re
from base import GeoIP
from gevent.pool import Pool
from gevent.server import StreamServer

def dotToInt( dottedIp ):
    st = ''
    for octet in dottedIp.split('.'):
        st += "%02x" % int(octet)
    return int(st,16)

class GeoServer(StreamServer):

    ipv4re = re.compile(r'(\d{1,3}\.){3}\d{1,3}')

    def __init__(self, listener, config, **kw):
        self.log = logging.getLogger()
        if listener is not None:
            super(GeoServer, self).__init__(listener, **kw)
        self.config = config
        self.geoip = GeoIP(path=config.GEOIP_PATH,
                cache=GeoIP.GEOIP_MEMORY_CACHE)
        self.log.info('GEOIP starting on port %s...' % config.PORT);

    def _error(self, errstr):
        self.log.error("GEOIP: %s" % errstr)
        return self._return('error', errstr)

    def _return(self, label='reply', obj={}):
        reply = json.dumps({label: obj})
        self.log.info("Returning: %s" % reply)
        return "%s\n" % reply

    def handle(self, socket, address):
        try:
            sock = socket.makefile()
            line = sock.readline()
            if ' ' not in line:
                sock.write(self._error('Invalid request\nGET addr'))
            else:
                cmd, addr = line.split(' ',2)
                if cmd.upper() != 'GET':
                    sock.write(self._error('Invalid Command\nuse GET '))
                elif addr is None:
                    sock.write(self._error('Missing address'))
                else:
                    addr = addr.strip()
                    reply = self.geoip.city(addr)
                    if reply is None:
                        sock.write(self._error('No information for site'))
                    else:
                        sock.write(self._return('success',reply))
        except Exception, e:
            sock.write(self._error("Unknown error: %s" % e))
        finally:
            sock.flush()

if __name__ == "__main__":
    try:
        import settings
    except ImportError:
        import pdb; pdb.set_trace()
        print "uh-oh"

    logging.basicConfig(stream=settings.LOG_STREAM, level=settings.LOG_LEVEL)
    pool = Pool(settings.MAX_CONNECTS)
    server = GeoServer((settings.HOST, settings.PORT),
                config=settings, spawn=pool)
    server.serve_forever()
#TODO:
# Add Logging
# Test.

