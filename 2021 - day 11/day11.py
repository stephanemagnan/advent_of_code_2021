import numpy as np


dimy = 10
dimx = 10 
this_map = np.zeros((dimy,dimx))
flashed_coords = np.zeros((dimy,dimx))
pending_coords = np.zeros((dimy,dimx))
with open("day11_input.txt","r") as f:
	for line_ind, line in enumerate(f):
		line = line.replace("\n","")
		#print(line_ind,line)
		for char_ind, char in enumerate(line):
			#print(char_ind,char)
			this_map[line_ind,char_ind] = int(char)

print(this_map)
max_steps = 1000

flash_count = 0
for i in range(0,max_steps):
	this_flash_count = 0
	#increment
	this_map+=1
	bust_count = np.count_nonzero(this_map>9)
	while bust_count>0:
		for row_ind,row in enumerate(this_map):
			for col_ind,col in enumerate(row):
				if col >9:
					this_map[row_ind,col_ind] = 0
					this_flash_count +=1
					nw = True
					n = True
					ne = True
					e = True
					se = True
					s = True
					sw = True
					w = True
					
					if col_ind == 0:
						nw = False
						w = False
						sw = False
					if col_ind == dimx-1:
						ne = False
						e = False
						se = False
					if row_ind == 0:
						nw = False
						n = False
						ne = False
					if row_ind == dimy-1:
						sw = False
						s = False
						se = False
					
					if nw:
						if this_map[row_ind-1,col_ind-1] !=0:
							this_map[row_ind-1,col_ind-1]+=1
					if n:
						if this_map[row_ind-1,col_ind] !=0:
							this_map[row_ind-1,col_ind]+=1
					if ne:
						if this_map[row_ind-1,col_ind+1] !=0:
							this_map[row_ind-1,col_ind+1]+=1
					if w:
						if this_map[row_ind,col_ind-1] !=0:
							this_map[row_ind,col_ind-1]+=1
					if e:
						if this_map[row_ind,col_ind+1] !=0:
							this_map[row_ind,col_ind+1]+=1
					if sw:
						if this_map[row_ind+1,col_ind-1] !=0:
							this_map[row_ind+1,col_ind-1]+=1
					if s:
						if this_map[row_ind+1,col_ind] !=0:
							this_map[row_ind+1,col_ind]+=1
					if se:
						if this_map[row_ind+1,col_ind+1] !=0:
							this_map[row_ind+1,col_ind+1]+=1																																																					
		
		bust_count = np.count_nonzero(this_map>9)
		#print(this_map)
		#print(bust_count)
		#if i ==1:
		#	break
		
	print(this_map)
	flash_count+=this_flash_count
	if this_flash_count == dimx*dimy:
		print("answer part 2: ")
		print(i+1)
		print(" ")
		break



print("answer part 1: ")
print(flash_count)
print(" ")
