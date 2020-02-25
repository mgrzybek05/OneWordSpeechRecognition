import os
import time
import socket
import sys
from datetime import datetime

sys.path.insert(0, "../classification")
from classifier import classify_sound

address_list = [
    '10.11.155.159',
]

def send_to_server(results):
	exit_client = False
	while exit_client == False:	
		connected = False
		while connected == False:
			try:
				print("Connecting to server")
				client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				client.connect(("10.11.238.30", 32500))
				connected = True
			except Exception as e:
				time.sleep(1)
				connected = False
		
		while sound_data:
			data = sound_data[:2048]
			if not data:
				break
			try:
				sent = client.send(data)
				sound_data = sound_data[sent:]
			except Exception as e:
				time.sleep(1)  
				break
		time.sleep(1)	
		from_server = client.recv(1024)

def get_sound_data():
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind(("10.16.9.113", 32500))
	server.listen(5)

	id_counter = 0
	it_counter = 0
	results = [ 0, 0, 0 ]
	while True:
		connection, address = server.accept()
		print(address)
		if address[0] != address_list[id_counter]:
			connection.close()
			print("Skip")
		else:
			start = datetime.now().timestamp()
			file_name = "sound_from_client.wav"
			size_count = 0
			with open(file_name, "wb") as f:
				while True:
					recieve = connection.recv(2048)
					size_count += len(recieve)
					if not recieve or recieve == "" or size_count > 3140000:
						f.write(recieve)
						break
					f.write(recieve)
					end = datetime.now().timestamp()
					result[id_counter] = classify_sound('RPM.h5','sound_from_client.wav')
					connection.send("Done".encode('utf-8'))
					connection.close()
					print("Done")

					id_counter+=1
					if id_counter >= len(address_list):
						id_counter = 0
					it_counter+=1
					print("{} {}".format(it_counter, id_counter))
				return max(set(results), key=results.count)
	
if __name__ == "__main__":	
	value = get_sound_data()
	print(value)
	#send_to_server(value)
