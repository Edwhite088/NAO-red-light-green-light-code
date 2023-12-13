#----------------------------------------------------------------------------------#
# NAO and server connection
# Version 1.0       Start writing the files using basic file command 21/11/2023
# Version 1.1       Realise that the code only works on software and not on the nao
# Version 2.0       Get socket to work and connect to the local machine 24/11/2023
# Version 2.1       Finally got NAO to connect to the server 11/12/2023

# Edward White

# Additional notes    The IP for the computer will change as have not set up a static
# IP address, It only works if following critera are met:
#    NAO is connected to the computer using ethernet and the lan IP address from
#    IPCONFIG is used.

#    The private IP address for the computer is used and not the public one
#----------------------------------------------------------------------------------#

#Import the required add-ons
import socket
import random
import time


class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)

    def onLoad(self):
        #put initialization code here
        pass

    def onUnload(self):
        #put clean-up code here
        pass

    def onInput_onStart(self):
        # Creates a random number to use as a time
        rand = random.randint(2,6)
        # Define the server (NAO robot) details
        # Computer's private IP address
        host = '169.254.13.207'
        # Port the server is listening on
        port = 8888

        # Create a socket object
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the server
        client_socket.connect((host, port))
        # Sends the random value to server
        client_socket.sendall(str(rand).encode())
        # Delays so the server can keep up
        time.sleep(0.001)
        # Sends a 1 to the server
        client_socket.sendall("1".encode())
        # Gets the infomation back from the server
        num = client_socket.recv(1024).decode()
        client_socket.sendall("0".encode())
        # Outputs the number that the NAO just got from the server
        self.onStopped(str(num)) #activate the output of the box
        pass

    def onInput_onStop(self):
        self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
        self.onStopped() #activate the output of the box
