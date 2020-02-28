import matplotlib.pyplot as plt

if __name__ == "__main__":
	fog_lat_1_file = open("latency_fog.txt", "r")
	
	latencies = {}
	for line in fog_lat_1_file.readlines():
		print(line)
