import random
import string

def generate_password(length):
    # Combine all types of characters we want to include in password
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Use random.choice to select a random character from the set of all_characters
    password = ''.join(random.choice(all_characters) for i in range(length))

    return password

def main():
    length = int(input("Enter the length of the password: "))
    print("Generated password: " + generate_password(length))

if __name__ == "__main__":
    main()
