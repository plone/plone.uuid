from plone.uuid.interfaces import IUUIDGenerator
from zope.interface import implementer

import uuid


@implementer(IUUIDGenerator)
class UUID4Generator:
    """Default UUID implementation.

    Uses uuid.uuid4()
    """

    def __call__(self):
        return uuid.uuid4().hex
