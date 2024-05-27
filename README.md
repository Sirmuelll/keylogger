# Python Keylogger

This project is a keylogger implemented in Python. It captures keystrokes, logs them, and sends the logs via email at regular intervals. It also ensures persistence by adding itself to the Windows startup registry, ensuring it runs every time the system boots.

## Note: 
- Being security minded, I have used placeholders rather than actual email and passwords. Furthermore, this would give room for persons to quickly understand and use the code. SO, Be sure to adjust the email configuration and SMTP server settings to match your requirements.

## Features

- **Keystroke Logging**: Captures all keystrokes made on the target machine.
- **Email Reporting**: Sends the captured keystrokes to a specified email address at regular intervals.
- **Persistence**: Adds itself to the Windows startup registry to run on every system boot.

## Installation

### Prerequisites

- Python 3.11.1
- Required Python libraries:
  - `pynput`
  - `smtplib`

You can install the required libraries using pip:

```bash
pip install pynput

LEGAL DISCLAIMER!!!
This keylogger is intended for educational purposes only. Unauthorized use of this software is illegal and unethical. 
