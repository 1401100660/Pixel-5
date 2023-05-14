import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the IP address and the port for the server
IP_ADDRESS = 'localhost'
PORT = 12345

# Bind the socket to the IP and port
s.bind((IP_ADDRESS, PORT))

# Listen for connections from clients
s.listen(1)

print("Server is ready and listening on {}:{}".format(IP_ADDRESS, PORT))

# Accept a connection from a client
client_socket, client_address = s.accept()

print("Client has connected from {}:{}".format(client_address[0], client_address[1]))

# Receive data from the client
data = client_socket.recv(1024)

print("Received '{}' from client".format(data.decode()))

# Send a message to the client
client_socket.send(b'Hello, Client!')

# Close the connection with the client
client_socket.close()

# Close the server socket
s.close()

print("Server has closed the connection")

