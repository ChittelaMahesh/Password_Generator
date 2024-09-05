import random
import math
import secrets
import string

# Define character sets
alpha_lower = string.ascii_lowercase
alpha_upper = string.ascii_uppercase
num = string.digits
special = "@#$%&*"

# Define password length and requirements
def get_password_length():
    while True:
        try:
            length = int(input("Enter Password Length (minimum 8): "))
            if length >= 8:
                return length
            else:
                print("Password length must be at least 8.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_custom_character_sets():
    custom_alpha = input("Include lowercase letters (y/n)? ").strip().lower() == 'y'
    custom_upper = input("Include uppercase letters (y/n)? ").strip().lower() == 'y'
    custom_num = input("Include numbers (y/n)? ").strip().lower() == 'y'
    custom_special = input("Include special characters (y/n)? ").strip().lower() == 'y'
    
    char_sets = ''
    if custom_alpha:
        char_sets += alpha_lower
    if custom_upper:
        char_sets += alpha_upper
    if custom_num:
        char_sets += num
    if custom_special:
        char_sets += special
    
    if not char_sets:
        print("At least one character set must be included.")
        return get_custom_character_sets()
    
    return char_sets

def generate_password(length, char_sets):
    password = []
    char_sets_len = len(char_sets)
    
    if char_sets_len == 0:
        raise ValueError("Character set is empty. Cannot generate password.")
    
    while len(password) < length:
        char = secrets.choice(char_sets)
        password.append(char)
    
    # Shuffle to ensure randomness
    secrets.SystemRandom().shuffle(password)
    
    return ''.join(password)

def main():
    print("Welcome to the Enhanced Password Generator!")
    
    length = get_password_length()
    char_sets = get_custom_character_sets()
    
    password = generate_password(length, char_sets)
    
    print(f"Generated Password: {password}")
    print("Password Strength:", evaluate_password_strength(password))

def evaluate_password_strength(password):
    length_criteria = len(password) >= 12
    uppercase_criteria = any(c.isupper() for c in password)
    lowercase_criteria = any(c.islower() for c in password)
    digit_criteria = any(c.isdigit() for c in password)
    special_criteria = any(c in special for c in password)
    
    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_criteria])
    
    if criteria_met == 5:
        return "Very Strong"
    elif criteria_met == 4:
        return "Strong"
    elif criteria_met == 3:
        return "Moderate"
    elif criteria_met == 2:
        return "Weak"
    else:
        return "Very Weak"

if __name__ == "__main__":
    main()
