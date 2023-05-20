import socket

class socket_client:
    def __init__(self, IP='localhost', PORT=8080):
        self.IP_ADDRESS=IP
        self.PORT=PORT
    
    def socket_tcp_client(self, TARGET_IP_ADDRESS='localhost', TARGET_PORT=8080):
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Define client ip and port
        s.bind((self.IP_ADDRESS, self.PORT))
        # Connect to the server
        s.connect((TARGET_IP_ADDRESS, TARGET_PORT))
        print("Connected to the server at {}:{}".format(TARGET_IP_ADDRESS, TARGET_PORT))
        # Send a message to the server
        s.send(b'Hello, Server!')
        # Receive data from the server
        data = s.recv(1024)
        print("Received '{}' from server".format(data.decode()))
        # Close the connection
        s.close()
        print("Client has closed the connection")

