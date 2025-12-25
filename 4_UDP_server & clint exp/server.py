# 4.	Write a program using UDP socket to do the following jobs:
# a.	Echo message
# b.	Menu driven mathematical operation.
# c.	Client will send “DAYTIME” to the server and the server will send back the corresponding date and time with a greetings like “Good Morning” or “Good Evening” depending on the time. 

import socket
import datetime

def handle_request(message, client_address):
    message = message.strip()
    
    if message.upper() == "DAYTIME":
        current_hour = datetime.datetime.now().hour
        if current_hour < 12:
            greeting = "Good Morning"
        elif current_hour < 18:
            greeting = "Good Afternoon"
        else:
            greeting = "Good Evening"
        return f"{greeting} - {datetime.datetime.now()}"
    
    elif message.startswith("M"):
        parts = message.split()
        if len(parts) == 4:
            try:
                operation = parts[1]
                num1 = int(parts[2])
                num2 = int(parts[3])
                
                if operation == '+':
                    return f"Result: {num1 + num2}"
                elif operation == '-':
                    return f"Result: {num1 - num2}"
                elif operation == '*':
                    return f"Result: {num1 * num2}"
                elif operation == '/':
                    return f"Result: {num1 / num2}" if num2 != 0 else "Error: Division by zero"
                else:
                    return "Invalid operation!"
            except ValueError:
                return "Invalid numbers in the operation!"
        else:
            return "Invalid format for mathematical operation!"
    
    else:
        return f"Echo: {message}"

def start_udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(("0.0.0.0", 8080))
    print("UDP Server is running on port 8080...")
    
    while True:
        data, client_address = server_socket.recvfrom(1024)
        message = data.decode('utf-8')
        print(f"Received from {client_address[0]}:{client_address[1]} → {message}")
        
        response = handle_request(message, client_address)
        server_socket.sendto(response.encode('utf-8'), client_address)

if __name__ == "__main__":
    start_udp_server()
