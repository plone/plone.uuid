from setuptools import setup, find_packages
import os

version = '1.0a0.simplon.1'

setup(name='plone.uuid',
      version=version,
      description="UUIDs for content items",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='plone uuid',
      author='Martin Aspeli',
      author_email='optilude@gmail.com',
      url='http://plone.org',
      license='GPL',
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
