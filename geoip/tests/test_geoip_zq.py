import json
import unittest

from StringIO import StringIO
from geoip.geoip_worker import GeoServer


class AsObj:

    def __init__(self, **items):
        self.__dict__.update(items)


class FakeSocket(StringIO):

    def makefile(self):
        return self


class TestGeoServer(unittest.TestCase):

    def setUp(self):
        self.server = GeoServer(None,
                'ipc:///tmp/test/rq0',
                'ipc:///tmp/test/rp0',
                AsObj(**{'GEOIP_PATH': 'data/',
                    'PORT': 0,
                    }))

    def test_valid(self):
        for address in ['63.245.217.20', '2620:101:8008:5::2:7']:
            value = self.server.process('GET %s' % address)
            resp = json.loads(value)
            self.failUnless('success' in resp)
            self.failUnlessEqual(resp['success']['country_code'], 'US')

    def test_bad_command(self):
        value = self.server.process('banana\n')
        self.failUnless('error' in value)

    def test_bad_request(self):
        value = self.server.process('\n')
        self.failUnless('error' in value)

    def test_empty_info(self):
        value = self.server.process('get 127.0.0.1\n')
        self.failUnless('error' in value)

    def test_check_connection(self):
        value = self.server.process('monitor\n')
        self.failUnless('200 OK' in value)
