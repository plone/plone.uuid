import unittest


class TestUUID(unittest.TestCase):
    def setUp(self):
        from zope.configuration import xmlconfig

        import plone.uuid
        import zope.component.testing

        zope.component.testing.setUp()
        xmlconfig.file("configure.zcml", plone.uuid)

    def tearDown(self):
        import zope.component.testing

        zope.component.testing.tearDown()

    def test_default_generator(self):
        from plone.uuid.interfaces import IUUIDGenerator
        from zope.component import getUtility

        generator = getUtility(IUUIDGenerator)

        uuid1 = generator()
        uuid2 = generator()

        self.assertNotEqual(uuid1, uuid2)
        self.assertTrue(isinstance(uuid1, str))
        self.assertTrue(isinstance(uuid2, str))

    def test_attribute_uuid_not_set(self):
        from plone.uuid.interfaces import IAttributeUUID
        from plone.uuid.interfaces import IUUID
        from zope.interface import implementer

        @implementer(IAttributeUUID)
        class Context:
            pass

        context = Context()

        uuid = IUUID(context, None)
        self.assertEqual(uuid, None)

    def test_attribute_uuid_create_handler(self):
        from plone.uuid.interfaces import ATTRIBUTE_NAME
        from plone.uuid.interfaces import IAttributeUUID
        from plone.uuid.interfaces import IUUID
        from zope.event import notify
        from zope.interface import implementer
        from zope.lifecycleevent import ObjectCopiedEvent
        from zope.lifecycleevent import ObjectCreatedEvent

        @implementer(IAttributeUUID)
        class Context:
            pass

        context = Context()
        notify(ObjectCreatedEvent(context))

        uuid = IUUID(context, None)
        self.assertNotEqual(uuid, None)
        self.assertTrue(isinstance(uuid, str))

        # calling handler again won't change if UUID already present:
        notify(ObjectCreatedEvent(context))
        self.assertEqual(uuid, IUUID(context, None))

        # ...except when the UUID attribute was the result of a copy
        copied = Context()
        setattr(copied, ATTRIBUTE_NAME, IUUID(context, None))
        self.assertNotEqual(IUUID(copied, None), None)  # mimic copied state
        self.assertEqual(uuid, IUUID(copied, None))  # before handler
        notify(ObjectCopiedEvent(copied, original=context))
        self.assertNotEqual(uuid, None)
        self.assertNotEqual(uuid, IUUID(copied, None))  # copy has new UID

    def test_uuid_view_not_set(self):
        from plone.uuid.interfaces import IAttributeUUID
        from zope.component import getMultiAdapter
        from zope.interface import implementer
        from zope.publisher.browser import TestRequest

        @implementer(IAttributeUUID)
        class Context:
            pass

        context = Context()

        request = TestRequest()
        view = getMultiAdapter((context, request), name="uuid")
        response = view()

        self.assertEqual("", response)
        self.assertTrue(isinstance(response, str))

    def test_uuid_view(self):
        from plone.uuid.interfaces import IAttributeUUID
        from plone.uuid.interfaces import IUUID
        from zope.component import getMultiAdapter
        from zope.event import notify
        from zope.interface import implementer
        from zope.lifecycleevent import ObjectCreatedEvent
        from zope.publisher.browser import TestRequest

        @implementer(IAttributeUUID)
        class Context:
            pass

        context = Context()
        notify(ObjectCreatedEvent(context))

        uuid = IUUID(context, None)

        request = TestRequest()
        view = getMultiAdapter((context, request), name="uuid")
        response = view()

        self.assertEqual(str(uuid), response)
        self.assertTrue(isinstance(response, str))

    def test_uuid_mutable(self):
        from plone.uuid import interfaces
        from zope import event
        from zope import interface
        from zope import lifecycleevent

        @interface.implementer(interfaces.IAttributeUUID)
        class Context:
            pass

        context = Context()
        event.notify(lifecycleevent.ObjectCreatedEvent(context))

        mutable = interfaces.IMutableUUID(context)

        uuid1 = mutable.get()
        mutable.set("a uuid to set")
        uuid2 = mutable.get()
        uuid3 = interfaces.IUUID(context)

        self.assertTrue(uuid1 != uuid2)
        self.assertTrue(uuid2 == uuid3)
