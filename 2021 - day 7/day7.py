import numpy as np


f=open("day7_input.txt","r")
for line in f.readlines():
	splits = line.split(',')
	crab_pos = np.zeros(len(splits))
	for ind,crab in enumerate(splits):
		crab_pos[ind]=int(crab)
f.close()

#print(crab_pos)

opt_pos = 0
opt_dev = 100000000
for this_pos in range(int(np.amin(crab_pos)),int(np.amax(crab_pos))+1):
	this_dev = sum(abs(crab_pos-this_pos))
	if this_dev<opt_dev:
		opt_dev = this_dev
		opt_pos = this_pos

print("answer part 1: ")
print(opt_dev)


opt_pos = 0
opt_dev = 100000000
for this_pos in range(int(np.amin(crab_pos)),int(np.amax(crab_pos))+1):
	this_dev = 0
	for this_crab in crab_pos:
		this_dev += sum(range(1,int(abs(this_crab-this_pos))+1))
	if this_dev<opt_dev:
		opt_dev = this_dev
		opt_pos = this_pos

print("answer part 2: ")
print(opt_dev)
