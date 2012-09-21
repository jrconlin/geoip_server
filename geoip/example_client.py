#! /usr/bin/python

# The following is a simple, thread safe call to the ZMQ broker service.
# The broker parcels out data to the various workers.
import json
from powerhose.client import Client


class TestClient():

    def __init__(self, config=None):
        self.client = Client(frontend=config.FRONTEND)

    def fetch(self, addr):
        return json.loads(self.client.execute(addr))


if __name__ == '__main__':
    import settings
    from pprint import pprint
    from random import randrange

    client = TestClient(config=settings)
    for i in xrange(0, 10000):
        # Get a random address
        addr = "GET %s.%s.%s.%s" % (randrange(0, 255), randrange(0, 255),
                randrange(0, 255), randrange(0, 255))
        pprint(client.fetch(addr))
