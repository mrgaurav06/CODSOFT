import random
import string
import time
print("***SMART PASSWORD GENERATOR****")

print("\nWelcome!")
print("This tool helps you create strong and secure passwords.\n")
while True:
    # Password length
    length = int(input("Enter password length: "))

    print("\nChoose what you want in your password:\n")
    use_upper = input("Include uppercase letters? (yes/no): ").lower()
    use_lower = input("Include lowercase letters? (yes/no): ").lower()
    use_numbers = input("Include numbers? (yes/no): ").lower()
    use_symbols = input("Include special symbols? (yes/no): ").lower()

    characters = ""
    password_list = []
    # Uppercase letters
    if use_upper == "yes":
        characters += string.ascii_uppercase
        password_list.append(random.choice(string.ascii_uppercase))
    # Lowercase letters
    if use_lower == "yes":
        characters += string.ascii_lowercase
        password_list.append(random.choice(string.ascii_lowercase))
    # Numbers
    if use_numbers == "yes":
        characters += string.digits
        password_list.append(random.choice(string.digits))
    # Symbols
    if use_symbols == "yes":
        characters += string.punctuation
        password_list.append(random.choice(string.punctuation))
    # If nothing selected
    if characters == "":
        print("\nPlease select at least one option.\n")
        continue
    print("\nGenerating secure password...")
    time.sleep(1)
    # Fill remaining characters
    while len(password_list) < length:
        password_list.append(random.choice(characters))
    # Shuffle password
    random.shuffle(password_list)
    # Convert list to string
    password = "".join(password_list)

    print("****GENERATED PASSWORD*****")
  
    print("\n", password)
    # Password strength
    print("\nPassword Strength:", end=" ")
    if length >= 12:
        print("Strong")
    elif length >= 8:
        print("Medium")
    else:
        print("Weak")

    # Generate again
    again = input("\nDo you want to generate another password? (yes/no): ").lower()
    if again != "yes":
        print("\nThank you for my  Password Generator ai")
        break