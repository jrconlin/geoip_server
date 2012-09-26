import json
import time
from powerhose.client import Client
from powerhose.exc import TimeoutError
from random import randrange

client = Client(frontend='ipc:///tmp/geo_front', timeout=100,
        timeout_max_overflow=1, timeout_overflows=1)

n = 1000
start = time.time()
try:
    for num in xrange(n):
        ip = '%s.%s.%s.%s' % (randrange(0, 255),
                randrange(0, 255),
                randrange(0, 255),
                randrange(0, 255)
                )
        raw = client.execute('GET %s' % ip)
        reply = json.loads(raw)
        if 'success' in reply and reply['success']['addr'] != ip:
            print "FAIL!\n%s\n%s" % (ip, json.dumps(reply))
    secs = time.time() - start
    print "Time: %s\n RpS: %s\n" % (secs, n/secs)
except ValueError, e:
    print "FAIL\n%s\n%s" % (str(e), raw)
except TimeoutError, e:
    print """ A timeout occured trying to process the request.
    Please make sure that the broker and workers are running.
    """

client.close()
