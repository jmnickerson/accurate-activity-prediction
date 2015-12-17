import numpy as np
import pylab as pl
import os
from collections import defaultdict


def PlotErrors(errors):
	pl.plot(errors)
	pl.title('Total Error')
	pl.ylabel('Total Error')
	pl.xlabel('Iteration')
	pl.show()

errors = []
out = []
f = open('output8_1000trn2.txt', 'r')
outMaxIndex = 0
totalCorrect = 0
totalWrong = 0
secondChance = 0
out = []
matrix = [[0 for x in range(16)] for x in range(16)]
outCount = [0 for x in range(16)]

for line in f:
	if "Total error:" in line:
		print line
		fields = line.split()
		error = fields[2]
		errors.append(float(error))
	if "out" in line:
		trimmedLine = line[line.find("[")+1:line.find("]")]
		#print trimmedLine
		splitLine = trimmedLine.split(",")
		out = [float(item) for item in splitLine]
		max_value = max(out)
		outMaxIndex = out.index(max_value)
		print "OutmaxIndex: " + str(outMaxIndex)
	if "correct" in line:
		trimmedLine = line[line.find("[")+1:line.find("]")]
		#print trimmedLine
		splitLine = trimmedLine.split(",")
		correct = [float(item) for item in splitLine]
		max_value = max(correct)
		correctMaxIndex = correct.index(max_value)
		matrix[outMaxIndex][correctMaxIndex] += 1
		outCount[correctMaxIndex] += 1
		print "OutCorrectIndex: " + str(correctMaxIndex)
		if outMaxIndex == correctMaxIndex:
			totalCorrect += 1
		else:
			out[outMaxIndex] = -1
			max_value = max(correct)
			secondChanceIndex = correct.index(max_value)
			print "Second Chance: " + str(secondChanceIndex)
			if secondChanceIndex == correctMaxIndex:
				#print "Correct on Second Try!"
				secondChance += 1
			totalWrong += 1
		print "\n"
testsum = 0
for j in range(16):
	for i in range(16):
		print str(matrix[i][j]) + " ",
		if i == j:
			testsum += matrix[i][j]
	print "\n"
for i in range(16):
	print str(outCount[i]) + " ",
	

print "Total Correct: " + str(totalCorrect) + " TESTSUM " + str(testsum)
print "Total Second Chance: " + str(secondChance)
print "Total Wrong: " + str(totalWrong)
print "Percentage: " + str(totalCorrect/(totalCorrect+float(totalWrong)))
print "Percentage With Second Chance: " + str((totalCorrect+secondChance)/(totalCorrect+float(totalWrong)))

#PlotErrors(errors)
	

