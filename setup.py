# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

setup(
    name='django_tastycake',
    version='1.0.0',
    author=u'Charles Hathaway',
    author_email='chathaway@logrit.com',
    packages=['tastycake'],
    url='https://github.com/chuck211991/django_tastycake',
    license='BSD license, see LICENCE.txt',
    description='Adds some simplicity and compatibility to django-tastypie',
    zip_safe=False,
    include_package_data=True,
)
