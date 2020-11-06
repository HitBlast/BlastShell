# Copyright (c) 2020 Anindya Shiddhartha, licensed under MIT License.
# Read the LICENSE and README.md file for more information.
# This is the Python file for installing missing modules for the source code.
# Run it before executing main.py in the 'Source Code' folder.

from subprocess import run
from time import sleep
from platform import system

operating_system = system()

while True:
    user_command = input("\nStart process? (Yes / No): ").lower()

    if user_command == "yes":
        try:
            if operating_system == "Linux":
                print("\nUpgrading PIP if available...")
                run("pip3 install --upgrade pip", shell=True, check=True)

                print("\nInstalling missing modules...")
                run("pip3 install playsound", shell=True, check=True)
                run("pip3 install youtube-dl", shell=True, check=True)
                run("pip3 install gTTS", shell=True, check=True)
                run("pip3 install wget", shell=True, check=True)

            else:
                print("\nUpgrading PIP if available...")
                run("python -m pip install --upgrade pip", shell=True, check=True)

                print("\nInstalling missing modules...")
                run("python -m pip install playsound", shell=True, check=True)
                run("python -m pip youtube-dl", shell=True, check=True)
                run("python -m pip install gTTS", shell=True, check=True)
                run("python -m pip install wget", shell=True, check=True)

        except:
            print("\u001b[31mUnexpected error occured during code execution, try again later.\u001b[0m")
            print("Closing in 3 seconds...")
            sleep(3)

        else:
            print("\u001b[32m\nProcess finished! Exiting window...\u001b[0m")
            sleep(1)
            break

    elif user_command == "no":
        print("Cleaning up...")
        sleep(1)
        break

    else:
        print("Command not found! Try typing 'Yes' or 'No'.")

