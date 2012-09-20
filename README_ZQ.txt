Using ZeroMQ with GeoIP server
====

As an experiment to improve resolution speed, I have implemented a
ZMQ broker/worker layer ontop of the geoip lookup code. This code
uses the zmq-broker framework https://github.com/samueltardieu/zmq-broker

It should be noted that the zmq-broker code was originally crafted to be
an example, however it fits the general model of what I needed fairly well
so little tweaking was required. Most modifications are only to mold it
to the existing settings config methods.

Setup
-----
No additional setup should be required. The ZMQ settings are noted
in the settings.py file if you wish to change port numbers or specify
a specific host.

Running
-------

tl:dr; $ ./zq_start.sh

You will need to run an instance of geoip/broker.py and one or more of
geoip/geoip_worker.py. While the geoip lookup portion isn't really CPU
intensive, it may be beneficial to add workers to catch the instances where
a lookup is occuring. Obviously, the broker is the bottleneck in that case,
and some additional optimization may be required.


