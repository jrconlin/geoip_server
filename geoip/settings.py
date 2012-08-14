import sys
import logging

LOG_LEVEL = logging.DEBUG
LOG_STREAM = sys.stderr

HOST = '0.0.0.0'
PORT = 5309
MAX_CONNECTS = 500

#GEOIP_PATH='./local/GeoLiteCity.dat'
GEOIP_PATH = 'data/'

STATSD_HOST = 'localhost'
STATSD_PORT = 8125
STATSD_PREFIX = 'geoip'
