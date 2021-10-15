# UDPPingerServer.py
# We will need the following modules to generate randomized lost packets import random
from socket import *
import random

print ("\nConnected to: " + gethostbyname(gethostname()))
# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind((gethostname(), 8080))

while True:
    # Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(1024)
    print("received", message.decode(), address)

    # Otherwise, the server responds
    serverSocket.sendto(message, address)
    print("sent", message.decode(), address)
