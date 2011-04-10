from zope.component import adapter
from zope.component import queryUtility

from zope.lifecycleevent.interfaces import IObjectCreatedEvent

from plone.uuid.interfaces import IUUIDGenerator
from plone.uuid.interfaces import IAttributeUUID

from plone.uuid.interfaces import ATTRIBUTE_NAME


@adapter(IAttributeUUID, IObjectCreatedEvent)
def addAttributeUUID(obj, event):

    generator = queryUtility(IUUIDGenerator)
    if generator is None:
        return

    uuid = generator()
    if not uuid:
        return

    setattr(obj, ATTRIBUTE_NAME, uuid)
