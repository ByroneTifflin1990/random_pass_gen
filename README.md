# 🔐 Python Password Generator

A simple and interactive Python CLI tool that generates secure random passwords using lowercase, uppercase, and special characters.

---

## 🧰 Features

- Generates passwords of a user-defined length
- Enforces a minimum length of 5 characters
- Includes lowercase, uppercase, and special symbols
- Continues running until the user chooses to exit
- Handles invalid input gracefully using exception handling

---

## 🛠️ Technologies Used

- Python 3
- `random` and `string` modules

---

## 📜 How It Works

1. The user is prompted to enter the desired length of the password.
2. If the number is less than the minimum length (5), the app will re-prompt the user.
3. A password is generated using randomly selected characters from a mix of:
   - Uppercase letters (A-Z)
   - Lowercase letters (a-z)
   - Special characters (!, %, ^, &, etc.)
4. The password is printed to the console.
5. The user is asked if they want to generate another password.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system

### Running the Script

```bash
python password_generator.py
