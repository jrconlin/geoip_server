APPNAME = geoip
VE = virtualenv
PY = bin/python
PI = bin/pip
NO = bin/nosetests -s --with-xunit

all: build

fetch: data/GeoIP.dat data/GeoLiteCity.dat

data/GeoIP.dat:
	mkdir -p data
	wget -P data "http://geolite.maxmind.com/download/geoip/database/GeoLiteCountry/GeoIP.dat.gz"
	gzip -d data/GeoIP.dat.gz
	cd -

data/GeoLiteCity.dat:
	mkdir -p data
	cd data
	wget -P data "http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz"
	gzip -d data/GeoLiteCity.dat
	cd -

build:
	$(VE) --no-site-packages .
	$(PI) install -r prod-reqs.txt
	$(PY) setup.py build

test:
	$(NO) $(APPNAME)

