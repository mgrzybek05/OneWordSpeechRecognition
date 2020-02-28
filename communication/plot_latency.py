import matplotlib.pyplot as plt
from numpy import mean

if __name__ == "__main__":
	fog_lat_1_file = open("latency_fog.txt", "r")
	
	value1 = 0
	value2 = 0	
	subtract = 0
	fog1_latencies = []
	for line in fog_lat_1_file.readlines():
		line = line.strip("\n")
		split_text = line.split(" ")
		if split_text[0] == "Start":
			value1 = float(split_text[2])
		else:
			value2 = float(split_text[2])
			subtract = 1
		
		if subtract == 1:
			fog1_latencies.append(value2 - value1)
			subtract = 0

	fog_lat_2_file = open("latency_fog2.txt", "r")
	
	value1 = 0
	value2 = 0	
	subtract = 0
	fog2_latencies = []
	for line in fog_lat_2_file.readlines():
		line = line.strip("\n")
		split_text = line.split(" ")
		if split_text[0] == "Start":
			value1 = float(split_text[2])
		else:
			value2 = float(split_text[2])
			subtract = 1
		
		if subtract == 1:
			fog2_latencies.append(value2 - value1)
			subtract = 0

	fog_lat_3_file = open("latency_fog3.txt", "r")
	
	value1 = 0
	value2 = 0	
	subtract = 0
	fog3_latencies = []
	for line in fog_lat_3_file.readlines():
		line = line.strip("\n")
		split_text = line.split(" ")
		if split_text[0] == "Start":
			value1 = float(split_text[2])
		else:
			value2 = float(split_text[2])
			subtract = 1
		
		if subtract == 1:
			fog3_latencies.append(value2 - value1)
			subtract = 0

	non_lat_1_file = open("latency_non.txt", "r")
	
	value1 = 0
	value2 = 0	
	subtract = 0
	non1_latencies = []
	for line in non_lat_1_file.readlines():
		line = line.strip("\n")
		split_text = line.split(" ")
		if split_text[0] == "Start":
			value1 = float(split_text[2])
		else:
			value2 = float(split_text[2])
			subtract = 1
		
		if subtract == 1:
			print(value2 - value1)
			non1_latencies.append(value2 - value1)
			subtract = 0
	
	non_lat_2_file = open("latency_non2.txt", "r")
	
	value1 = 0
	value2 = 0	
	subtract = 0
	non2_latencies = []
	for line in non_lat_2_file.readlines():
		line = line.strip("\n")
		split_text = line.split(" ")
		if split_text[0] == "Start":
			value1 = float(split_text[2])
		else:
			value2 = float(split_text[2])
			subtract = 1
		
		if subtract == 1:
			non2_latencies.append(value2 - value1)
			subtract = 0

	non_lat_3_file = open("latency_non3.txt", "r")
	
	value1 = 0
	value2 = 0	
	subtract = 0
	non3_latencies = []
	for line in non_lat_3_file.readlines():
		line = line.strip("\n")
		split_text = line.split(" ")
		if split_text[0] == "Start":
			value1 = float(split_text[2])
		else:
			value2 = float(split_text[2])
			subtract = 1
		
		if subtract == 1:
			non3_latencies.append(value2 - value1)
			subtract = 0

	print(mean(fog1_latencies))		
	print(mean(fog2_latencies))
	print(mean(fog3_latencies))
	print(mean(non1_latencies))	
	print(mean(non2_latencies))	
	print(mean(non3_latencies))	
