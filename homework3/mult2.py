#!/usr/bin/env python2

import argparse
import sys
import fileinput

parser = argparse.ArgumentParser(description='Process some numbers.')
#parser.add_argument('--ignore-blank', nargs='?', const='c', default='d')
#parser.add_argument('--ignore-non-numeric', nargs='?', const='c', default='d')
parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default = sys.stdin)
args = parser.parse_args()

product = 1

for line in fileinput.input():
    try:
        n = line
        product *= int(n)
    except EOFError:
        print product
        break
    except:
        if n == '\n':
            print product
            product = 1
        else:
            print "Could not convert string to float: %s" %n
            sys.exit(1)
            break
print product
