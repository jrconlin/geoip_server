#! /usr/bin/python

# The following is a simple, thread safe call to the ZMQ broker service.
# The broker parcels out data to the various workers.
import json
import zmq


class TestClient():

    def __init__(self, context=None, config=None):
        if context is not None:
            self.context = context
        else:
            self.context = zmq.Context(1)
        if config is None:
            config = dict({})
        self.sock = self.context.socket(zmq.REQ)
        self.sock.connect(settings.REQ_PORT)

    def fetch(self, addr):
        self.sock.send(addr)
        return json.loads(self.sock.recv())


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
