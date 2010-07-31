import uuid

from zope.interface import implements

from plone.uuid.interfaces import IUUIDGenerator

class UUID1Generator(object):
    """Default UUID implementation.
    
    Uses uuid.uuid1()
    """
    
    implements(IUUIDGenerator)
    
    def __call__(self):
        return str(uuid.uuid1())
