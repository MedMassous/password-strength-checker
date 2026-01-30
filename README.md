Password Strength Checker

A lightweight Python tool that checks how strong your passwords are. Built to learn about security basics and pattern matching.

## What it does

- Checks password length
- Looks for uppercase, lowercase, numbers, and symbols
- Warns about common passwords
- Catches repeated characters

## How to use
```bash
python password_checker.py
```

Then just type in a password when it asks.

## Example
```
Enter a password: test123
⚠️  Weak password
- Needs special characters
- Too short (min 8 characters)
```

## What I learned

This project helped me understand:
- Working with regex in Python
- Basic security concepts
- Input validation
- File handling for password lists

## Files

- `password_checker.py` - main script
- `common_passwords.txt` - list of weak passwords to check against
- `requirements.txt` - dependencies (if any)

## Tech

- Python 3
- Regular expressions

## Future ideas

- Add password strength scoring
- Check against breach databases
- Make it a command-line tool with arguments
- Add password generation

---

Feel free to try it out or suggest improvements!
