# 5. Write a program using TCP socket to do the following jobs:

# a.Echo message (to be seen both on server and clients)
# b.Menu driven mathematical operation (ADD, SUBTRACT, MULTIPLY, DIVISION, MODULUS)
# c.Client will send “DAYTIME” to the server and the server will send back the corresponding date and time with a greetings like “Good Morning” or “Good Evening” depending on the time.

import socket

def tcp_client(host="localhost", port=5000):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((host, port))
        print(f"Connected to server at {host}:{port}")

        while True:
            
            # message = input("Enter message (or type 'exit' to quit): ").strip()
            # if message.lower() == "exit":
            #     break

            print("\nTCP Client Menu:")
            print("1. Send Normal Message")
            print("2. Perform Mathematical Operation")
            print("3. Get Current Date & Time")
            print("4. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                message = input("Enter message: ")
            elif choice == "2":
                try:
                    op = input("Enter operation (+, -, *, /): ")
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))
                    message = f"M {op} {num1} {num2}"
                except ValueError:
                    print("Invalid number input. Please enter valid numbers.")
                    continue
                except Exception as e:
                    print(f"Mathematical operation error: {e}")
                    continue
            elif choice == "3":
                message = "DAYTIME"
            elif choice == "4":
                print("Exiting Client...")
                break
            else:
                print("Invalid option! Try again.")
                continue

            client_socket.send(message.encode())
            response = client_socket.recv(1024).decode()
            print(f"Server Response: {response}")

    except Exception as e:
        print(f"Client error: {e}")

    finally:
        client_socket.close()
        print("Disconnected from server.")

if __name__ == "__main__":
    tcp_client()