import json
import unittest

from StringIO import StringIO
from geoip.geoip import GeoServer


class AsObj:

    def __init__(self, **items):
        self.__dict__.update(items)


class FakeSocket(StringIO):

    def makefile(self):
        return self


class TestGeoServer(unittest.TestCase):

    def setUp(self):
        self.server = GeoServer(None, AsObj(**{
            'GEOIP_PATH': 'data/',
            'PORT': 0,
            }))

    def test_valid(self):
        for address in ['63.245.217.20', '2620:101:8008:5::2:7']:
            fake = FakeSocket('get %s\n' % address)
            self.server.handle(fake, None)
            value = fake.getvalue().split('\n')[1]
            resp = json.loads(value)
            self.failUnless('success' in resp)
            self.failUnlessEqual(resp['success']['country_code'], 'US')

    def test_bad_command(self):
        fake = FakeSocket('banana\n')
        self.server.handle(fake, None)
        value = fake.getvalue().split('\n')[1]
        self.failUnless('error' in value)

    def test_bad_request(self):
        fake = FakeSocket('\n')
        self.server.handle(fake, None)
        value = fake.getvalue().split('\n')[1]
        self.failUnless('error' in value)

    def test_empty_info(self):
        fake = FakeSocket('get 127.0.0.1\n')
        self.server.handle(fake, None)
        value = fake.getvalue().split('\n')[1]
        self.failUnless('error' in value)

    def test_monitor(self):
        fake = FakeSocket('monitor\n')
        self.server.handle(fake, None)
        self.failUnless('200 OK' in fake.getvalue())
