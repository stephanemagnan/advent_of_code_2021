import numpy as np

incomplete_lines = []
with open("day10_input.txt") as f:
	total_score = 0
	for line in f:
		this_line = line.rstrip()
		#print(this_line)
		last_len = len(this_line)+1
		while len(this_line)<last_len:
			last_len = len(this_line)
			this_line = this_line.replace('()','')
			this_line = this_line.replace('[]','')
			this_line = this_line.replace('{}','')
			this_line = this_line.replace('<>','')
		print(this_line)
		
		line_score = 0
		index = -1
		this_search = this_line.find(')')
		if this_search>-1 and (this_search<index or index==-1):
			line_score = 3
			index = this_search
		this_search = this_line.find(']')
		if this_search>-1 and (this_search<index or index==-1):
			line_score = 57
			index = this_search
		this_search = this_line.find('}')
		if this_search>-1 and (this_search<index or index==-1):
			line_score = 1197
			index = this_search
		this_search = this_line.find('>')
		if this_search>-1 and (this_search<index or index==-1):
			line_score = 25137
			index = this_search
		total_score+=line_score
		if line_score !=0:
			print(line_score)
		else:
			incomplete_lines.append(this_line)	
		
print("answer part 1: ")
print(total_score)
print(" ")



incomplete_scores = np.zeros(len(incomplete_lines))
for row_ind,incomplete_row in enumerate(incomplete_lines):
	print(incomplete_row)
	for this_char in incomplete_row[::-1]:
		if this_char == '(':
			incomplete_scores[row_ind] = 5*incomplete_scores[row_ind] + 1
		elif this_char == '[':
			incomplete_scores[row_ind] = 5*incomplete_scores[row_ind] + 2
		elif this_char == '{':
			incomplete_scores[row_ind] = 5*incomplete_scores[row_ind] + 3
		elif this_char == '<':
			incomplete_scores[row_ind] = 5*incomplete_scores[row_ind] + 4
		
sorted_scores = sorted(incomplete_scores)
print(sorted_scores)
print((len(sorted_scores)-1)/2)
median_score = sorted_scores[(len(sorted_scores)-1)/2]

print("answer part 2: ")
print(median_score)
print(" ")
