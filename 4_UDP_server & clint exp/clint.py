# 4.	Write a program using UDP socket to do the following jobs:
# a.	Echo message
# b.	Menu driven mathematical operation.
# c.	Client will send “DAYTIME” to the server and the server will send back the corresponding date and time with a greetings like “Good Morning” or “Good Evening” depending on the time. 

import socket

def udp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ("localhost", 8080)
    
    while True:
        print("\nUDP Client Menu:")
        print("1. Send Normal Message")
        print("2. Perform Mathematical Operation")
        print("3. Get Current Date & Time")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            message = input("Enter message: ")
        elif choice == "2":
            op = input("Enter operation (+, -, *, /): ")
            num1 = input("Enter first number: ")
            num2 = input("Enter second number: ")
            message = f"M {op} {num1} {num2}"
        elif choice == "3":
            message = "DAYTIME"
        elif choice == "4":
            print("Exiting Client...")
            break
        else:
            print("Invalid option! Try again.")
            continue
        
        client_socket.sendto(message.encode('utf-8'), server_address)
        response, _ = client_socket.recvfrom(1024)
        print("Server Response:", response.decode('utf-8'))
    
    client_socket.close()

if __name__ == "__main__":
    udp_client()
