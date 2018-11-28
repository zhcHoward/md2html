# -*- coding: utf-8 -*-

from backend.utils import Buffer


class Tag(object):
    reg = r''
    multiple = False

    def __init__(self, children=None, buf_len=0):
        self.buffer = Buffer(buf_len)
        self.name = self.__class__.__name__
        self.type = 'html'
        self.children = children if children else []

    def parse(self, reader):
        raise NotImplementedError


class SingleLineTag(Tag):
    def parse(self, reader):
        self.content = reader.readline().rstrip()  # remove tailing '\n'
        return self


class BlockTag(Tag):
    pass


class InlineTag(Tag):
    pass


