#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

if len(sys.argv) < 2:
    sys.exit(1)


def isComment(line: str) -> bool:
    return line.lstrip().startswith(";")


total = 0
cur_length = 1

lines = (
    line.strip()
    for line in open(sys.argv[1], "r")
    if not isComment(line) and "E" in line
)

for line in lines:
    tmp_length = float([leng[1:] for leng in line.split() if leng.startswith("E")][0])
    if tmp_length > cur_length:
        cur_length = tmp_length
    else:
        total += tmp_length
        cur_length = 0
print(total)
