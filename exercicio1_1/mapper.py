#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys

for line in sys.stdin:
	if line == "\t": continue
	else:	
		data = line.strip().split("\t")
		date, time, store, item, cost, payment = data
		print(store+"\t"+cost)