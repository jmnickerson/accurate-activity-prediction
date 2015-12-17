# Created by James McCabe Nickerson
# for CS 6600 at Utah State University

# This program reads data files from the CASAS project
# see http://casas.wsu.edu/
# and analyzes them for what types of data is in each file in a directory

import os
from collections import defaultdict
# Path of data files
path = 'Data/rawdata'

# Loop through every directory entry at path
for dir_entry in os.listdir(path):
	dir_entry_path = os.path.join(path,dir_entry)
	if os.path.isfile(dir_entry_path):
		# Ignore backup files
		if "~" not in dir_entry:
			# Initialize counters
			activityCount = 0
			powerCount = 0
			motionCount = 0
			activities = defaultdict(int)
			sensors = []
			dates = []
			print "File: " + dir_entry
			with open(dir_entry_path,'r') as my_file:
				for line in my_file:
						fields = line.split()
						date = fields[0]
						time = fields[1]
						sensor = fields[2]
						if date not in dates:
							dates.append(date)
						if len(fields) > 3:
							value = fields[3]
							if "M" in sensor:
								motionCount += 1
							if "P" in sensor:
								powerCount += 1
							# If there are more than 4 items, it must be an activity
							if len(fields) > 4 and "SG" not in sensor:
								note =  fields[4] + " " + fields[5]
								activityCount = activityCount + 1
								#if fields[4] not in activities:
								activities[fields[4]] += 1
				print "Number of Activities: " + str(len(activities)) + "  Activity Occurances: " + str(activityCount)
				print "Power Recorded: ", + powerCount
				print "Number of Days: " + str(len(dates))
			if activities:
				print "Activities Summary"
			for k,v in activities.iteritems():
				print k + " " + str(v/2)
			# Add newline after each file is displayed
			print "" 
				
