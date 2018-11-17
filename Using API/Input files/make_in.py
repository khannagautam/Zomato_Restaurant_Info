ctr = 0
ind = 1
filename = "in"
file = "in1.txt"
with open ('restaurants.csv', "r") as myfile:
	for line in myfile.readlines():
		ctr += 1
		if(ctr%900 == 0):
			ind += 1
			file = filename+str(ind)+".txt"
		with open(file,"a") as f:
			f.write(line)	
