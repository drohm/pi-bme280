__author__ = 'Doug Rohm'
import re
import ast
from os import path
from setuptools import setup


here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

_version_re = re.compile(r'__version__\s+=\s+(.*)')
with open('pi_bme280/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(f.read().decode('utf-8')).group(1)))

download_url = 'https://github.com/drohm/pi-bme280/releases/tag/{0}'.format(version)

classifiers = ['Development Status :: 5 - Production/Stable',
               'Environment :: Console',
               'Intended Audience :: Developers',
               'Intended Audience :: End Users/Desktop',
               'Intended Audience :: Manufacturing',
               'Intended Audience :: Science/Research',
               'Intended Audience :: System Administrators',
               'License :: OSI Approved :: MIT License',
               'Operating System :: POSIX :: Linux',
               'Programming Language :: Python :: 3.4',
               'Programming Language :: Python :: 3 :: Only',
               'Topic :: Home Automation',
               'Topic :: Scientific/Engineering :: Atmospheric Science',
               'Topic :: System :: Hardware :: Hardware Drivers',
               'Topic :: System :: Monitoring',
               'Topic :: System :: Operating System Kernels :: Linux',
               'Topic :: Software Development',
               'Topic :: Utilities']

setup(
    name='pi-bme280',
    version=version,
    url='https://github.com/drohm/pi-bme280',
    license='MIT',
    author=__author__,
    author_email='pypi@dougrohm.com',
    description='Python 3 library for the BOSCH BME280 combined humidity and pressure sensor for the Raspberry Pi.',
    long_description=long_description,
    include_package_data=True,
    download_url=download_url,
    packages=['pi_bme280', 'examples'],
    install_requires=[
        'RPi.GPIO>=0.6.3',
    ],
    classifiers=classifiers,
    keywords='bosch sensor bme280 T temperature humidity RH dew-point celsius measurement'
             ' gpio serial 2-wire 3-wire 4-wire crc crc-8 hardware driver ic'
)
