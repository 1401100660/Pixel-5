import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the IP address and the port of the server
SERVER_IP_ADDRESS = 'localhost'
SERVER_PORT = 12345 

# Connect to the server
s.connect((SERVER_IP_ADDRESS, SERVER_PORT))

print("Connected to the server at {}:{}".format(SERVER_IP_ADDRESS, SERVER_PORT))

# Send a message to the server
s.send(b'Hello, Server!')

# Receive data from the server
data = s.recv(1024)

print("Received '{}' from server".format(data.decode()))

# Close the connection
s.close()

print("Client has closed the connection")

