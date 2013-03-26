"""
    This Source Code Form is subject to the terms of the Mozilla Public
    License, v. 2.0. If a copy of the MPL was not distributed with this
    file, You can obtain one at http://mozilla.org/MPL/2.0/.


    Stand alone MaxMind GeoIP binary service

    In order to isloate potential segfaults from the C API, creating this as
    a pollable service that can be quickly restarted.

    based off of django_geoip
    <https://github.com/futurecolors/django-geoip/>

"""

from __future__ import absolute_import

try:
    from base import GeoIP
    HAS_GEOIP = True
except:
    HAS_GEOIP = False
