import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


version = '1.0'

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
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
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
          'zope.interface',
          'zope.lifecycleevent',
          'zope.publisher',

          # XXX: In Zope 2.13, we probably won't need this just to get the
          # browser:view directive
          'zope.app.publisher',
      ],
      entry_points="""
      """,
      )
