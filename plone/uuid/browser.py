from plone.uuid.interfaces import IUUID
from zope.publisher.browser import BrowserView

import sys


text_type = str


class UUIDView(BrowserView):
    """A simple browser view that renders the UUID of its context"""

    def __call__(self):
        return text_type(IUUID(self.context, ""))
