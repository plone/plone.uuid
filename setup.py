import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


version = '1.0.4.dev0'

long_description = (
    read('README.txt')
    + '\n' +
#    read('plone', 'uuid', 'README.txt')
#    + '\n' +
    read('CHANGES.txt')
    + '\n'
    )

setup(name='plone.uuid',
      version=version,
      description="UUIDs for content items",
      long_description=long_description,
      # Get more strings from
      # https://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Framework :: Plone :: 5.0",
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        ],
      keywords='plone uuid',
      author='Martin Aspeli',
      author_email='optilude@gmail.com',
      url='http://plone.org',
      license='BSD',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plone'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'zope.browserpage',
          'zope.interface',
          'zope.lifecycleevent',
          'zope.publisher',
      ],
      entry_points="""
      """,
      )
