APPNAME = geoip
VE = virtualenv
PY = bin/python
PI = bin/pip
NO = bin/nosetests -s --with-xunit

all: build

# Note:
# Unfortunately, this may fail with a 503 error. If that's the case, you
# will have to go to the download page directly.
# You will need both the City and Country databases.
fetch: data/GeoIP.dat data/GeoLiteCity.dat
	@echo "Fetching data"

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
	@echo "Run 'make fetch' to fetch GeoIP data."

test:
	$(NO) $(APPNAME)

