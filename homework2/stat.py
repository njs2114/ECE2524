# ECE 2524 Homework 2 Problem 3 Nick Strohl

from sys import argv
script, filename = argv
maxAmount = 0
minAmount = 9999
count = 0
totalAmount = 0
with open(filename, 'r') as f:
    for line in f:
        newline = line.split()
        person = newline[1]
        amount = float(newline[2])
        totalAmount = totalAmount + amount
        if amount > maxAmount:
            maxAmount = amount
            maxPerson = person
        if amount < minAmount:
            minAmount = amount
            minPerson = person
        count = count + 1

avgAmount = totalAmount/count

print "ACCOUNT SUMMARY"
print "Total amount owed =", totalAmount
print "Average amount owed =", avgAmount
print "Maximum amount owed =", maxAmount, " by ", maxPerson
print "Minimum amount owed =", minAmount, " by ", minPerson
