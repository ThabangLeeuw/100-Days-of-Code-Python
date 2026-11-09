# Password Manager

A simple Password Manager application built with Python and Tkinter that allows users to generate secure passwords, save login credentials, and search for stored credentials using a local JSON database.

## Features

- Generate secure random passwords
- Automatically copy passwords to the clipboard
- Save website credentials to a JSON file
- Search for stored credentials by website name
- Handle missing or empty JSON files
- Simple Tkinter graphical user interface

## Screenshot

![Password Manager Screenshot](screenshot.png)

## Built With

- Python
- Tkinter
- JSON
- Pyperclip

## Getting Started

### Prerequisites

- Python 3.x

### Installation

```bash
git clone https://github.com/your-username/password-manager.git
cd password-manager
pip install pyperclip
```

### Run the Application

```bash
python main.py
```

## Project Structure

```text
password-manager/
├── main.py
├── password.json
├── logo.png
├── screenshot.png
└── README.md
```

## Example JSON Format

```json
{
    "Google": {
        "email/username": "example@gmail.com",
        "password": "Password123!"
    },
    "Github": {
        "email/username": "developer@example.com",
        "password": "SecurePass@2026"
    }
}
```

## What I Learned

This project helped me practice:

- Tkinter GUI development
- JSON file handling
- Exception handling
- Python dictionaries
- File I/O operations
- Password generation
- Clipboard integration with Pyperclip

## Future Improvements

- Password strength indicator
- Update existing credentials
- Delete credentials
- Password encryption
- Search suggestions
- Dark mode

## Author

**Imraan Thabang Leeuw**

Aspiring Data Engineer | Python Developer | Microsoft Fabric Enthusiast

Connect with me on LinkedIn and GitHub to follow my learning journey and projects.
