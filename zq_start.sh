#! /bin/sh

PYTHON= bin/python
NUMWORKERS=3

REQUEST_SOCKET='tcp://*:5309'
WORKER_SOCKET='tcp://*:5310'
ANSWER_SOCKET='tcp://*:5311'

# Start the broker:
echo "Starting the broker..."
$PYTHON zmq-broker/broker.py &

# Start the workers:
for ((a=0; a < NUMWORKERS; a++))
do
    echo "starting worker $a"
    $PYTHON geoip_worker.py &
done

