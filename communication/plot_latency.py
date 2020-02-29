import matplotlib.pyplot as plt
from numpy import mean

if __name__ == "__main__":
	non_1_files = ["non_lat_1a.txt", "non_lat_1b.txt", "non_lat_1c.txt"]

	non1_latencies = []
	for lat_filename in non_1_files:
		lat_file = open(lat_filename, "r")

		value1 = 0
		value2 = 0	
		subtract = 0
		temp_latencies = []
		for line in lat_file.readlines():
			line = line.strip("\n")
			split_text = line.split(" ")
			if split_text[0] == "Start":
				value1 = float(split_text[2])
			else:
				value2 = float(split_text[2])
				subtract = 1
		
			if subtract == 1:
				temp_latencies.append(value2 - value1)
				subtract = 0
		temp_latencies = temp_latencies[-60:]
		temp_latencies = temp_latencies[10:39]
		non1_latencies = non1_latencies + temp_latencies

		

	non_2_files = ["non_lat_2a.txt", "non_lat_2b.txt", "non_lat_2c.txt", "non_lat_2d.txt", "non_lat_2e.txt", "non_lat_2f.txt"]

	non2_latencies = []
	for lat_filename in non_2_files:
		lat_file = open(lat_filename, "r")

		value1 = 0
		value2 = 0	
		subtract = 0
		temp_latencies = []
		for line in lat_file.readlines():
			line = line.strip("\n")
			split_text = line.split(" ")
			if split_text[0] == "Start":
				value1 = float(split_text[2])
			else:
				value2 = float(split_text[2])
				subtract = 1
		
			if subtract == 1:
				temp_latencies.append(value2 - value1)
				subtract = 0
		temp_latencies = temp_latencies[-60:]
		temp_latencies = temp_latencies[10:39]
		non2_latencies = non2_latencies + temp_latencies
	
		

	non_3_files = ["non_lat_3a.txt", "non_lat_3b.txt", "non_lat_3c.txt", "non_lat_3e.txt", "non_lat_3f.txt", "non_lat_3g.txt", "non_lat_3h.txt", "non_lat_3i.txt"]

	non3_latencies = []
	for lat_filename in non_3_files:
		lat_file = open(lat_filename, "r")

		value1 = 0
		value2 = 0	
		subtract = 0
		temp_latencies = []
		for line in lat_file.readlines():
			line = line.strip("\n")
			split_text = line.split(" ")
			if split_text[0] == "Start":
				value1 = float(split_text[2])
			else:
				value2 = float(split_text[2])
				subtract = 1
		
			if subtract == 1:
				if value2-value1 > 0.0005:
					temp_latencies.append(value2 - value1)
				subtract = 0	
		temp_latencies = temp_latencies[-60:]
		temp_latencies = temp_latencies[10:39]
		non3_latencies = non3_latencies + temp_latencies

	fog_1_files = ["fog_lat_1a.txt"]

	fog1_latencies = []
	for lat_filename in fog_1_files:
		lat_file = open(lat_filename, "r")

		value1 = 0
		value2 = 0	
		subtract = 0
		temp_latencies = []
		for line in lat_file.readlines():
			line = line.strip("\n")						
			if line != "":
				split_text = line.split(" ")
				if split_text[0] == "Start":
					value1 = float(split_text[2])
				else:
					value2 = float(split_text[2])
					subtract = 1
	
				if subtract == 1:
					temp_latencies.append(value2 - value1)
					subtract = 0
		temp_latencies = temp_latencies[-60:]
		temp_latencies = temp_latencies[10:39]
		fog1_latencies = fog1_latencies + temp_latencies

	fog_2_files = ["fog_lat_2a.txt", "fog_lat_2b.txt"]

	fog2_latencies = []
	for lat_filename in fog_2_files:
		lat_file = open(lat_filename, "r")

		value1 = 0
		value2 = 0	
		subtract = 0
		temp_latencies = []
		for line in lat_file.readlines():
			line = line.strip("\n")
			split_text = line.split(" ")
			if split_text[0] == "Start":
				value1 = float(split_text[2])
			else:
				value2 = float(split_text[2])
				subtract = 1
		
			if subtract == 1:
				temp_latencies.append(value2 - value1)
				subtract = 0
		temp_latencies = temp_latencies[-60:]
		temp_latencies = temp_latencies[10:39]
		fog2_latencies = fog2_latencies + temp_latencies

	fog_3_files = ["fog_lat_3a.txt", "fog_lat_3b.txt", "fog_lat_3c.txt"]

	fog3_latencies = []
	for lat_filename in fog_3_files:
		lat_file = open(lat_filename, "r")

		value1 = 0
		value2 = 0	
		subtract = 0
		temp_latencies = []
		for line in lat_file.readlines():
			line = line.strip("\n")
			split_text = line.split(" ")
			if split_text[0] == "Start":
				value1 = float(split_text[2])
			else:
				value2 = float(split_text[2])
				subtract = 1
		
			if subtract == 1:
				temp_latencies.append(value2 - value1)
				subtract = 0
		temp_latencies = temp_latencies[-60:]
		temp_latencies = temp_latencies[10:39]
		fog3_latencies = fog3_latencies + temp_latencies

	print(mean(non1_latencies))
	print(mean(non2_latencies))	
	print(mean(non3_latencies))
	print(mean(fog1_latencies))	
	print(mean(fog2_latencies))	
	print(mean(fog3_latencies))	
