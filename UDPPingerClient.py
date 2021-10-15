from socket import *
import timeit
import statistics

# Create a client UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Server details
serverIP = gethostname()
serverPort = 8080

loop = 10
rtts = []
lost = 0

# Send 10 pings to server
for i in range(0, loop):

    # Ping message to be sent
    message = "Ping " + str(i+1)

    # Start time to calculate RTT
    start = timeit.default_timer()
    print(start)
   
    # Send the message
    clientSocket.sendto(message.encode(), (serverIP, serverPort))

    try:
        print ("Packet",i+1)
        # Set timeout for any response from the Ping server
        clientSocket.settimeout(1)
        response = clientSocket.recv(128).decode() #kpn msg dtg

        # End time to calculate RTT
        end = timeit.default_timer()
        print(end)
        rtt = end - start
        rtts.append(rtt)

        # Remove timeout
        print ("Calculated Round Trip Time = " + str(round(rtt*1000, 3))+ " ms")
        clientSocket.settimeout(None)

    except timeout:
        # Packet has been lost
        lost += 1
        print ("Request timed out")

# Print report
print ("\n")
print ("Maximum RTT   = " + str(round(max(rtts)*1000, 3))+" ms")
print ("Minimum RTT   = " + str(round(min(rtts)*1000, 3))+" ms")
print ("Mean RTT      = " + str(round(statistics.mean(rtts)*1000, 3))+" ms")
print ("StDeviasi RTT = " + str(round(statistics.stdev(rtts)*1000, 3))+" ms")
