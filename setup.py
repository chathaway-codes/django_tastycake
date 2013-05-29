#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='django-tastycake',
    version='0.1.0',
    author=u'Charles Hathaway',
    author_email='chathaway@logrit.com',
    package_dir = {'':'src/sample_site/'},
    packages=['tastycake'],
    requires=[
        'django_tastypie',
    ],
    install_requires=[
        'django_tastypie',
    ],
    url='https://github.com/chuck211991/django_tastycake',
    license='BSD license, see LICENCE.txt',
    description='Adds some simplicity and compatibility to django-tastypie',
    zip_safe=False,
    include_package_data=True,
)
