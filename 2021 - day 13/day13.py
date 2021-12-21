import numpy as np
#import matplotlib.pyplot as plt

dimy = 10
dimx = 10 
folds = []
coords = []
with open("day13_input.txt","r") as f:
	for line_ind, line in enumerate(f):
		line = line.replace("\n","")
		if "," in line:
			these_coords = line.split(",")
			coords.append(np.array([int(these_coords[0]),int(these_coords[1])]))
		elif "fold along " in line:
			these_instr = line.split("fold along ")	
			this_fold = these_instr[1].split("=")
			folds.append((this_fold[0],int(this_fold[1])))
			
print(coords)

print(folds)
#part 1 
#folds = [folds[0]]
for this_fold in folds:
	
	fold_direction = this_fold[0]
	fold_centre = this_fold[1]
	
	for coord_ind,this_coord in enumerate(coords):
		if fold_direction == "x":
			if this_coord[0]>fold_centre:
				coords[coord_ind][0] = fold_centre-(coords[coord_ind][0]-fold_centre)
		
		else: #fold_direction == "x":
			if this_coord[1]>fold_centre:
				coords[coord_ind][1] = fold_centre-(coords[coord_ind][1]-fold_centre)
	
	unique_coords = []
	for this_coord in coords:
		unique = True
		for this_unique in unique_coords:
			if np.all(this_coord == this_unique):
				unique = False
				break
		if unique:
			unique_coords.append(this_coord)		
	coords = unique_coords

		
print("answer part 1: ")
print(len(coords))
print(" ")


final_coords = np.zeros((len(coords),2))
for this_ind,this_coord in enumerate(coords):
	final_coords[this_ind,0] = this_coord[0]
	final_coords[this_ind,1] = this_coord[1]

#plt.scatter(final_coords[:,1], final_coords[:,1])
print("")
print(final_coords)

#had to plot in excel due to import problems
answer = UFRZKAUZ
