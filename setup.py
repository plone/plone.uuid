# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup


version = '1.0.6'

long_description = (
    open('README.rst').read() + '\n' +
    open('CHANGES.rst').read() + '\n'
)

setup(
    name='plone.uuid',
    version=version,
    description="UUIDs for content items",
    long_description=long_description,
    # Get more strings from
    # https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Framework :: Plone :: 5.0",
        "Framework :: Plone :: 5.1",
        "Framework :: Plone :: 5.2",
        "Framework :: Plone :: Core",
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keywords='plone uuid',
    author='Martin Aspeli',
    author_email='optilude@gmail.com',
    url='https://github.com/plone/plone.uuid',
    license='BSD',
    packages=find_packages(),
    namespace_packages=['plone'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Acquisition',
        'setuptools',
        'zope.component',
        'zope.browserpage',
        'zope.interface',
        'zope.lifecycleevent',
        'zope.publisher',
    ],
    extras_require={
        'test': [
            'zope.configuration',
            'zope.event',
        ]
    },
    entry_points="""
    """,
)
