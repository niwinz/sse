# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest
import sys

def to_unicode(data):
    if sys.version_info[0] >= 3: # Python 3
        return str(data)
    return unicode(data)

from sse import Sse


class ServerSentEventsProtocolTests(unittest.TestCase):
    def test_constructor(self):
        self.assertEqual(list(Sse()), ['retry: 2000\n\n'])
        self.assertEqual(list(Sse(default_retry=1000)), ['retry: 1000\n\n'])

    def test_add_message__simple_text(self):
        sse = Sse()

        sse.add_message("foo", "foo-message")
        sse.add_message("bar", "bar-message")

        self.assertEqual(to_unicode(sse), "retry: 2000\n\nevent: foo\ndata: "
                                          "foo-message\n\nevent: bar\ndata: "
                                          "bar-message\n\n")

        self.assertEqual(list(sse), [
            'retry: 2000\n\n',
            'event: foo\n',
            'data: foo-message\n',
            '\n',
            'event: bar\n',
            'data: bar-message\n',
            '\n'
        ])

    def test_add_message__simple_text_split(self):
        sse = Sse()
        sse.add_message("foo", "foo\nmessage")
        sse.add_message("bar", "bar\nmessage")

        self.assertEqual(list(sse), [
            'retry: 2000\n\n',
            'event: foo\n',
            'data: foo\n',
            'data: message\n',
            '\n',
            'event: bar\n',
            'data: bar\n',
            'data: message\n',
            '\n'
        ])

    def test_add_message__list(self):
        sse = Sse()

        sse.add_message("foo", ["foo-message"])
        sse.add_message("bar", ["bar-message"])

        self.assertEqual(list(sse), [
            'retry: 2000\n\n',
            'event: foo\n',
            'data: foo-message\n',
            '\n',
            'event: bar\n',
            'data: bar-message\n',
            '\n'
        ])

    def test_add_message__list_split(self):
        sse = Sse()
        sse.add_message("foo", ["foo\nmessage"])
        sse.add_message("bar", ["bar\nmessage"])

        self.assertEqual(list(sse), [
            'retry: 2000\n\n',
            'event: foo\n',
            'data: foo\n',
            'data: message\n',
            '\n',
            'event: bar\n',
            'data: bar\n',
            'data: message\n',
            '\n'
        ])

    def test_dinamic_methods(self):
        sse = Sse()
        sse.add_event_foo(text="bar")

        self.assertEqual(list(sse), ['retry: 2000\n\n', 'event: foo\n', 'data: bar\n', '\n'])

    def test_flush(self):
        sse = Sse()
        sse.add_message("foo", "bar")

        sse.flush()
        self.assertEqual(len(sse._buffer), 0)

    def test_flush_on_iter(self):
        sse = Sse()
        sse.add_message("foo", "bar")

        self.assertEqual(list(sse), ['retry: 2000\n\n', 'event: foo\n', 'data: bar\n', '\n'])
        self.assertEqual(list(sse), [])


if __name__ == "__main__":
    unittest.main()
