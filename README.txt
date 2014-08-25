plone.uuid
==========

This is a minimal package that can be used to obtain a universally unique
identifier (UUID) for an object.

The default implementation uses the Python standard library ``uuid`` module
to generate an RFC 4122-compliant UUID, using the ``uuid1()`` function. It
will assign a UUID upon object creation (by subscribing to
``IObjectCreatedEvent`` from ``zope.lifecycleevent``) and store it in an
attribute on the object.

  Why use an attribute and not annotations? The most common form of annotation
  is the one provided by ``IAttributeAnnotations``. This stores annotations in
  a BTree in an attribute called ``__annotations__``, which means that
  annotation values do not end up in the same ZODB persistent object as the
  parent. This is good for "large" values, but not very good for small ones
  that are frequently required, as it requires a separate ZODB object load.

Simple usage
============

To automatically assign a UUID to your objects using the default
implementation outlined above, you should:

* Make sure they implement ``plone.uuid.interfaces.IAttributeUUID``. You
  can do this in code, via the ``implements()`` directive, or in ZCML, with
  a statement like::

    <class class="my.package.MyClass">
        <implements interface="plone.uuid.interfaces.IAttributeUUID" />
    </class>

* Make sure that an ``IObjectCreatedEvent`` is fired for this object when it
  is first created.

Once the event handler has triggered, you can obtain a UUID by adapting the
object to the ``IUUID`` interface::

    from plone.uuid.interfaces import IUUID
    uuid = IUUID(context)

The ``uuid`` variable will now be a (byte) string containing a UUID. If the
UUID has not yet been assigned, adaptation will fail with a ``TypeError``.

If you would rather get ``None`` instead of a ``TypeError``, you can do::

    uuid = IUUID(context, None)

UUID view
=========

If you require a UUID in a page template or remotely, you can use the
``@@uuid`` view, which is registered for all objects that provide the
``IUUIDAware`` marker interface (which is a super-interface of the
``IAttributeUUID`` marker seen above).

For example::

    <div tal:attributes="id string:uuid-${context/@@uuid}">
        ...
    </div>

The view simply returns the UUID string as looked up by the ``IUUID`` adapter.

Customising behaviour
=====================

There are two primary customisation points for this package:

* You can change the default UUID generating algorithm by overriding the
  unnamed utility providing the ``IUUIDGenerator`` interface. The default
  implementation simply calls ``uuid.uuid1()`` and casts the result to a
  ``str``.
* You can change the UUID storage by providing a custom ``IUUID`` adapter
  implementation. If you do this, you must also provide a mechanism for
  assigning UUIDs upon object creation, usually via an event handler. To
  obtain a UUID, use the ``IUUIDGenerator`` interface::

    from zope.component import getUtility
    from plone.uuid.interfaces import IUUIDGenerator

    generator = getUtility(IUUIDGenerator)
    uuid = generator()

  You should also make sure that instances with a UUID provide a sub-interface
  of ``plone.uuid.interfaces.IUUIDAware``.
