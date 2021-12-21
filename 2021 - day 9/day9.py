import numpy as np
from itertools import islice

dimy = 5
dimx = 10

dimy = 100
dimx = 100 
this_map = np.zeros((dimy,dimx))
low_points = np.ones((dimy,dimx))
with open("day9_input.txt","r") as f:
	for line_ind, line in enumerate(f):
		line = line.replace("\n","")
		#print(line_ind,line)
		for char_ind, char in enumerate(line):
			#print(char_ind,char)
			this_map[line_ind,char_ind] = char

risk_level = 0
for line_ind,line in enumerate(this_map):
	
	for char_ind,char in enumerate(line):
		this_low = True
		if char_ind != 0:
			if this_map[line_ind,char_ind-1]<=this_map[line_ind,char_ind]:
				this_low = False
		if char_ind != dimx-1:
			if this_map[line_ind,char_ind+1]<=this_map[line_ind,char_ind]:
				this_low = False
		if line_ind != 0:
			if this_map[line_ind-1,char_ind]<=this_map[line_ind,char_ind]:
				this_low = False
		if line_ind != dimy-1:	
			if this_map[line_ind+1,char_ind]<=this_map[line_ind,char_ind]:
				this_low = False
		if not this_low:
			low_points[line_ind,char_ind]=0
		else:
			print(line_ind,char_ind,this_map[line_ind,char_ind])
			risk_level+=1+this_map[line_ind,char_ind]
print(this_map)
print(low_points)

print("answer part 1: ")
print(risk_level)
print(" ")
