# Password Strength Checker
# Author: @MedMassous
# Description: Checks password strength and detects common weak patterns

import re 

MIN_LENGTH = 8
def load_common_passwords():
    with open('common_passwords.txt', 'r') as file:
        return set(line.strip() for line in file)
    
def check_strength(password,common_passwords):
    issues = []
    if len(password) < MIN_LENGTH:
        issues.append(f"Password must be at least {MIN_LENGTH} characters long.")

    if not re.search(r'[A-Z]', password):
        issues.append("Password must contain at least one uppercase letter.")

    if not re.search(r'[a-z]', password):
        issues.append("Password must contain at least one lowercase letter.")
    
    if not re.search(r'\d', password):
        issues.append("Password must contain at least one digit.")
    if password.lower() in common_passwords:
        issues.append("Password is too common.")    
    if re.search(r'(.)\1\1', password):
        issues.append("Repetitive characters detected.")
    return issues
def main():
    print("Welcome to the Password Strength Checker!")
    common_passwords = load_common_passwords()
    password = input("Enter a password to check: ")
    issues = check_strength(password,common_passwords)
    if issues:
        print("Password is weak for the following reasons:")
        for issue in issues:
            print(f"- {issue}")
    else:
        print("Password is strong!")
if __name__ == "__main__":
    main()
