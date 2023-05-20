
import socket
import sys
import time

def socket_tcp_web(MSG,IP_ADDRESS="localhost",PORT=2345):
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to the IP and port
    s.bind((IP_ADDRESS, PORT))
    # Listen for connections from clients
    s.listen(5)
    print("Server is ready and listening on {}:{}".format(IP_ADDRESS, PORT))
    # Accept a connection from a client
    client_sock, client_addr = s.accept()
    print("Client has connected from {}:{}".format(client_addr[0], client_addr[1]))
    # Receive up to 1024 bytes of data from the client
    request_data = client_sock.recv(1024).decode('utf-8')
    # Split the request data into lines and take the first line (request line)
    request_line = request_data.splitlines()[0]
    # Extract the HTTP method, path, and version from the request line
    method, path, version = request_line.split(' ')
    print(method, path, version)
    # Prepare the HTTP response headers and body
    response_headers = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\n"
    response_body = MSG
    # Send the response headers and body to the client
    client_sock.send(response_headers.encode('utf-8'))
    client_sock.send(response_body.encode('utf-8'))
    # Close the connection with the client
    client_sock.close()
    # Close the server socket
    s.close()
    print("Server has closed the connection")

def socket_tcp_cmd(MSG, IP_ADDRESS="localhost", PORT=12345):
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
    # Parse the message that will be sent to the client into a byte string
    message = MSG.encode("utf-8")
    # Send a message to the client
    client_socket.send(message)
    # Close the connection with the client
    client_socket.close()
    # Close the server socket
    s.close()
    print("Server has closed the connection")

if __name__ == "__main__":
    socket_tcp_web(sys.argv[1])
    time.sleep(3)
    socket_tcp_cmd(sys.argv[1])
