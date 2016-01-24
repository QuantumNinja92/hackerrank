#!/bin/python

import sys


n = int(raw_input().strip())
formatS = "{:>"+str(n)+"}"
s = "#"
for i in range(0,n):
    print formatS.format(s)
    s+="#"