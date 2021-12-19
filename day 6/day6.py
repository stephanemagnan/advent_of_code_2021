import numpy as np

fish_tracker = np.zeros(9)

f=open("day6_input.txt","r")
for line in f.readlines():
	splits = line.split(',')
	for fish in splits:
		fish_tracker[int(fish)]+=1
f.close()


days = 256

for day in range(0,days):
	repros = fish_tracker[0]
	fish_tracker[0:8] = fish_tracker[1:]
	fish_tracker[6]+=repros
	fish_tracker[8]=repros 
	print(fish_tracker)

print(fish_tracker)

count = np.sum(fish_tracker)
print("answer part 1: ")
print(count)
