import random
import string

def generate_password(length):
    # Define possible characters: letters, digits, symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password of given length
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# --- Main Program ---
try:
    # Take user input for password length
    length = int(input("Enter the desired password length: "))
    
    if length < 4:
        print("Password length should be at least 4 characters.")
    else:
        password = generate_password(length)
        print(f"Generated Password: {password}")

except ValueError:
    print("Invalid input! Please enter a number.")
