def main():
    while True:
        print("\nMenu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        choice = input("Please enter an option: ")

        if choice == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print(f"Your password has been encoded and stored as: {encoded_password}")

        elif choice == "2":
            encoded_password = input("Please enter the encoded password to decode: ")
            decoded_password = decode(encoded_password)
            print(f"The decoded password is: {decoded_password}")

        elif choice == "3":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")


# PARTNER COMMIT
def encode(password):
     

# PARTNER COMMIT
def decode(encoded_password):
    

if __name__ == "__main__":
    main()