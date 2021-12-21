import numpy as np

f=open("day3_input.txt","r")
input_list = [line for line in f.readlines()]
f.close()


high_count = np.array([0,0,0,0,0,0,0,0,0,0,0,0])
low_count = np.array([0,0,0,0,0,0,0,0,0,0,0,0])
#high_count = np.array([0,0,0,0,0])
#low_count = np.array([0,0,0,0,0])

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

print(gamma)
print(epsilon)
ap1 = gamma*epsilon
print("answer part 1: ")
print(ap1)
print(" ")

remaining_list = input_list
print(remaining_list)
for index,var in enumerate(high_count):
	low_list = []
	high_list = []
	print(high_list)
	print(low_list)
	for entry in remaining_list:
		if entry[index] == '1':
			high_list.append(entry)
		else:
			low_list.append(entry)
		if len(high_list)>=len(low_list):
			remaining_list = high_list
		else:
			remaining_list = low_list	

	print(high_list)
	print(low_list)
	if len(remaining_list) == 1:
		break
	
print("high list",high_list)	
oxygen_string = high_list[0]
oxygen = int(oxygen_string,2)
print(oxygen)
print(" ")
		
remaining_list = input_list
print(remaining_list)
for index,var in enumerate(high_count):
	low_list = []
	high_list = []
	print(high_list)
	print(low_list)
	for entry in remaining_list:
		if entry[index] == '1':
			high_list.append(entry)
		else:
			low_list.append(entry)
		if len(high_list)>=len(low_list):
			remaining_list = low_list
		else:
			remaining_list = high_list	

	print(high_list)
	print(low_list)
	if len(remaining_list) == 1:
		break
	
print("low list",low_list)	
co2_string = low_list[0]
co2 = int(co2_string,2)
print(co2)
print(" ")


ap2 = oxygen*co2
print("answer part 2: ")
print(ap2)
print(" ")
