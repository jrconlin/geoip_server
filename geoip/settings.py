import sys
import logging

LOG_LEVEL = logging.DEBUG
LOG_STREAM = sys.stderr

HOST = '0.0.0.0'
PORT = 5309
MAX_CONNECTS = 500

# Start ZeroMQ Values
ZQ_HOST = '*'
REQ_PORT = 'tcp://%s:5309' % ZQ_HOST
# Since workers and the broker tend to be on the same box, no need
# for the TCP overhead.
#WORK_PORT = 'tcp://%s:5310' % ZQ_HOST
#ANS_PORT = 'tcp://%s:5311' % ZQ_HOST
WORK_PORT = 'ipc:///tmp/geo/w'
ANS_PORT = 'ipc:///tmp/geo/a'
ZQ_TRIES = 2
ZQ_TIMEOUT = 1
# End ZeroMQ Values

GEOIP_PATH = 'data/'
# Free data:
GEOIP_CITY = 'GeoLiteCity.dat'
GEOIP_COUNTRY = 'GeoIP.dat'
# Paid data:
#GEOIP_CITY = 'GeoIPCity.dat'
#GEOIP_COUNTRY = 'GeoIP.dat'
GEOIP_COUNTRY_V6 = 'GeoIPv6.dat'
GEOIP_CITY_V6 = 'GeoLiteCityv6.dat'


STATSD_HOST = 'localhost'
STATSD_PORT = 8125
STATSD_PREFIX = 'geoip'

GEOIP_SETTINGS = {'GEOIP_PATH': GEOIP_PATH,
                  'GEOIP_CITY': GEOIP_CITY,
                  'GEOIP_COUNTRY': GEOIP_COUNTRY,
                  'GEOIP_CITY_V6': GEOIP_CITY_V6,
                  'GEOIP_COUNTRY_V6': GEOIP_COUNTRY_V6,
                  }
