import numpy as np

f=open("day3_input.txt","r")
input_list = [line for line in f.readlines()]
f.close()


high_count = np.array([0,0,0,0,0,0,0,0,0,0,0,0])
low_count = np.array([0,0,0,0,0,0,0,0,0,0,0,0])

for entry in input_list:
	for index, current_char in enumerate(entry[:-1]):
		print(index,current_char)
		high_count[index]+=int(current_char)
		low_count[index]+=1-int(current_char)
		

gamma = 0			
epsilon = 0	
		
current_power = 1
for i in range( len(high_count) - 1, -1, -1) :
	if high_count[i]>low_count[i]:
		gamma += current_power
	else:
		epsilon += current_power	
		
	current_power*=2		

ap1 = gamma*epsilon
print("answer part 1: ")
print(ap1)






