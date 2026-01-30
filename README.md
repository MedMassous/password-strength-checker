# Password Strength Checker

A simple Python tool that evaluates password strength by detecting weak patterns and common security issues.  
This project was created to practice security fundamentals and pattern matching using Python.

## Features

- Checks minimum password length
- Detects uppercase and lowercase letters
- Detects numbers and special characters
- Identifies common passwords
- Flags repeated characters

## Usage

Run the script:

```bash
python password_checker.py
Enter a password when prompted.

Example
Enter a password: test123

Weak password detected:
- Missing special characters
- Too short (minimum 8 characters)
What I Learned
Using regular expressions in Python

Basic password security concepts

Input validation

Reading and processing files

Writing simple security-focused scripts

Project Structure
password-strength-checker/
├── password_checker.py
├── common_passwords.txt
├── README.md
└── requirements.txt
Data Source
The file common_passwords.txt contains a list of common passwords from a public dataset:

https://github.com/iryndin/10K-Most-Popular-Passwords

Technologies
Python 3

Regular expressions

Future Improvements
Add password strength scoring

Check passwords against breach databases

Convert the script into a CLI tool

Add password generation

Notes
This project is intentionally kept simple and beginner-friendly, with a focus on understanding security basics rather than building a production tool.


---

### Why this version is better
- **No emojis** (professional GitHub look)
- Clean heading hierarchy
- Proper fenced code blocks
- No broken inline Markdown
- Renders correctly in GitHub preview

If you want, next I can:
- Rewrite it to sound **SOC / blue-team oriented**
- Add a **LICENSE**
- Add **badges**
- Turn this into a **portfolio-level project**

Say the word.
