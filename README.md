# 🔐 Password Strength Checker

A lightweight Python tool that evaluates password strength by detecting weak patterns and common security issues.  
Built as a hands-on project to learn **security fundamentals**, **regex**, and **defensive thinking**.

---

## 🚀 Features

- Enforces minimum password length  
- Detects uppercase, lowercase, numbers, and special characters  
- Identifies common and widely used passwords  
- Flags repeated character patterns (e.g. `aaa`, `111`)  

---

## ▶️ How to Use

Run the script:

```bash
python password_checker.py
When prompted, enter a password to receive instant feedback.

🧪 Example Output
Enter a password: test123

⚠️ Weak password detected:
- Missing special characters
- Too short (minimum 8 characters)
📚 What I Learned
This project helped me practice and understand:

Regular expressions in Python

Password security best practices

Input validation and user feedback

File handling for password lists

Defensive (blue team) security thinking

📁 Project Structure
password-strength-checker/
├── password_checker.py
├── common_passwords.txt
├── README.md
└── requirements.txt
🛠️ Technologies Used
Python 3

Regular Expressions (re module)

📄 Data Source
common_passwords.txt contains the 10,000 most common passwords

Source:
https://github.com/iryndin/10K-Most-Popular-Passwords

🔮 Future Improvements
Add password strength scoring (entropy-based)

Check passwords against breach databases (e.g. Have I Been Pwned API)

Convert into a CLI tool using argparse

Add secure password generation

🤝 Feedback
Feel free to try it out, fork the repository, or suggest improvements.
This project is intentionally simple and focused on learning core security concepts.


---

### ✅ Why this README works on GitHub
- Correct heading hierarchy (`#`, `##`)
- Proper fenced code blocks
- Clean lists with spacing
- No broken Markdown
- Recruiter-friendly language

If you want next:
- **Badges (Python, Security, Beginner)**
- **SOC-style wording**
- **Resume bullet points from this project**
- **v2 roadmap section**

Just say which one 🔥
