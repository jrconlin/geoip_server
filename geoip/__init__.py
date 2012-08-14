"""
    Stand alone MaxMind GeoIP binary service

    In order to isloate potential segfaults from the C API, creating this as
    a pollable service that can be quickly restarted.

    based off of django_geoip.

"""

from __future__ import absolute_import

try:
    from base import GeoIP
    HAS_GEOIP = True
except:
    HAS_GEOIP = False
