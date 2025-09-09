from plone.uuid import interfaces
from zope import component
from zope import interface


@interface.implementer(interfaces.IUUID)
@component.adapter(interfaces.IAttributeUUID)
def attributeUUID(context):
    return getattr(context, interfaces.ATTRIBUTE_NAME, None)


@interface.implementer(interfaces.IMutableUUID)
@component.adapter(interfaces.IAttributeUUID)
class MutableAttributeUUID:
    def __init__(self, context):
        self.context = context

    def get(self):
        return getattr(self.context, interfaces.ATTRIBUTE_NAME, None)

    def set(self, uuid):
        uuid = str(uuid)
        setattr(self.context, interfaces.ATTRIBUTE_NAME, uuid)
