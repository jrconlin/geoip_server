import os

from setuptools import setup, find_packages

setup(name='geoip_server',
        version='0.1',
        description='Stand alone GeoIP server',
        author='jrconlin',
        author_email='',
        license='MPL 2.0',
        url='https://github.com/jrconlin/geoip_server',
        include_package_data=True,
        classifiers=[],
        packages=find_packages(exclude=['tests']),
        install_requires=[])



