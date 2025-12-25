# 5. Write a program using TCP socket to do the following jobs:

# a.Echo message (to be seen both on server and clients)
# b.Menu driven mathematical operation (ADD, SUBTRACT, MULTIPLY, DIVISION, MODULUS)
# c.Client will send “DAYTIME” to the server and the server will send back the corresponding date and time with a greetings like “Good Morning” or “Good Evening” depending on the time.


import socket
import datetime
import threading

def handle_client(client_socket, client_address):
    print(f"Connected to {client_address}")
    try:
        while True:
            data = client_socket.recv(1024).decode().strip()
            if not data:
                break

            print(f"Received from {client_address}: {data}")

            if data.upper() == "DAYTIME":
                now = datetime.datetime.now()
                time = now.strftime("%Y-%m-%d %H:%M:%S")
                hour = now.hour
                greeting = "Good Morning" if 6 <= hour < 12 else "Good Evening" if hour >= 18 else "Good Afternoon"
                response = f"{greeting}, {time}"

            elif data.startswith("M"): #Updated to match the client format.
                parts = data.split()
                if len(parts) == 4:
                    try:
                        op = parts[1]
                        num1 = float(parts[2])
                        num2 = float(parts[3])

                        if op == '+': result = num1 + num2
                        elif op == '-': result = num1 - num2
                        elif op == '*': result = num1 * num2
                        elif op == '/': result = num1 / num2
                        else: result = "Invalid operator"

                        response = str(result)
                    except ValueError:
                        response = "Invalid number format"
                    except ZeroDivisionError:
                        response = "Division by zero"
                    except Exception as e:
                        response = f"Server error: {e}"
                else:
                    response = "Invalid message format"

            else:
                response = data  # Echo the message back

            client_socket.send(response.encode())

    except Exception as e:
        print(f"Error: {e}")

    finally:
        print(f"Connection closed: {client_address}")
        client_socket.close()

def tcp_server(host="localhost", port=5000):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_thread.start() #Start a new thread for each client.

    except KeyboardInterrupt:
        print("\nServer shutting down.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    tcp_server()