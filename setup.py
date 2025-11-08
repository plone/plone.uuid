from pathlib import Path
from setuptools import setup


version = "3.0.0.dev0"

long_description = (
    f"{Path('README.rst').read_text()}\n{Path('CHANGES.rst').read_text()}"
)

setup(
    name="plone.uuid",
    version=version,
    description="UUIDs for content items",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    # Get more strings from
    # https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Plone",
        "Framework :: Plone :: 6.2",
        "Framework :: Plone :: Core",
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="plone uuid",
    author="Martin Aspeli",
    author_email="optilude@gmail.com",
    url="https://github.com/plone/plone.uuid",
    license="BSD",
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.10",
    install_requires=[
        "Acquisition",
        "setuptools",
        "zope.component",
        "zope.browserpage",
        "zope.interface",
        "zope.lifecycleevent",
        "zope.publisher",
    ],
    extras_require={
        "test": [
            "zope.configuration",
            "zope.event",
        ]
    },
    entry_points="""
    """,
)
