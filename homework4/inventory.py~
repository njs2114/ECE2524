#!/usr/bin/env python2

import argparse
import sys
import fileinput
import shlex

def add(data):
    print "sorry, not implemented yet"
    return

def remove(data):
    print "sorry, not implemented yet"
    return

def list(data):
    datLength = len(data)
    if datLength < 2:
        i = 0
        j = 0
        while j < len(inlist):
            while i < 4:
                if j > 3:
                    print "%s: %s" % (inlist[i], inlist[j])
                i = i+1
                j = j+1
            print
            i = 0
    if datLength is 2:
        sort()
    if datLength is 3:
        i = 0
        j = 0
        while j < len(inlist): # in the list
            while i < 4: # single entry
                if i is 3 and j > 3: # quantity and not label
                    if inlist[j] is data[2]:
                        i = 0
                        j = j-3
                        while i < 4:
                            print "%s: %s" % (inlist[i], inlist[j])
                            i = i+1
                            j = j+1
                        print
                        i = 0
                if j < len(inlist):
                    i = i+1
                    j = j+1
                else:
                    return
            i = 0    
    return

def update(data):
    ID = data[3]
    if len(data) is 4:
        i = 0
        j = 0
        while j < len(inlist):
            while i < 4:
                if i is 0 and j > 3:
                    if inlist[j] == ID:
                        inlist[j+3] = data[1]

                i = i+1
                j = j+1
            i = 0    
    return

def sort():
    print "sorry, not implemented yet"
    return
    
def exit(data):
    sys.exit(0)

if __name__ == '__main__':  
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--data-file')
    args = parser.parse_args()
    
    inlist = []
    
    filename = sys.argv[2]
    body = file(filename).read()

    lexer = shlex.split(body)
    for token in lexer:
        inlist.append(token) # store the input in a list
        
while(1):
    try:
        cmdLine = sys.stdin.readline()
        if cmdLine == '\n':
            cmdLine = "enter"
        cmdParts = shlex.split(cmdLine)
        cmdType = cmdParts[0]
        cmdParts.pop(0)
    except KeyboardInterrupt:
        sys.exit(0)
        
    commands = {'add': add, 'remove': remove, 'list': list, 'set': update, 'exit': exit}
    try:
        commands[cmdType](cmdParts)
    except KeyError as e:
        sys.stderr.write("Invalid command: {}\n".format(cmdType))
        sys.stderr.write("Valid commands are:\nadd <part info string>\nremove <PartID>\nlist all (optional: Quantity <Quantity>)\nset Quantity <Quantity> for <PartID>\nlist all sort\nexit\n")
    


