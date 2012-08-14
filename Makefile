APPNAME = geoip
VE = virtualenv
PY = bin/python
PI = bin/pip
NO = bin/nosetests -s --with-xunit

all: build

build:
	$(VE) --no-site-packages .
	$(PI) install -r prod-reqs.txt
	$(PY) setup.py build

test:
	$(NO) $(APPNAME)

