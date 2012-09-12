# ECE 2524 Homework 2 Problem 1 Nick Strohl

with open('/etc/passwd', 'r') as f:
    for line in f:
        line = line.split(':')
        userName = line[0]
        pathName = line[6]
        print userName + "  " + pathName
