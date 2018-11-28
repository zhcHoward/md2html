# -*- coding: utf-8 -*-

import re

from tags.h import H


class Buffer(object):
    """A class works like string with limited length."""
    def __init__(self, length=1, content=''):
        self.length = length
        self.content = content[:length] if length > 0 else content

    def append(self, string):
        if self.length > 0:
            self.content = (self.content + string)[-self.length:]
        else:
            self.content += string

    def pop(self):
        content = self.content
        self.content = ''
        return content

    def __add__(self, other):
        buf = Buffer(length=self.length, content=self.content)
        buf.append(other)
        return buf

    def __radd__(self, other):
        return other + self.content

    def __iadd__(self, other):
        self.append(other)
        return self

    def __eq__(self, other):
        if isinstance(other, Buffer):
            return self.content == other.content and self.length == other.length
        else:
            return self.content == other

    def __str__(self):
        return self.content

    def __repr__(self):
        return "Buffer(length={}, content='{}')".format(self.length, self.content)


class State(object):
    def __init__(self):
        self.line_start = True
        self.buffer = Buffer(0)

    def update(self, **kwargs):
        for k, v in kwargs:
            setattr(self, k, v)

    def guessTag(self):
        if self.line_start:
            # check for all tags
            pass
        else:
            # check inline tags
            pass
        if re.match(r'#{1,6}', self.buffer.content):
            return H

        return None
