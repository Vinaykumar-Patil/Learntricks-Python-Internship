'''Random Password Generator: Build a program that generates random passwords with 
user-defined length and complexity (e.g., uppercase, lowercase, numbers, symbols).'''

import random
import string

# Defining Function to generate a random password
def generate_password(length, uppercase=True, lowercase=True, numbers=True, symbols=True):
    characters = ''
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if symbols:
        characters += string.punctuation
    
    # Checking if at least one character set is selected
    if not characters:
        print("Error: At least one character set must be selected.")
        return None
    
    # Generating the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Defining Main function to interact with the user
def main():
    # Asking for the length of the password
    length = int(input("Enter the length of the password: "))
    
    # Warning, if password length is less than 4 characters
    if length < 4:
        print("Warning: Password length should be at least 4 characters for security reasons.")
        return
    
    # Asking for user preferences for character sets
    uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
    symbols = input("Include symbols? (yes/no): ").lower() == 'yes'
    
    # Warning, if no character set is selected
    if not (uppercase or lowercase or numbers or symbols):
        print("Warning: No character set selected. Password will be generated without any characters.")
    
    # Generating the password based on user preferences
    password = generate_password(length, uppercase, lowercase, numbers, symbols)
    if password:
        print("Generated Password:", password)

# Entry point of the program
if __name__ == "__main__":
    main()
