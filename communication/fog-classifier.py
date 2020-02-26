import os
import time
import socket
import sys
from datetime import datetime

sys.path.insert(0, "../classification")
from classifier import classify_sound

address_list = [
    '10.11.155.159',
	'10.11.207.176',
	'10.11.216.196'
]

port = 32500

def send_to_server(results):
	connected = False
	while connected == False:
		try:
			print("Connecting to server")
			client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			client.connect(("10.11.238.30", 32500))
			sent = client.send(str(results).encode())
			time.sleep(1)	
			from_server = client.recv(1024)
			if from_server == b'Done':
				connected = True				
		except Exception as e:
			time.sleep(1)
			connected = False


def get_sound_data():
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)	
	server.bind(("10.16.9.113", 32500))
	server.listen(3)

	id_counter = 0
	results = [ 0, 0, 0 ]
	while True:

		connection, address = server.accept()
		print(address)
		if address[0] != address_list[id_counter]:
			connection.close()
			print("Skip")
		else:
			file_name = "sound_from_client.wav"
			size_count = 0
			with open(file_name, "wb") as f:
				while True:
					recieve = connection.recv(2048)
					size_count += len(recieve)
					if not recieve or recieve == "" or size_count >= 32044:
						f.write(recieve)
						break
					f.write(recieve)
			results[id_counter] = classify_sound('../classification/training_models/RPM.h5','sound_from_client.wav')
			connection.send("Done".encode('utf-8'))
			connection.close()

			id_counter+=1
			if id_counter >= len(address_list):
				break
			print("{}".format(id_counter))

		
		
	return max(set(results), key=results.count)

if __name__ == "__main__":
	time_file = open("runtime-fog.txt", "a+")
	start = datetime.now().timestamp()
	time_file.write("Start {}\n".format(start))
	value = get_sound_data()
	send_to_server(value)
	end = datetime.now().timestamp()
	time_file.write("End {}\n".format(end))
