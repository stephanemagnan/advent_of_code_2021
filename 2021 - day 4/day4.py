import numpy as np

game_count = 3
game_count = 100
bingo_cards = np.zeros((game_count,5,5),int)
bingo_solved = np.zeros((game_count,5,5),int)
with open("day4_input.txt") as f:
	first_line = f.readline().rstrip()
	call_order = first_line.split(',')
	
	for game in range(0,game_count):
		f.readline()
		for bingo_row in range(0,5):
			print(bingo_row)
			this_row = f.readline().rstrip()	
			#print(this_row)
			this_row = this_row.replace('  ',' ')	
			#print(this_row)
			if this_row[0] == ' ':
				this_row = this_row[1:]
			row_nums = this_row.split(' ')	
			print(row_nums)
			for this_num_ind,this_num in enumerate(row_nums):
				print(bingo_row,this_num_ind,game,this_num)
				bingo_cards[game,bingo_row,this_num_ind] = int(this_num) 
				for call_ind,this_call in enumerate(call_order):
					
					if this_num == this_call:
						print(this_call,this_num,call_ind)
						bingo_solved[game,bingo_row,this_num_ind] = call_ind+1
						break
						
print(bingo_cards)
print(bingo_solved)


best_game_id = -1
best_call_count = max(bingo_solved[0,:,0])

for game in range(0,game_count):
	for search_rc in range(0,5):
		if max(bingo_solved[game,search_rc,:])<best_call_count:
			best_game_id = game
			best_call_count = max(bingo_solved[game,search_rc,:])
		if max(bingo_solved[game,:,search_rc])<best_call_count:
			best_game_id = game
			best_call_count = max(bingo_solved[game,:,search_rc])

print(best_game_id,best_call_count)

bingo_score = 0
for search_r in range(0,5):
	for search_c in range(0,5):
		if bingo_solved[best_game_id,search_r,search_c]>best_call_count:
			bingo_score+=bingo_cards[best_game_id,search_r,search_c]

last_call = int(call_order[best_call_count-1])

a1 = last_call*bingo_score
print(last_call)
print(bingo_score)

print("answer part 1: ")
print(a1)
print(" ")


best_game_id = -1
best_call_count = 0

for game in range(0,game_count):
	this_call_count = 1000
	for search_rc in range(0,5):
		if max(bingo_solved[game,search_rc,:])<this_call_count:
			this_call_count = max(bingo_solved[game,search_rc,:])
		if max(bingo_solved[game,:,search_rc])<this_call_count:
			this_call_count = max(bingo_solved[game,:,search_rc])

	if this_call_count>best_call_count:
		best_call_count = this_call_count
		best_game_id = game

print(best_game_id,best_call_count)

bingo_score = 0
for search_r in range(0,5):
	for search_c in range(0,5):
		if bingo_solved[best_game_id,search_r,search_c]>best_call_count:
			bingo_score+=bingo_cards[best_game_id,search_r,search_c]

last_call = int(call_order[best_call_count-1])

a2 = last_call*bingo_score
print(last_call)
print(bingo_score)

print("answer part 2: ")
print(a2)
print(" ")
