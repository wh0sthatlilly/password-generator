import random
import string

def generate_password(length):
    # Characters to use
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    special = string.punctuation

    # Combine all characters
    all_characters = upper + lower + digits + special

    # Ensure at least one character from each category
    password = [
        random.choice(upper),
        random.choice(lower),
        random.choice(digits),
        random.choice(special)
    ]

    # Fill the remaining length with random characters
    if length < 4:
        print("Password length must be at least 4.")
        return None

    password += random.choices(all_characters, k=length - 4)

    # Shuffle to avoid predictable pattern
    random.shuffle(password)

    return "".join(password)


def main():
    print("=== PASSWORD GENERATOR TOOL ===")

    try:
        length = int(input("Enter desired password length: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    result = generate_password(length)
    
    if result:
        print("\nYour Generated Password:")
        print(result)


if __name__ == "__main__":
    main()
