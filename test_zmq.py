import zmq
import json
from random import randrange

context = zmq.Context()
socket = context.socket(zmq.REQ)

socket.connect("tcp://127.0.0.1:5309")

for num in range(10000):
    ip = '%s.%s.%s.%s' % (randrange(0, 255),
            randrange(0, 255),
            randrange(0, 255),
            randrange(0, 255)
            )
    socket.send('GET %s\n' % ip)
    reply = json.loads(socket.recv())
    if 'success' in reply and reply['success']['addr'] != ip:
        import pdb; pdb.set_trace()
        print "FAIL!\n%s\n%s" % (ip, json.dumps(reply))
    print reply
