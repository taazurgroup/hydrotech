# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in hydrotech/__init__.py
from hydrotech import __version__ as version

setup(
	name='hydrotech',
	version=version,
	description='Hydrotech erp customization',
	author='Taazur',
	author_email='santosh.baburao@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
