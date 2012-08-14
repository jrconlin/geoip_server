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

