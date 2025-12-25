# 2.	Write a program to demonstrate bit-stuffing technique. Assume the flag pattern is 111110. Your program should stuff bits accordingly and de-stuff the stuffed bit string. The system will identify the position(s) of bit-stuffing, stuff bit(s) autonomously. User will input data and flag only. The program will de-stuff the bit(s) when user instruct to the program. 

def bit_stuffing(data, flag):
    """Performs bit stuffing on the given data."""
    flag_size = len(flag)
    max_consecutive_ones = max(len(run) for run in ''.join(flag).split('0')) if '1' in flag else 0

    if max_consecutive_ones <= 1:
        raise ValueError("Flag must contain at least 2 consecutive 1s.")

    stuff_threshold = max_consecutive_ones - 1
    consecutive_ones = 0
    stuffed_data = list(data)  

    i = 0
    while i < len(stuffed_data):
        if stuffed_data[i] == '1':
            consecutive_ones += 1
            if consecutive_ones == stuff_threshold:
                stuffed_data.insert(i + 1, '0')
                consecutive_ones = 0
                i += 1  
        else:
            consecutive_ones = 0
        i += 1

    return "".join(stuffed_data)

def bit_destuffing(data, flag):
    """Performs bit destuffing on the given data."""
    flag_size = len(flag)
    max_consecutive_ones = max(len(run) for run in ''.join(flag).split('0')) if '1' in flag else 0

    if max_consecutive_ones <= 1:
        raise ValueError("Flag must contain at least 2 consecutive 1s.")

    stuff_threshold = max_consecutive_ones - 1
    consecutive_ones = 0
    destuffed_data = list(data)

    i = 0
    while i < len(destuffed_data):
        if destuffed_data[i] == '1':
            consecutive_ones += 1
            if consecutive_ones == stuff_threshold and i + 1 < len(destuffed_data) and destuffed_data[i + 1] == '0':
                del destuffed_data[i + 1]
                consecutive_ones = 0
        else:
            consecutive_ones = 0
        i += 1

    return "".join(destuffed_data)

def main():
    """Main function to handle user input and perform bit stuffing/destuffing."""
    flag = input("Enter flag pattern (binary string, e.g., '01111110'): ")

    max_consecutive_ones = max(len(run) for run in ''.join(flag).split('0')) if '1' in flag else 0

    if max_consecutive_ones <= 1:
        print("Error: Flag must contain at least 2 consecutive 1s.")
        return

    print(f"Stuffing rule: A '0' will be inserted after {max_consecutive_ones - 1} consecutive 1s.")

    while True:
        print("\nOptions:")
        print("1. Perform bit stuffing")
        print("2. Perform bit destuffing")
        print("3. Stuff, destuff, and verify")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            data = input("Enter data to stuff (binary string): ")
            stuffed_data = bit_stuffing(data, flag)
            print("Original Data:", data)
            print("Stuffed Data: ", stuffed_data)

        elif choice == '2':
            stuffed_data = input("Enter stuffed data (binary string): ")
            destuffed_data = bit_destuffing(stuffed_data, flag)
            print("Stuffed Data: ", stuffed_data)
            print("Destuffed Data:", destuffed_data)

        elif choice == '3':
            data = input("Enter data (binary string): ")
            original_data = data
            stuffed_data = bit_stuffing(data, flag)
            destuffed_data = bit_destuffing(stuffed_data, flag)
            print("Original Data: ", original_data)
            print("Stuffed Data:  ", stuffed_data)
            print("Destuffed Data:", destuffed_data)
            print("Verification:  ", "SUCCESS" if original_data == destuffed_data else "FAILED")

        elif choice == '4':
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()          