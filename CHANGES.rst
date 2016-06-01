Changelog
=========

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
