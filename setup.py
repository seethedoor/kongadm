# -*- coding:utf-8 -*-
# !/usr/bin/env python
#
# Author: daisheng
# Email: shawntai.ds@gmail.com

import sys

try:
    from setuptools import setup, find_packages
except ImportError:
    print ("setuptools not found, run 'pip install setuptools' before setup kongadm")
    sys.exit(1)

with open("requirements.txt") as requirements_file:
    requirements = requirements_file.read().splitlines()
    if not requirements:
        print ("requirements.txt file not found.")
        sys.exit(2)

setup(name='kongadm',

      version='0.3',

      url='https://github.com/seethedoor/kongadm',

      license='GPL3',

      author='daisheng',

      author_email='shawntai.ds@gmail.com',

      description='python package of kong managements',

      packages=find_packages(exclude=['tests']),

      long_description=open('README.md').read(),

      zip_safe=False,

      install_requires=requirements,

      test_suite='nose.collector')