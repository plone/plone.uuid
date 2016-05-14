from zope.publisher.browser import BrowserView
from plone.uuid.interfaces import IUUID

import sys
if sys.version_info >= (3,):
    text_type = str
else:
    text_type = unicode


class UUIDView(BrowserView):
    """A simple browser view that renders the UUID of its context
    """

    def __call__(self):
        return text_type(IUUID(self.context, u""))
