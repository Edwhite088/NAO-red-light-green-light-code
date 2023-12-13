#----------------------------------------------------------------------------------#
# Communication NAO robot red light green light game
# Version 1.0       Start writing the code tried with just sending files 20/11/2023
# Version 1.1        Get to work in choregraphe but not on the NAO 21/11/2023
# Version 2         Start all over but this time using socket for ip communication 24/11/2023
# Version 2.1       Had complications with getting it to work with the NAO but hopeful 26/11/2023
# Version 2.2       Changed the IP address to the right one using IPCONFIG in command window and using the wired connection rather than trying to use wireless 11/12/2023
# Version 2.3       Current and working flawlessly


# Edward White
#----------------------------------------------------------------------------------#

# Import all the required add-ons
import socket
import time
# creates a counter called x to be used later on
x = 0

# Define the server (computer) details
host = '0.0.0.0'
port = 8888

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(1)


print("Waiting for incoming connection...")
# Sets the code to go forever
while True:
    # Accept a connection
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address} has been established.")
    # Gets a number from the nao which has been random generated in the choregraphe code
    timer = client_socket.recv(1024).decode()
    # Debugging to see if the timer value was what we were expecting from the choregraphe script
    #print(timer)
    # Opens file that the motion detection uses to turn on and off the live feed
    with open('C:\\Users\\Edward\\PycharmProjects\\testwithopencv2\\red.txt', "w") as file:
        # Writes to the file what the nao sends across (should be a one at this point)
        file.write(client_socket.recv(1024).decode())
    # Opens the file that the motion detection sends its output variables to
    with open('C:\\Users\\Edward\\PycharmProjects\\testwithopencv2\\move.txt', "r") as file1:
        read1 = file1.read()
    # Checks if the random number has been counted too yet
    while int(timer) != x:
        # Repeat opening the file to check if the output has changed
        with open('C:\\Users\\Edward\\PycharmProjects\\testwithopencv2\\move.txt', "r") as file2:
            read2 = file2.read()
        # If the file hasn't changed increment x by 0.5 and delay the code for 0.5 seconds
        if read1 == read2:
            # Debugging
            #print(0)
            x = x + 0.5
            time.sleep(0.5)
        # If the file has changed its value
        else:
            # Sets the value that will be sent across to 1 just as a contingency
            read1 = 1
            # Debugging
            #print(1)
            break
    # Sends the output to the nao (either a 1 or 0 for simplicity)
    client_socket.sendall(str(read1).encode())
    # Tells the motion script to turn live feed off
    with open('C:\\Users\\Edward\\PycharmProjects\\testwithopencv2\\red.txt', "w") as file:
        file.write(client_socket.recv(1024).decode())
    # Reset the timer variable for the next connection
    x = 0
