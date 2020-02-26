import os
import time
import socket
import sys
from datetime import datetime

def send_to_server(results):
	connected = False
	while connected == False:
		try:
			print("Connecting to server")
			client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			client.connect(("10.11.239.102", 32500))
			sent = client.send(str(results).encode())
			time.sleep(1)	
			from_server = client.recv(1024)
			if from_server == b'Done':
				connected = True				
		except Exception as e:
			time.sleep(1)
			connected = False

if __name__ == "__main__":
	value = 1
	send_to_server(value)
	
