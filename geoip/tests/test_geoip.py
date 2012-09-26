import json
import unittest

from StringIO import StringIO
from geoip.geoip_ph import GeoServer


class AsObj:

    def __init__(self, **items):
        self.__dict__.update(items)


class TestGeoServer(unittest.TestCase):

    def setUp(self):
        self.server = GeoServer()

    def test_valid(self):
        for address in ['63.245.217.20', '2620:101:8008:5::2:7']:
            value = self.server.process(AsObj(**{'data':
                'get %s\n' % address}))
            resp = json.loads(value)
            self.failUnless('success' in resp)
            self.failUnlessEqual(resp['success']['country_code'], 'US')

    def test_bad_command(self):
        value = self.server.process(AsObj(**{'data': 'banana\n'}))
        self.failUnless('error' in value)

    def test_bad_request(self):
        value = self.server.process(AsObj(**{'data': '\n'}))
        self.failUnless('error' in value)

    def test_empty_info(self):
        value = self.server.process(AsObj(**{'data': 'get 127.0.0.1\n'}))
        self.failUnless('error' in value)

    def test_monitor(self):
        value = self.server.process(AsObj(**{'data': 'monitor\n'}))
        self.failUnless('200 OK' in value)
