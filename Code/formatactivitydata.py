import numpy as np
import pylab as pl
import os

from collections import namedtuple
from collections import defaultdict
path = 'Data/rawdata/tulum2data'
numOfActivities = 16
numOfSensors = 31
activities = defaultdict(bool)
sensors = defaultdict(bool)
activitystart = True

# Initialize activities and sensors
infile = open(path,'r')
for line in infile:
	fields = line.split()
	if len(fields) > 4:
		activities[fields[4]] = False
	if "M" in fields[2]:
		sensors[fields[2]] = True;
infile.close()

infile = open(path,'r')
outfile = open("activityoutput.txt",'w')
outfile.write("Inputs: " + str(len(sensors)) + " Outputs: " + str(len(activities)) + "\n")
for line in infile:
	fields = line.split()
	date = fields[0]
	time = fields[1]
	sensor = fields[2]
	if len(fields) > 3:						
		if len(fields) > 4:
			#Activity Label
			note =  fields[4]
			if activitystart:
				activitystart = False
				for k,v in sensors.iteritems():
					sensors[k] = False
				for k,v in activities.iteritems():
					activities[k] = False
			else:
				activitystart = True
				activities[note] = True
				for k,v in sensors.iteritems():
					outfile.write(str(int(v)) + " ")
				for k,v in activities.iteritems():
					outfile.write(str(int(v)) + " ")
				outfile.write ('\n')
		else:
			if "M" in sensor:
				sensors[sensor] = True;
for k,v in activities.iteritems():
	print k
	
