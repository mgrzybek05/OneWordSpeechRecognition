import socket
import os
import sys
import time
from datetime import datetime

sys.path.insert(0, "../classification")
from classifier import classify_sound

address_list = [
    '10.11.155.159',
    '10.11.201.222',
    '10.11.216.196',
    '10.11.186.106',
    '10.11.177.188',
    '10.11.249.2'
]

if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("10.11.239.102", 32500))
    server.listen(10)

    id_counter = 0
    time_file = open("latency_non2.txt", "a+")
    it_counter = 0
    while True:
        connection, address = server.accept()
        print(address)
        if address[0] != address_list[id_counter]:
            connection.close()
            print("Skip")
        else:
            start = datetime.now().timestamp()
            time_file.write("Start {} {}\n".format(address[0], start))
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
            end = datetime.now().timestamp()
            time_file.write("End {} {}\n".format(address[0], end))
            #classify_sound('../classification/training_models/RPM.h5', 'sound_from_client.wav')
            connection.send("Done".encode('utf-8'))
            connection.close()
            print("Done")
        
            id_counter+=1
            if id_counter >= len(address_list):
                id_counter = 0
            it_counter+=1

            if it_counter >= 60:
                break
            print("{} {}".format(it_counter, id_counter))
            
