import json
import time
from powerhose.client import Client
from random import randrange

client = Client(frontend='ipc:///tmp/geo-front')

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
except ValueError, e:
    print "FAIL\n%s\n%s" % (str(e), raw)

secs = time.time() - start
print "Time: %s\n RpS: %s\n" % (secs, n/secs)



