import numpy as np

line_map = np.zeros((1000,1000))
#line_map = np.zeros((10,10))

f=open("day5_input.txt","r")
for line in f.readlines():
	line2 = line.replace('->',',')
	line3 = line2.replace('\n','')
	line4 = line3.replace(' ','')
	splits = line4.split(',')
	#print(splits)
	if splits[0] == splits[2] or splits[1] == splits[3]:
		
		x1 = min(int(splits[0]),int(splits[2]))
		x2 = max(int(splits[0]),int(splits[2]))
		y1 = min(int(splits[1]),int(splits[3]))
		y2 = max(int(splits[1]),int(splits[3]))
		
		#print(x1,x2,y1,y2)
		
		line_map[y1:y2+1,x1:x2+1]+=1

f.close()

#print(line_map)

count = np.count_nonzero(line_map>=2)
print("answer part 1: ")
print(count)


line_map = np.zeros((1000,1000))
#line_map = np.zeros((10,10))

f=open("day5_input.txt","r")
for line in f.readlines():
	line2 = line.replace('->',',')
	line3 = line2.replace('\n','')
	line4 = line3.replace(' ','')
	splits = line4.split(',')
	

	
	if splits[0] == splits[2] or splits[1] == splits[3]:
		x1 = min(int(splits[0]),int(splits[2]))
		x2 = max(int(splits[0]),int(splits[2]))
		y1 = min(int(splits[1]),int(splits[3]))
		y2 = max(int(splits[1]),int(splits[3]))
		
		print(x1,x2,y1,y2)
		line_map[y1:y2+1,x1:x2+1]+=1
	else:#diagonal line
		x1 = int(splits[0])
		x2 = int(splits[2])
		y1 = int(splits[1])
		y2 = int(splits[3])
		
		if x1>x2:
			xs = range(x1,x2-1,-1)
		else:
			xs = range(x1,x2+1,1)
		
		if y1>y2:
			ys = range(y1,y2-1,-1)
		else:
			ys = range(y1,y2+1,1)				
		

		print(xs,ys)
		for i in range(0,len(xs)):
			
			print(ys[i],xs[i])
			line_map[ys[i],xs[i]]+=1
		

f.close()

print(line_map)

count = np.count_nonzero(line_map>=2)
print("answer part 2: ")
print(count)
