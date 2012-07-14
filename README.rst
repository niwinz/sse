sse
===

Server Sent Events protocol implemetation on python2 and python3 in the same codebase.


Python tested versions:
-----------------------

* Python 2.7.x
* Python 3.2.x
* PyPy 1.9.0r


Api documentation:
------------------

``Sse.__init__(default_retry=2000)``

    Constructor. On this method is called, automaticali initialize the internal
    buffer with retry statement with 2000ms as default value.

``Sse.set_retry(num)``

    Method for set a custom retry value on initialized Sse intance.

``Sse.set_event_id(event_id)``

    The specification of sse indicates that you can put ids to events. For
    more info, see: http://www.w3.org/TR/eventsource/#concept-event-stream-last-event-id

    With this method, can set or reset the id value.

``Sse.reset_event_id()``

    Helper method for reseting event id.

``Sse.add_message(event, text, encoding='utf-8')``

    Method for add messages to the buffer and associate this messages to events.
    The event parameter can be a unicode string and text can be string, list,
    tuple or set.

``Sse.flush()``

    Clears the internal buffer.

``Sse.__str__()``

    Returns a raw output of buffer, ready for set to client.
    **NOTE**: this method will be used only on python3.

``Sse.__unicode__()``

    Returns a raw output of buffer. Same as ``__str__`` but returns unicode
    value on python2. Is not used on python3.


Aditional info:
---------------

* Sse instance object can be used as iterator. On finish the iteration the internal buffer is automaticaly cleared.
* Can use dynamic methods ``Sse.add_event_eventname(text='foo')`` as alias of ``Sse.add_message('eventname', 'foo')``

License:
--------

BSD License
