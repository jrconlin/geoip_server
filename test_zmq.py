import zmq
import json
import time
from random import randrange

context = zmq.Context()
socket = context.socket(zmq.REQ)
start = time.time()
socket.connect("tcp://localhost:5309")
n = 1000
try:
    for num in range(n):
        ip = '%s.%s.%s.%s' % (randrange(0, 255),
                randrange(0, 255),
                randrange(0, 255),
                randrange(0, 255)
                )
        socket.send('GET %s\n' % ip)
        raw = socket.recv()
        reply = json.loads(raw)
        if 'success' in reply and reply['success']['addr'] != ip:
            print "FAIL!\n%s\n%s" % (ip, json.dumps(reply))
except ValueError, e:
    print "FAIL\n%s\n%s" % (str(e), raw)

secs = time.time() - start
print "Time: %s\n RpS: %s\n" % (secs, n/secs)
