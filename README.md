# Password Manager

A cross-platform password manager application built with Python and Tkinter. This tool helps you securely store and manage your passwords, generating strong, random passwords and saving them for easy retrieval.

## Features

- **Generate Strong Passwords**: Create secure, random passwords with a mix of letters, numbers, and symbols.
- **Save and Manage Passwords**: Store passwords associated with various websites in a secure JSON file.
- **Find Existing Passwords**: Retrieve stored passwords based on the website name.
- **Cross-Platform**: Compatible with multiple operating systems, including Windows, macOS, and Linux.

## Technologies Used

- **Python**: The programming language used for development.
- **Tkinter**: Used for creating the graphical user interface (GUI).
- **Pyperclip**: Clipboard module for copying passwords to the clipboard.
- **JSON**: For storing and retrieving passwords.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/password-manager.git
    ```
2. Navigate into the project directory:
    ```bash
    cd password-manager
    ```
3. Install dependencies using Poetry:
    ```bash
    poetry install
    ```
4. Run the application:
    ```bash
    poetry run python main.py
    ```

## Usage

- Open the application.
- Use the "Generate Password" button to create a new password.
- Enter the website, email, and password, and click "Add" to save the information.
- Use the "Search" button to find saved passwords by website name.

