from zope.interface import implementer
from zope.component import adapter

from plone.uuid.interfaces import IUUID
from plone.uuid.interfaces import IAttributeUUID

from plone.uuid.interfaces import ATTRIBUTE_NAME

@implementer(IUUID)
@adapter(IAttributeUUID)
def attributeUUID(context):
    return getattr(context, ATTRIBUTE_NAME, None)
