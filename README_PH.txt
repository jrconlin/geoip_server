Using Powerhose with GeoIP server
===

As an experiment to improve resolution speed, I have implemented a
powerhose broker/client ontop of the geoip lookup code. This code uses
the powerhose framework https://github.com/mozilla-services/powerhose

Powerhose uses ZMQ internally and is best run via circusd
http://pypi.python.org/pypi/circus
A circus config file has been included for conveinence. The configuration
also presumes using file based IPC under the /tmp directory.

Setup
---
No additional setup should be required. the circus.ini file contains the
IPC settings, with geoip/settings.py containing more app specific settings.

Running:
---
tl:dr; $ ./ph_start.sh

Circus handles running the two applications needed. It also provides
some process monitoring and automatic restarts. While no more than one
broker is required, additional workers may be useful in cases of high demand.
