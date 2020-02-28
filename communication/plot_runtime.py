import matplotlib.pyplot as plt
from numpy import mean

if __name__ == "__main__":
	fog_run = open("runtime-fog.txt", "r")

	value1 = 0
	value2 = 0	
	subtract = 0
	fog_times = []
	for line in fog_run.readlines():
		split_text = line.split(" ")
		if split_text[0] == "Start":
			value1 = float(split_text[1])
		else:
			value2 = float(split_text[1])
			subtract = 1
		
		if subtract == 1:
			fog_times.append(value2 - value1)
			subtract = 0

	non_run = open("runtime-non.txt", "r")

	value1 = 0
	value2 = 0	
	subtract = 0
	non_times = []
	for line in non_run.readlines():
		split_text = line.split(" ")
		if split_text[0] == "Start":
			value1 = float(split_text[1])
		else:
			value2 = float(split_text[1])
			subtract = 1
		
		if subtract == 1:
			non_times.append(value2 - value1)
			subtract = 0

	plt.plot(fog_times[5:25], '-o', label="Fog Setup")
	plt.plot(non_times[5:25], '-o', label="Cloud Setup")
	plt.legend(loc='best')
	plt.xlabel('Number of Iterations')
	plt.ylabel('Runtime (s)')
	plt.savefig("runtime.png")

	print("Fog: " + str(mean(fog_times[5:25])))
	print("Cloud: " + str(mean(non_times[5:25])))
