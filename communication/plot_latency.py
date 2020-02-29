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

	avg_non1 = mean(non1_latencies)*1000
	avg_non2 = mean(non2_latencies)*1000
	avg_non3 = mean(non3_latencies)*1000
	avg_fog1 = mean(fog1_latencies)*1000
	avg_fog2 = mean(fog2_latencies)*1000
	avg_fog3 = mean(fog3_latencies)*1000

	print(mean(non1_latencies))
	print(mean(non2_latencies))	
	print(mean(non3_latencies))
	print(mean(fog1_latencies))	
	print(mean(fog2_latencies))	
	print(mean(fog3_latencies))	

	values = [avg_non1, avg_non2, avg_non3, avg_fog1, avg_fog2, avg_fog3]
	plt.grid(b=True, which='major', color='gray', linestyle=':')
	plt.bar([0.875,1.875,2.875], [avg_non1, avg_non2, avg_non3], width=0.25, label="Cloud Setup", align="center", color="green")
	plt.bar([1.125,2.125,3.125], [avg_fog1, avg_fog2, avg_fog3], width=0.25, label="Fog Setup", align="center", color="red")
	
	plt.text(0.75, 16, str(15.91), color='black', fontweight='bold', ha='left', va='baseline')
	plt.text(1.75, 15.7, str(15.66), color='black', fontweight='bold', ha='left', va='baseline')
	plt.text(2.75, 20.1, str(20.02), color='black', fontweight='bold', ha='left', va='baseline')	

	plt.text(1.025, 0.16, str(0.15), color='black', fontweight='bold', ha='left', va='baseline')
	plt.text(2.025, 0.16, str(0.15), color='black', fontweight='bold', ha='left', va='baseline')
	plt.text(3.025, 0.24, str(0.16), color='black', fontweight='bold', ha='left', va='baseline')	
	plt.legend(loc='best')
	plt.xlabel('Number of Rooms')
	plt.ylabel('Latency (ms)')
	plt.xticks([1,2,3])
	plt.savefig("latency.png")
