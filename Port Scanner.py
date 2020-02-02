from socket import socket
from datetime import datetime

target = input("Enter target hostname or ip to scan: ")
min_port = input("Enter lower port range (default: 1): ")
max_port = input("Enter upper port range (default: 65535): ")
timeout = input("Enter maximum time to scan each port (default: 3.5): ")

if min_port == '':
    min_port = 1
else:
    min_port = int(min_port)

if max_port == '':
    max_port = 65535
else:
    max_port = int(max_port)

if timeout == '':
    timeout = 3.5
else:
    timeout = int(timeout)

start_time = datetime.now()

for port in range(min_port, max_port + 1):
    sock = socket()
    sock.settimeout(timeout)

    if sock.connect_ex((target, port)) == 0:
        print('Port', port, ': Open')

    sock.close()

stop_time = datetime.now()
print("Time taken:", stop_time - start_time)
