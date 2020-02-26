import socket
import os
import time
from datetime import datetime

address_list = [
    '10.11.155.159',
    '10.11.201.222',
    '10.11.216.196'
]

if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("10.11.239.102", 32500))
    server.listen(10)

    id_counter = 0
    time_file = open("latency_fog3.txt", "a+")
    it_counter = 0
    while True:
        connection, address = server.accept()
        start = datetime.now().timestamp()
        print(address)
        if address[0] != address_list[id_counter]:
            connection.close()
            print("Skip")
        else:
            time_file.write("Start {} {}\n".format(address[0], start))
            recieve = connection.recv(1024)
            end = datetime.now().timestamp()
            time_file.write("End {} {}\n".format(address[0], end))
            connection.send("Done".encode('utf-8'))
            connection.close()
            print("Done")

            id_counter+=1
            if id_counter >= len(address_list):
                id_counter = 0
            it_counter+=1
            print("{} {}".format(it_counter, id_counter))
            
