from plone.uuid.interfaces import ATTRIBUTE_NAME
from plone.uuid.interfaces import IAttributeUUID
from plone.uuid.interfaces import IUUIDGenerator
from zope.component import adapter
from zope.component import queryUtility
from zope.lifecycleevent.interfaces import IObjectCopiedEvent
from zope.lifecycleevent.interfaces import IObjectCreatedEvent


try:
    from Acquisition import aq_base
except ImportError:

    def aq_base(obj):
        # soft-dependency on Zope2, fallback
        return obj


@adapter(IAttributeUUID, IObjectCreatedEvent)
def addAttributeUUID(obj, event):
    if not IObjectCopiedEvent.providedBy(event):
        if getattr(aq_base(obj), ATTRIBUTE_NAME, None):
            return  # defensive: keep existing UUID on non-copy create

    generator = queryUtility(IUUIDGenerator)
    if generator is None:
        return

    uuid = generator()
    if not uuid:
        return

    setattr(obj, ATTRIBUTE_NAME, uuid)
