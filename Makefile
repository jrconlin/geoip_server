APPNAME = geoip
VE = virtualenv
PY = bin/python
PI = bin/pip
NO = bin/nosetests -s --with-xunit

all: build

fetch: data/GeoIP.dat
	mkdir -p data
	pushd data
	wget "http://geolite.maxmind.com/download/geoip/database/GeoLiteCountry/GeoIP.dat.gz"
	wget "http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz"
	gzip -d GeoIP.dat.gz
	gzip -d GeoLiteCity.dat.gz
	popd

build:
	$(VE) --no-site-packages .
	$(PI) install -r prod-reqs.txt
	$(PY) setup.py build

test:
	$(NO) $(APPNAME)

