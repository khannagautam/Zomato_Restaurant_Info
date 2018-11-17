ctr = 0
ind = 1
filename = "cuisines"
for ind in range(1,5):
	part_file = filename+str(ind)+".csv"
	with open (part_file, "r") as myfile:
		for line in myfile.readlines():
			with open("cuisines.csv","a") as f:
				f.write(line)	

