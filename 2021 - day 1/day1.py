import numpy as np

data = np.loadtxt("day1_input.txt")

increase_count = sum(np.greater(data[1:], data[0:-1]))
print("answer part 1: ")
print(increase_count)


smoothed_data = data[0:-2]+data[1:-1]+data[2:]
increase_count_2 = sum(np.greater(smoothed_data[1:], smoothed_data[0:-1]))
print("answer part 2: ")
print(increase_count_2)



