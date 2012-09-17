#!/usr/bin/env python2

import argparse
import sys

parser = argparse.ArgumentParser(description='Process some numbers.')
args = parser.parse_args()

product = 1
while 1:
    try:
        n = raw_input()
        product *= int(n)
    except EOFError:
        print product
        break
    except:
        if n == '':
            print product
            product = 1
        else:
            print "Could not convert string to float: %s" %n
            sys.exit(1)
            break
