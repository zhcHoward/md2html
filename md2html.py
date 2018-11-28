# -*- coding: utf-8 -*-

from tags.base import Tag
from utils import State

ONE_LINE_TAG = ('#', '*', '-', '+', r'\d+\.', '>', '- [ ]')
BLOCK_TAG = ('```',)
INLINE_TAG = ('**', '*')
tags = ('#', '*', '-', '+', '**', '`', '|', '!', '[', *(str(i) for i in range(10)), '>')
inline_tag = ('*', '')
ESCAPE_CHAR = '\\'
with open('test.md') as reader:
    parse(reader)

space = 0
instance = None
tag = ''
indent = ''
escape = False

root = Tag()
def parse(content):
    line_start = True
    escape = False

    for char in content:
        if escape:
            tag.children += char
            escape = False
            continue

