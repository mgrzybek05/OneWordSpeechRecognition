
if __name__ == "__main__":
	runtime_file = open("communication/runtime-fog.txt", "r")
	
	value1 = 0
	value2 = 0	
	subtract = 0
	for line in runtime_file.readlines():
		split_text = line.split(" ")
		if split_text[0] == "Start":
			value1 = float(split_text[1])
		else:
			value2 = float(split_text[1])
			subtract = 1
		
		if subtract == 1:
			print(value2 - value1)
			subtract = 0
