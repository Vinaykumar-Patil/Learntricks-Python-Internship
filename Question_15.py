'''Password Manager: Design a password manager that securely stores and retrieves 
passwords for different accounts. Use encryption to protect sensitive data.'''

from cryptography.fernet import Fernet
import os

# Defining a class which manages passwaord 
class PasswordManager:
    def __init__(self, key_file):
        """Initialize the PasswordManager object."""
        self.key_file = key_file
        self.load_key()

    def load_key(self):
        """Load encryption key from file or generate new key if file does not exist."""
        if os.path.exists(self.key_file):
            with open(self.key_file, "rb") as key_file:
                self.key = key_file.read()
        else:
            self.generate_key()

    def generate_key(self):
        """Generate a new encryption key and save it to a file."""
        self.key = Fernet.generate_key()
        with open(self.key_file, "wb") as key_file:
            key_file.write(self.key)

    def encrypt_password(self, password):
        """Encrypt password using the encryption key."""
        cipher_suite = Fernet(self.key)
        return cipher_suite.encrypt(password.encode())

    def decrypt_password(self, encrypted_password):
        """Decrypt encrypted password using the encryption key."""
        cipher_suite = Fernet(self.key)
        return cipher_suite.decrypt(encrypted_password).decode()

    def save_password(self, account, password):
        """Save encrypted password to a file."""
        encrypted_password = self.encrypt_password(password)
        with open(f"{account}.pwd", "wb") as password_file:
            password_file.write(encrypted_password)

    def get_password(self, account):
        """Retrieve decrypted password from file."""
        with open(f"{account}.pwd", "rb") as password_file:
            encrypted_password = password_file.read()
        return self.decrypt_password(encrypted_password)

# Defining main function
def main():
    key_file = "key.key"  # Path to the key file
    password_manager = PasswordManager(key_file)

    while True:
        print("\nPassword Manager Menu:")
        print("1. Save Password")
        print("2. Get Password")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            account = input("Enter account name: ")
            password = input("Enter password: ")
            password_manager.save_password(account, password)
            print("Password saved successfully!")
        elif choice == "2":
            account = input("Enter account name: ")
            try:
                password = password_manager.get_password(account)
                print(f"Password for {account}: {password}")
            except FileNotFoundError:
                print("Password not found for the specified account.")
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
