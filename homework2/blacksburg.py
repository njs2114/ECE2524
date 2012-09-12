# ECE 2524 Homework 2 Problem 2 Nick Strohl

print "ACCOUNT INFORMATION FOR BLACKSBURG RESIDENTS"
from sys import argv
script, filename = argv
with open(filename, 'r') as f:
    for line in f:
        line = line.split()
        firstName = line[0]
        lastName = line[1]
        amountOwed = line[2]
        phoneNumber = line[4]
        if line[3] == "Blacksburg":
            print phoneNumber + ", " + lastName + ", " + firstName + ", " + amountOwed
