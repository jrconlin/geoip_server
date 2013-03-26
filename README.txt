Stand Alone GeoIP reader.
====

Why?
___

We're using this on a bunch of production servers. That means that the
associated data file will be updated, but may have some random corruption
that could cause a segfault, which would kill the server.
Since we'd rather not have that happen, we're putting this into it's own
service to protect from any (albeit remote) corruption crashes.

Reliablity means being paranoid.

What's the difference between this and django_geoip?
___

As little as possible.

Data:
____

Fetch the GeoIP databases from MaxMind:
http://www.maxmind.com/app/geolite

System Requirements:
____
You'll need to install the following system libraries using your
preferred local package manager:
(e.g. for Debian, use apt-get)

libevent-dev
libgeoip-dev

Installing:
____
$make build

Running:
____
To run as a stand-alone server:
$make run_sa
You can execute on calls to
http://_host_:5039/_IP Address_
e.g.
http://127.0.0.1:5039/63.245.217.20

To run as a Powerhose Client:
$make run_ph

This will require a powerhose client. See geoip/example_client.py for
an example of how to use this. For more info about powerhose see:
http://powerhose.readthedocs.org/en/0.6/

