""" Move GeoIPException into it's own file to break a dependency chain """

class GeoIPException(Exception):
    pass
