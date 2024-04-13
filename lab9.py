def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        
        option = input("Please enter an option: ")
        
        if option == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
        elif option == "2":
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
        elif option == "3":
            break
        else:
            print("Invalid option. Please try again.")

def encode(password):
    # Your code for the encode function goes here
    pass

# Your partner will provide the decode function
def decode(encoded_password):
    pass

if __name__ == "__main__":
    main()