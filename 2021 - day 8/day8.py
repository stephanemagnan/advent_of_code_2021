import numpy as np

easy_count = 0
f=open("day8_test_input.txt","r")
for line in f.readlines():
	splits = line.replace("\n","")
	splits = splits.split('|')
	#print(splits)
	results = splits[1].split(' ')
	
	for this_out in results:
		if  len(this_out) == 2 or len(this_out) == 4 or len(this_out) == 3 or len(this_out) == 7 :
			easy_count +=1
f.close()

print("answer part 1: ")
print(easy_count)
print(" ")

segment_sum = 0
segment_letters = 'abcdefg'
f=open("day8_input.txt","r")
for line in f.readlines():
	segment_counts = np.zeros(7)
	splits = line.replace("\n","")
	splits = splits.split('|')
	#print(splits)
	results = splits[0].split(' ')
	
	for this_digit in results:
		if  segment_letters[0] in this_digit:
			segment_counts[0] +=1
		if  segment_letters[1] in this_digit:
			segment_counts[1] +=1
		if  segment_letters[2] in this_digit:
			segment_counts[2] +=1
		if  segment_letters[3] in this_digit:
			segment_counts[3] +=1
		if  segment_letters[4] in this_digit:
			segment_counts[4] +=1
		if  segment_letters[5] in this_digit:
			segment_counts[5] +=1
		if  segment_letters[6] in this_digit:
			segment_counts[6] +=1		
		if len(this_digit) == 2:
			one_segments = this_digit		
		if len(this_digit) == 3:
			seven_segments = this_digit		
		if len(this_digit) == 4:
			four_segments = this_digit	
	#print(one_segments,four_segments,seven_segments)
	for this_7seg in seven_segments:
		if this_7seg not in one_segments:
			segment_A = this_7seg
			#print("A ",segment_A)	
			break
	
	for index,this_seg in enumerate(segment_counts):
		#print(index,this_seg)
		
		if this_seg == 6:
			segment_B = segment_letters[index]	
			#print("B ",segment_B)	
		if this_seg == 4:
			segment_E = segment_letters[index]
			#print("E ",segment_E)			
		if this_seg == 9:
			segment_F = segment_letters[index]	
			#print("F ",segment_F)		
		if this_seg == 8:
			if segment_letters[index] != segment_A:
				segment_C = segment_letters[index]
				#print("C ",segment_C)	
		if this_seg == 7:
			if segment_letters[index] in four_segments:
				segment_D = segment_letters[index]	
				#print("D ",segment_D)	
			else:
				segment_G = segment_letters[index]
				#print("G ",segment_G)																			
			
	zero_string = ''.join(sorted(segment_A+segment_B+segment_C+segment_E+segment_F+segment_G))
	one_string = ''.join(sorted(segment_C+segment_F))
	two_string = ''.join(sorted(segment_A+segment_C+segment_D+segment_E+segment_G))
	three_string = ''.join(sorted(segment_A+segment_C+segment_D+segment_F+segment_G))
	four_string = ''.join(sorted(segment_B+segment_C+segment_D+segment_F))
	five_string = ''.join(sorted(segment_A+segment_B+segment_D+segment_F+segment_G))
	six_string = ''.join(sorted(segment_A+segment_B+segment_D+segment_E+segment_F+segment_G))
	seven_string = ''.join(sorted(segment_A+segment_C+segment_F))
	eight_string = ''.join(sorted(segment_A+segment_B+segment_C+segment_D+segment_E+segment_F+segment_G))
	nine_string = ''.join(sorted(segment_A+segment_B+segment_C+segment_D+segment_F+segment_G))
			
	this_num = 0
	
	displays = splits[1].split(' ')
	print(displays)
	for this_display in displays:
		
		this_len = len(this_display)
		if this_len == 2:
			this_num = 10*this_num + 1
		elif this_len == 3:
			this_num = 10*this_num + 7
		elif this_len == 4:
			this_num = 10*this_num + 4			
		elif this_len == 5:
			if ''.join(sorted(this_display)) == two_string:
				this_num = 10*this_num + 2			
			elif ''.join(sorted(this_display)) == three_string:
				this_num = 10*this_num + 3			
			elif ''.join(sorted(this_display)) == five_string:
				this_num = 10*this_num + 5			
		elif this_len == 6:
			if ''.join(sorted(this_display)) == zero_string:
				this_num = 10*this_num + 0			
			elif ''.join(sorted(this_display)) == six_string:
				this_num = 10*this_num + 6			
			elif ''.join(sorted(this_display)) == nine_string:
				this_num = 10*this_num + 9					
		elif this_len == 7:
			this_num = 10*this_num + 8
	
	print(this_num)
		
	
	segment_sum += this_num	
			
f.close()
#print(segment_letters)
#print(segment_counts)
#print(segment_A,segment_B,segment_C,segment_D,segment_E,segment_F,segment_G)
print("answer part 2: ")
print(segment_sum)
