# Copyright (c) 2020 Anindya Shiddhartha, licensed under MIT License.
# Read the LICENSE and README.md file for more information.
# This is the Python file for installing missing modules for the source code.
# Run it before executing main.py in the 'Source Code' folder.

import subprocess
import time

while True:
    user_command = input("\nStart process? (yes or no): ")

    if user_command == "yes":

        try:
            print("\nUpgrading PIP if available...")
            subprocess.run("python -m pip install --upgrade pip", shell=True, check=True)

            print("\nInstalling missing modules...")
            subprocess.run("python -m pip install playsound", shell=True, check=True)
            subprocess.run("python -m pip install youtube-dl", shell=True, check=True)
            subprocess.run("python -m pip install gTTS", shell=True, check=True)

        except:
            print("\u001b[31mUnexpected error occured during code execution...\u001b[0m")
            print("Closing in 3 seconds...")
            time.sleep(3)

        else:
            print("\u001b[32m\nProcess finished! Exiting window...\u001b[0m")
            time.sleep(1)
            break

    elif user_command == "no":
        
        print("Cleaning up...")
        time.sleep(1)
        break

    else:
        print("Command not found!")

