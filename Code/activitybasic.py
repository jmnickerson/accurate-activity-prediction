import pybrain
import numpy as np

from pybrain.datasets.supervised import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
numOfInputs = 0
numOfOutputs = 0
		
f = open('activityoutput.txt','r')
line = f.readline();
linearr = line.split()
numOfInputs = linearr[1]
numOfOutputs = linearr[3]
print str(numOfInputs) + " " + str(numOfOutputs)
f.close()

ds = SupervisedDataSet(int(numOfInputs),int(numOfOutputs))

inputFile = open('activityoutput.txt','r')
firstline = True
for line in inputFile.readlines():
	if firstline:
		firstline = False
	else:
		data = [int(x) for x in line.strip().split() if x != '']
		indata =  data[:int(numOfInputs)]
		outdata = data[int(numOfInputs):]
		ds.addSample(indata,outdata)
test_data, train_data = ds.splitWithProportion(0.20)
print str(len(test_data)) + " " + str(len(train_data))

n = buildNetwork(ds.indim,4,4,ds.outdim)
t = BackpropTrainer(n,verbose=True)

t.trainOnDataset(train_data,10000)
t.testOnData(test_data,verbose=True)
out = n.activateOnDataset(ds)


