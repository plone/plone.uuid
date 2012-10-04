import uuid

from zope import interface
from zope import component

from plone.uuid import interfaces


@interface.implementer(interfaces.IUUID)
@component.adapter(interfaces.IAttributeUUID)
def attributeUUID(context):
    return getattr(context, interfaces.ATTRIBUTE_NAME, None)


class MutableAttributeUUID(object):
    interface.implements(interfaces.IMutableUUID)
    component.adapts(interfaces.IAttributeUUID)

    def __init__(self, context):
        self.context = context

    def get(self):
        return getattr(self.context, interfaces.ATTRIBUTE_NAME, None)

    def set(self, uuid):
        uuid = str(uuid)
        setattr(self.context, interfaces.ATTRIBUTE_NAME, uuid)


@interface.implementer(interfaces.IUUIDObject)
@component.adapter(interfaces.IUUID)
def uuid_object(context):
    uid_str = interfaces.IUUID(context, None)
    if uid_str is None:
        return None
    return uuid.UUID(uid_str)


@interface.implementer(interfaces.IUUID)
@component.adapter(interfaces.IUUIDObject)
def uuid_serialized(context):
    return str(context)


# classImplements here to avoid complex package dependencies
# necessary for <class...> in ZCML.
interface.classImplements(uuid.UUID, interfaces.IUUIDObject)
