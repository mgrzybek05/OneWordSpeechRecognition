import os
import time
import socket
import sys
from datetime import datetime

def send_to_server(results):
	connected = False
	latency_name = "fog_lat_3a.txt"
	ip_address = "10.11.155.159"
	
	latency_file = open(latency_name, "a+")
	while connected == False:
		try:
			time.sleep(2)
			print("Connecting to server")
			client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			client.connect(("10.11.232.95", 32500))
			start = datetime.now().timestamp()
			sent = client.send(str(results).encode())
			end = datetime.now().timestamp()
			connected = True
			latency_file.write("Start {} {}\n".format(ip_address, start))
			latency_file.write("End {} {}\n".format(ip_address, end))				
		except Exception as e:
			print(e)
			time.sleep(1)
			connected = False

if __name__ == "__main__":
	for i in range(60):
		value = 1
		send_to_server(value)
		print(i)	
