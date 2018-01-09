from plone.uuid.interfaces import IUUIDGenerator
from zope.deprecation import deprecate
from zope.interface import implementer

import uuid


@implementer(IUUIDGenerator)
class UUID4Generator(object):
    """Default UUID implementation.

    Uses uuid.uuid4()
    """

    def __call__(self):
        return uuid.uuid4().hex


@deprecate(
    'UUID1Generator was renamed to UUID4Generator, as we use uuid4 instead of '
    'uuid1. Please use UUID4Generator instead.'
)
class UUID1Generator(UUID4Generator):
    """BBB. Remove with next major version.
    """
