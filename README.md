# About The Tool

This is a reconnaissance tool for information gathering. The goal of the windows_keylogger tool is to listen to keystrokes, takes a screenshot, listens and records microphone waves, and to know what are the running processes. The purpose of this tool is to obtain sensitive information about the victim that can used to aid future attacks against them.

# How Does the code work:

The code contains five functions:

1. keyboard_log: This function records keystrokes and appends it to the keyboard.log 
2. ListenKeyboard: This function listens keystrokes
3. Microphone: This function listens and records microphone waves and stores in .wav extension 
4. screenshot: This function takes screenshots of the system
5. running_process: This function that gets all processes that are running from the Task Manager (Windows)

# How To Download It:

* git clone the file
* Installing all Modules 
1. ```pip install Pynput```
2. ```pip install sounddevice```
3. ```pip install scripy```
4. ```pip install numpy```
5. ```pip install opencv-python```
6. ```pip install sounddevice```
7. ```pip install logging```
8. ```pip install pyautogui```
9. ```pip install wmi```
* python windows_keylogger.py

# How to run the code:

1. To Execute: ```python windows_keylogger.py```
2. It will append a keyboard.log, output.wav, screenshot.png
3. The output will be stored in the same folder



