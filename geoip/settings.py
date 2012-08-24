import sys
import logging

LOG_LEVEL = logging.DEBUG
LOG_STREAM = sys.stderr

HOST = '0.0.0.0'
PORT = 5309
MAX_CONNECTS = 500

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
