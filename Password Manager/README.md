# Password Manager 🔐

A simple desktop Password Manager built with Python and Tkinter. The application allows users to generate secure passwords, automatically copy them to the clipboard, and save website credentials to a CSV file.

## Features

- Generate random passwords using letters, numbers, and special characters.
- Automatically copy generated passwords to the clipboard.
- Store website credentials in a CSV file.
- Validate user input before saving.
- Append new records without overwriting existing data.
- Simple and user-friendly graphical interface.

## Technologies Used

- Python 3
- Tkinter
- Pandas
- Pyperclip
- Random
- String

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/password-manager.git
cd password-manager
```

### Install Dependencies

```bash
pip install pandas pyperclip
```

### Run the Application

```bash
python main.py
```

## Project Structure

```text
password-manager/
│
├── main.py
├── logo.png
├── password.csv
└── README.md
```

## How It Works

### Generating a Password

1. Click the **Generate Password** button.
2. A random password is generated.
3. The password is automatically inserted into the Password field.
4. The password is copied to your clipboard.

### Saving Credentials

1. Enter the website name.
2. Enter your email/username.
3. Enter or generate a password.
4. Click the **Add** button.
5. The credentials are appended to `password.csv`.

## Example CSV Output

```csv
gmail.com,user@gmail.com,MyP@ssword123!
github.com,user@gmail.com,Secure#Pass456
```

## User Interface Components

| Component | Description |
|------------|-------------|
| Website | Stores the website name |
| Email/Username | Stores the login email or username |
| Password | Stores the generated or entered password |
| Generate Password | Creates a random password |
| Add | Saves credentials to the CSV file |

## Current Limitations

- Passwords are stored in plain text.
- No encryption is implemented.
- Duplicate entries are not checked.
- No password search functionality.
- No editing or deleting of saved credentials.

## Future Enhancements

- Encrypt stored passwords.
- Add website search functionality.
- Store credentials in JSON format.
- Add edit and delete features.
- Implement duplicate detection.
- Add password strength indicators.
- Add user authentication for improved security.

## Learning Objectives

This project demonstrates:

- GUI development using Tkinter
- Event-driven programming
- CSV file handling with Pandas
- Input validation
- Password generation techniques
- Clipboard integration with Pyperclip
- Working with Python modules and functions

## License

This project is open-source and intended for educational and personal use.

## Author

Imraan Thabang Leeuw

Built as part of a Python learning journey focused on GUI development, data handling, and practical application development.
