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
			#risk_level+=1+this_map[line_ind,char_ind]
#print(this_map)
#print(low_points)

print("answer part 1: ")
print(risk_level)
print(" ")


this_low_map = np.zeros((dimy,dimx))
next_region_id = -1
for line_ind,line in enumerate(this_map):
	for char_ind,char in enumerate(line):
		if this_map[line_ind,char_ind] !=9:
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
			if this_low:
				this_low_map[line_ind,char_ind] = next_region_id
				next_region_id-=1
		else: 
			this_low_map[line_ind,char_ind] = 1


#loop through, expanding every time
it = 0
while np.count_nonzero(this_low_map==0)>0:
	for line_ind,line in enumerate(this_map):
		for char_ind,char in enumerate(line):
			if this_map[line_ind,char_ind] !=9:
				local_min = this_low_map[line_ind,char_ind]
				
				if char_ind != 0:
					if this_low_map[line_ind,char_ind-1]<this_low_map[line_ind,char_ind]:
						local_min = this_low_map[line_ind,char_ind-1]
				if char_ind != dimx-1:
					if this_low_map[line_ind,char_ind+1]<this_low_map[line_ind,char_ind]:
						local_min = this_low_map[line_ind,char_ind+1]
				if line_ind != 0:
					if this_low_map[line_ind-1,char_ind]<this_low_map[line_ind,char_ind]:
						local_min = this_low_map[line_ind-1,char_ind]
				if line_ind != dimy-1:	
					if this_low_map[line_ind+1,char_ind]<this_low_map[line_ind,char_ind]:
						local_min = this_low_map[line_ind+1,char_ind]
				
				this_low_map[line_ind,char_ind] = local_min
	it+=1
	if it >100:
		break
print(this_low_map)
region_sizes = np.zeros((-next_region_id-1))
for region_id in range(-1,next_region_id,-1):
	region_sizes[-region_id-1] = np.count_nonzero(this_low_map==region_id)
	print(region_id,region_sizes[-region_id-1])
		
sorted_regions = np.sort(region_sizes)

prod = sorted_regions[-1]*sorted_regions[-2]*sorted_regions[-3]	
print(sorted_regions)
print("answer part 2: ")
print(prod)
print(" ")		
			
