import numpy as np

lookup_dict = {}
with open("day14_input.txt") as f:
	start_string = f.readline().rstrip()
	f.readline()
	
	for dict_line in f:
		this_tag = dict_line[0:2]
		this_insert = dict_line[-2]
		lookup_dict[this_tag]=this_insert
		
print(lookup_dict)
print(start_string)
max_steps = 40

last_string = start_string
for it in range(0,max_steps):
	this_output = last_string[0]
	for char_index,this_char in enumerate(last_string[1:]):
		this_output += lookup_dict[last_string[char_index:char_index+2]]
		this_output += this_char
		
	#print(this_output)
	
	last_string = this_output

min_count = len(last_string)
max_count = 0

counted_chars = ""
string_len = len(last_string)
for this_char in last_string:
	if this_char not in counted_chars:
		this_count = string_len-len(last_string.replace(this_char,""))
		if this_count<min_count:
			min_count=this_count
		if this_count>max_count:
			max_count = this_count
		
		
		counted_chars+=this_char

diff = max_count-min_count
print("answer part 1: ")
print(diff)
print(" ")

