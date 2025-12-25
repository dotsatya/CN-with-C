# 3.	Write a program to detect error using CRC technique. The message to transmit is M=110001101, divisor polynomial D=X4+X2+1. Your program output should show the transmitting bit-stream along with CRC, error detected if any and the received message. 

def xor_operation(a, b):
    """Performs XOR operation on two binary strings."""
    result = ""
    for i in range(1, len(b)):
        result += '0' if a[i] == b[i] else '1'
    return result

def mod2div(dividend, divisor):
    """Performs modulo-2 division on two binary strings."""
    pick = len(divisor)
    remainder = dividend[:pick]

    while pick < len(dividend):
        if remainder[0] == '1':
            remainder = xor_operation(remainder, divisor) + dividend[pick]
        else:
            remainder = xor_operation(remainder, '0' * len(divisor)) + dividend[pick]
        pick += 1

    if remainder[0] == '1':
        remainder = xor_operation(remainder, divisor)
    else:
        remainder = remainder[1:]

    return remainder

def main():
    """Main function to perform CRC encoding and decoding."""
    message = input("Enter the message : ")
    divisor = input("Enter the divisor : ")

    appended_message = message + '0' * (len(divisor) - 1)
    remainder = mod2div(appended_message, divisor)
    print(f"Remainder: {remainder}")

    transmitted_message = message + remainder
    print(f"Transmitting Data: {transmitted_message}")

    received_data = input("Enter the received data (binary): ")
    checking_value = mod2div(received_data, divisor)
    print(f"Checking Value: {checking_value}")

    if checking_value == '0' * (len(divisor) - 1):
        print("Error Check: No Error")
    else:
        print("Error Check: Error Detected")

if __name__ == "__main__":
    main()