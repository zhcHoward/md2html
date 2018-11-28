#! -*- coding: utf-8 -*-

from tags.base import InlineTag
from utils import Buffer


class Strong(InlineTag):
    end_tag = '**'

    def __init__(self):
        self.buffer = Buffer(2)
        super().__init__()

    def parse(self, reader):
        for char in reader.read(1):
            self.buffer.append(char)
            if self.buffer == self.end_tag:
                return self
            else:
                self.content += char
