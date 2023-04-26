Changelog
=========

.. You should *NOT* be adding new change log entries to this file.
   You should create a file in the news directory instead.
   For helpful instructions, please see:
   https://github.com/plone/plone.releaser/blob/master/ADD-A-NEWS-ITEM.rst

.. towncrier release notes start

2.0.0 (2023-04-26)
------------------

Breaking changes:


- Drop python 2.7 support.
  [gforcada] (#1)


Internal:


- Update configuration files.
  [plone devs] (2ed8f544)


1.0.6 (2020-04-22)
------------------

Bug fixes:


- Minor packaging updates. (#1)


1.0.5 (2018-01-18)
------------------

Bug fixes:

- Fix package dependencies.
  [gforcada]

- Fix documentation and uuid generator class name to reflect the fact that we use the ``uuid4`` implementation instead of ``uuid1``.
  [thet]


1.0.4 (2016-06-02)
------------------

Bug fixes:

- Update setup.py url to point to github.
  [esteele]

- Fixed issues preventing tests passing on Python 3
  [datakurre]


1.0.3 (2012-05-31)
------------------

- Use zope.browserpage.
  [hannosch]

- Defensive UUID assignment in addAttributeUUID() handler: keep existing
  UUID value if handler called more than once, except in case of object
  copy event, where original and destination should have distinct UUID.
  [seanupton]


1.0.2 - 2011-10-18
------------------

- Generate UUID without dashes.
  [elro]


1.0.1 - 2011-05-20
------------------

- Relicense under modified BSD license.
  See http://plone.org/foundation/materials/foundation-resolutions/plone-framework-components-relicensing-policy
  [davisagli]


1.0 - 2011-05-13
----------------

- Release 1.0 Final
  [esteele]

- Add MANIFEST.in.
  [WouterVH]


1.0b2 - 2011-01-03
------------------

- Add MutableUUID component
  [toutpt]


1.0b1 - 2010-11-27
------------------

- Initial release
