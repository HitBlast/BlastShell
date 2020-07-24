# Please read README.md and LICENSE for more information.

print("This will take a few moments...")

# Program authorship variables.
__author__ = "Anindya Shiddhartha"
__copyright__ = "Copyright 2020 Anindya Shiddhartha"
__version__ = "1.0"
__license__ = "MIT"

# Mathematical memory variable.
math_mem = 0

# Modules to import.
import os
dir_path = os.getcwd()

def windowcls():
    os.system('cls')

def get_current_path():
    os.getcwd()

import socket
host_name = socket.gethostname()

import random
from datetime import datetime
from fractions import Fraction
import webbrowser
import shutil

from win32com.client import Dispatch
S = Dispatch("SAPI.SpVoice")

import youtube_dl
import platform

# Fetching device specs.
device_platform = platform.machine()
processor = platform.processor()
operating_system = platform.system()
build = platform.version()


# Main interface.
windowcls()
print("BlastShell | Type 'help' or 'about' for more information.")
print(__copyright__)

while True:

    user_command = input("\u001b[0m\n" + host_name + " <--> \u001b[36m").lower().replace(" ", "")

    if user_command == "about":
        print("\n\n\033[1;34mBlastShell\u001b[0m | Version: " + __version__)
        print("Licensed under " + __license__ + " | " + __copyright__)
        print("\nAn easy-to-use interactive command line interface / shell developed mainly")
        print("for solving complex mathematical problems and for accomplishing day-to-day")
        print("tasks. BlastShell has a handful of useful commands available inside it, so")
        print("that users can use this application freely, without having to use internet")
        print("connection.")
        print("\nBlastShell gets updated frequently in order to maintain stable experience,")
        print("and also to introduce new commands and features to the users of it.")
        print("\nReach / Support: hitblastofficial@gmail.com\n")

    elif user_command == "help":
        print("\u001b[0m\n\nCD         Displays current working directory and changes it.")
        print("CLS        Refreshes the screen.")
        print("CLOCK      Displays current date and time.")
        print("CRDIR      Creates a directory.")
        print("CTEXT      Executes text file builder which enables user to create & modify")
        print("           text files.")
        print("DEL        Removes a file or directory.")
        print("EXIT       Terminates the shell.")
        print("IPCONF     Displays device's hostname and IP address.")
        print("LISTDIR    Displays all subdirectories in current working directory.")
        print("MATH       Executes mathematics console.")
        print("RESTART    Restarts device.")
        print("SYS        Displays device specifications in detail.")
        print("SPEAK      Speaks a text given by user.")
        print("SHUTDOWN   Turns off device.")
        print("VDL        Downloads a specific video from YouTube as well as from")
        print("           other destinations when executed. (as video or audio)")
        print("WEB        Enables console to enter specific or custom")
        print("           websites.\n")

    elif user_command == "exit":
        print("\u001b[0mClosing shell...")
        break

    elif user_command == "listdir":
        list_dir = str(os.listdir()).replace("[", "").replace("]", "").replace("'", "")
        print("\n\n\u001b[33m" + list_dir + "\n\n")

    elif user_command == "shutdown":
        shutdown_confirm = input("\u001b[0mConfirm device shutdown? (Yes/No) <> ").lower().replace(" ", "")

        if shutdown_confirm == "yes":
            print("\u001b[32mShutting down...\u001b[0m")
            os.system("shutdown /s /t 1")

        elif shutdown_confirm == "no":
            print("\u001b[32mShutdown aborted!\u001b[0m")

        else:
            print("\u001b[31mCommand not found! Try either 'Yes' or 'No'.\u001b[0m")

    elif user_command == "restart":
        restart_confirm = input("\u001b[0mConfirm device restart? (Yes/No) <> ").lower().replace(" ", "")

        if restart_confirm == "yes":
            print("\u001b[32mRestarting...\u001b[0m")
            os.system("shutdown /r /t 1")

        elif restart_confirm == "no":
            print("\u001b[32mRestart aborted!\u001b[0m")

        else:
            print("\u001b[31mCommand not found! Try either 'Yes' or 'No'.")

    elif user_command == "cd":
        print("\u001b[0mCurrent Path: \u001b[33m" + dir_path)
        dir_path = input("\u001b[0mNew Path <> ")

        if dir_path == "":
            print("\u001b[31mPath field empty! Reverting back to previous working directory.")
            get_current_path()

        else:
            try:
                os.chdir(dir_path)

            except:
                print("\u001b[31mPath not found! Reverting back to previous working directory.\u001b[0m")
                get_current_path()

            else:
                print("\u001b[32mPath set as current working directory.\u001b[0m")

    elif user_command == "ipconf":

        try: 
            host_name = socket.gethostname() 
            host_ip = socket.gethostbyname(host_name) 

        except: 
            print("\u001b[31mUnable to get hostname and IP address! Try again later.\u001b[0m")

        else:
            print("\u001b[0m\n\nHostname   : \u001b[32m" + host_name + "\u001b[0m") 
            print("IP Address : \u001b[32m" + host_ip + "\u001b[0m\n") 

    elif user_command == "ctext":
        print("\u001b[0mExecuted text file builder. Type 'help' to show executable commands.")

        while True:
            ctext_command = input("\nText Builder> ").lower().replace(" ", "")

            if ctext_command == "help":
                print("\n\nCRT    Creates a text file in program directory.")
                print("CLS    Refreshes the screen.")
                print("CUST   Creates a text file with text in a custom")
                print("       file extension.")
                print("EXIT   Terminates text file builder.")
                print("MOD    Created a text file with text in program") 
                print("       directory.\n")

            elif ctext_command == "crt":
                file_name_mainword = input("File Name <> ")
                file_name = file_name_mainword + ".txt"
                my_file = open(file_name,"w+")
                print("\u001b[32mSuccessfully created file.\u001b[0m")
                break

            elif ctext_command == "cust":

                try:
                    file_name_mainword = input("File Name <> ")
                    file_name_extension = input("File Extension <> ")
                    file_name = file_name_mainword + "." + file_name_extension
                    my_file = open(file_name,"w+")
                    my_file.write(input("Text <> "))
                    my_file = open(file_name,"w+")
                    print("\u001b[32mSuccessfully created file with text in custom extension.\u001b[0m")
                    break

                except:
                    print("\u001b[31mFile extension can't be empty!\u001b[0m")

            elif ctext_command == "cls":
                windowcls()

            elif ctext_command == "mod":
                file_name_mainword = input("File Name <> ")
                file_name = file_name_mainword + ".txt"
                my_file = open(file_name,"w+")
                my_file.write(input("Text <> "))
                my_file = open(file_name,"w+")
                print("\u001b[32mSuccessfully created file with text.\u001b[0m")
                break

            elif ctext_command == "exit":
                break

            else:
                print("\u001b[31mWhoa! Command not found. Type 'help' to show executable commands.\u001b[0m")

    elif user_command == "math":
        print("\u001b[0mMathematics console enabled. Type 'help' to show executable commands.")

        while True:
            math_command = input("\nMath> ").lower().replace(" ", "")

            if math_command == "help":
                print("\n\nADD        Adds two numbers.")
                print("AGECONV    Converts age from traditional 'years' format to days, hours and minutes.")
                print("CLS        Refreshes the screen.")
                print("CUBE       Cubes a number.")
                print("DIV        Divides one number with another.")
                print("EXIT       Quits mathematical console.")
                print("GENNUM     Generates a value within given minimum and maximum value.")
                print("MEM        Shows values stored in math memory.")
                print("MULTI      Multiplies one number with another.")
                print("NUMFRAQ    Converts a decimal number to a fraction.")
                print("PI         Adds the value of pi to memory.")
                print("PROFLOSS   Detects profit or loss by using purchase and selling value.")
                print("MEMCLS     Clears application maemory.")
                print("SQ         Squares a given value.")
                print("SUB        Subtracts one number with another.")
                print("XQ         Modify a number with a to-the-power value.\n")

            elif math_command == "exit":
                break

            elif math_command == "ageconv":
        
                try:
                    math_user_age_inyears = float(input("Age (In Years) <> "))

                    math_user_age_indays = math_user_age_inyears * 365
                    math_user_age_inhours = math_user_age_indays * 24
                    math_user_age_inminutes = math_user_age_inhours * 60

                except OverflowError:
                    print("\u001b[31mAge too big to calculate!\u001b[0m")

                except ValueError:
                    print("\u001b[31mInvalid age! Try again with a valid number.\u001b[0m")

                else:
                    print("\n\nHere's what your age is in...\n")
                    print("Days    : \u001b[32m" + str(math_user_age_indays) + "\u001b[0m days.")
                    print("Hours   : \u001b[32m" + str(math_user_age_inhours) + "\u001b[0m hours.")
                    print("Minutes : \u001b[32m" + str(math_user_age_inminutes) + "\u001b[0m minutes.\n")

            elif math_command == "gennum":

                try:
                    gen_minvalue = float(input("Minimum Value <> "))
                    gen_maxvalue = float(input("Maximum Value <> "))
                    gen_res = random.randint(gen_minvalue, gen_maxvalue)
                
                except OverflowError:
                    print("\u001b[31mValue too large to solve!\u001b[0m")

                except ValueError:
                    print("\u001b[31mInvalid number! Try again with a valid number.\u001b[0m")

                else:
                    addtomem = input("Add to memory? (Yes/No) <> ").lower().replace(" ", "")

                    if addtomem == "yes":
                        math_mem += gen_res
                        print("Generated Value = \u001b[32m" + str(gen_res) + "\u001b[0m [Added to memory]")

                    elif addtomem == "no":
                        print("Generated Value = \u001b[32m" + str(gen_res) + "\u001b[0m")

                    else:
                        print("\u001b[31mCommand not found! Try either 'Yes' or 'No'.")

            elif math_command == "profloss":

                try:
                    buy_value = float(input("Purchase Value <> "))
                    sell_value = float(input("Selling Value <> "))

                    if buy_value < sell_value:
                        sell_value -= buy_value
                        profloss_value = sell_value / buy_value * 100
                        output_type = ("Profit \u001b[32m")

                    elif buy_value > sell_value:
                        buy_value -= sell_value
                        profloss_value = buy_value / sell_value * 100
                        output_type = ("Loss \u001b[31m")

                    else:
                        buy_value -= sell_value
                        profloss_value = buy_value / sell_value * 100
                        output_type = ("None \u001b[32m")

                except ValueError:
                    print("\u001b[31mValue invalid! Try again with a valid number.\u001b[0m")

                except OverflowError:
                    print("\u001b[31mValue too large to solve!\u001b[0m")

                else:
                    addtomem = input("Add to memory? (Yes/No) <> ").lower().replace(" ", "")

                    if addtomem == "yes":
                        math_mem += profloss_value
                        print("Result = " + output_type + "(" + str(profloss_value) + "%) \u001b[0m [Added to memory]")

                    elif addtomem == "no":
                        print("Result = " + output_type + "(" + str(profloss_value) + "%) \u001b[0m")

                    else:
                        print("\u001b[31mCommand not found! Try either 'Yes' or 'No'.")

            elif math_command == "pi":
                pi_value = 3.1415926535897932384626433832

                if math_mem == 0:
                    math_mem += pi_value
                    print("Pi = \u001b[32m" + str(pi_value) + "\u001b[0m [Added to memory]")

                else:
                    print("Using previous memory results for main value.")
                    pi_action = input("Action (add/sub/div/multi) <> ").lower().replace(" ", "")

                    if pi_action == "add":

                        try:
                            math_mem += pi_value

                        except OverflowError:
                            print("\u001b[31mMemory overload!\u001b[0m")

                        else:
                            print("Result = \u001b[32m" + str(math_mem) + "\u001b[0m [Refreshed memory]")

                    elif pi_action == "sub":
                        
                        try:
                            math_mem -= pi_value

                        except OverflowError:
                            print("\u001b[31mMemory overload!\u001b[0m")

                        else:
                            print("Result = \u001b[32m" + str(math_mem) + "\u001b[0m [Refreshed memory]")

                    elif pi_action == "div":
                        
                        try:
                            math_mem /= pi_value

                        except OverflowError:
                            print("\u001b[31mMemory overload!\u001b[0m")

                        else:
                            print("Result = \u001b[32m" + str(math_mem) + "\u001b[0m [Refreshed memory]")

                    elif pi_action == "multi":
                        
                        try:
                            math_mem *= pi_value

                        except OverflowError:
                            print("\u001b[31mMemory overload!\u001b[0m")

                        else:
                            print("Result = \u001b[32m" + str(math_mem) + "\u001b[0m [Refreshed memory]")

                    else:
                        print("\u001b[31mAction not found! Try something else.\u001b[0m")

            elif math_command == "numfraq":

                if math_mem == 0:

                    try:
                        convfraq_num = float(input("Value <> "))

                    except OverflowError:
                        print("\u001b[31mValue too large to solve!\u001b[0m")

                    except ValueError:
                        print("\u001b[31mValue invalid! Try again with a valid number.\u001b[0m")

                    else:
                        print("Fraction = \u001b[32m" + str(Fraction(convfraq_num)) + "\u001b[0m")

                else:
                    
                    try:
                        print("Using previous memory result for main value.")
                        convfraq_num = Fraction(math_mem)

                    except OverflowError:
                        print("\u001b[31mUnexpected value error occured!\u001b[0m")

                    else:
                        print("Fraction = \u001b[32m" + str(convfraq_num) + "\u001b[0m")

            elif math_command == "xq":

                def xq(x, y):
                    return x ** y
                
                if math_mem == 0:

                    try:
                        xq_num1 = float(input("Primary Value <> "))
                        xq_num2 = float(input("To-The-Power Value <> "))
                        sum = xq(xq_num1, xq_num2)

                    except OverflowError:
                        print("\u001b[31mValue too large to solve!\u001b[0m")

                    except ValueError:
                        print("\u001b[31mValue invalid! Try again with a valid number.\u001b[0m")

                    else:
                        math_mem += sum
                        print("Result = \u001b[32m" + str(sum) + "\u001b[0m [Added to memory]")

                else:

                    try:
                        print("Using previous memory result for main value.")
                        xq_num2 = float(input("To-The-Power Value <> "))
                        sum = xq(math_mem, xq_num2)

                    except OverflowError:
                        print("\u001b[31mValue too large to solve!\u001b[0m")

                    except ValueError:
                        print("\u001b[31mValue invalid! Try again with a valid number.\u001b[0m")

                    else:
                        math_mem -= math_mem
                        math_mem += sum
                        print("Result = \u001b[32m" + str(sum) + "\u001b[0m [Refreshed memory]")

            elif math_command == "cube":

                def cube(x):
                    return x ** 3
                
                if math_mem == 0:

                    try:
                        cube_input = float(input("Value <> "))
                        sum = cube(cube_input)

                    except OverflowError:
                        print("\u001b[31mValue too large to solve!\u001b[0m")

                    except ValueError:
                        print("\u001b[31mValue invalid! Try again with a valid number.\u001b[0m")

                    else:
                        math_mem += sum
                        print("Result = \u001b[32m" + str(sum) + "\u001b[0m [Added to memory]")

                else:

                    try:
                        print("Using previous memory result for main value.")
                        sum = cube(math_mem)

                    except OverflowError:
                        print("\u001b[31mValue too large to solve!\u001b[0m")

                    else:
                        math_mem -= math_mem
                        math_mem += sum
                        print("Result = \u001b[32m" + str(sum) + "\u001b[0m [Refreshed memory]")

            elif math_command == "sq":

                def sq(x):
                    return x ** 2
                
                if math_mem == 0:

                    try:
                        sq_input = float(input("Value <> "))
                        sum = sq(sq_input)

                    except OverflowError:
                        print("\u001b[31mValue too large to solve!\u001b[0m")

                    except ValueError:
                        print("\u001b[31mValue invalid! Try again with a valid number.\u001b[0m")

                    else:
                        math_mem += sum
                        print("Result = \u001b[32m" + str(sum) + "\u001b[0m [Added to memory]")

                else:

                    try:
                        print("Using previous memory result for main value.")
                        sum = sq(math_mem)

                    except OverflowError:
                        print("\u001b[31mValue too large to solve!\u001b[0m")

                    else:
                        math_mem -= math_mem
                        math_mem += sum
                        print("Result = \u001b[32m" + str(sum) + "\u001b[0m [Refreshed memory]")

            elif math_command == "mem":
                
                if math_mem == 0:
                    print("\u001b[32mMathematical memory is empty!\u001b[0m")

                else:
                    print("Stored value = \u001b[32m" + str(math_mem) + "\u001b[0m")

            elif math_command == "memcls":
                math_mem -= math_mem
                print("\u001b[32mCleared math memory!\u001b[0m")

            elif math_command == "cls":
                windowcls()

            elif math_command == "add":

                def add(x, y):
                    return x + y

                if math_mem == 0:

                    try:
                        num1 = float(input("Value 1 <> "))
                        num2 = float(input("Value 2 <> "))
                        sum = add(num1, num2)

                    except OverflowError:
                        print("\u001b[31mValue too large to solve!\u001b[0m")

                    except ValueError:
                        print("\u001b[31mValue invalid! Try again with a valid number.\u001b[0m")

                    else:
                        math_mem += sum
                        print("Result = \u001b[32m" + str(sum) + "\u001b[0m [Added to memory]")

                else:

                    try:
                        print("Using previous memory result for main value.")
                        num1 = float(input("Value <> "))
                        sum = add(math_mem, num1)
                        

                    except OverflowError:
                        print("\u001b[31mValue too large to solve!\u001b[0m")

                    except ValueError:
                        print("\u001b[31mValue invalid! Try again with a valid number.\u001b[0m")

                    else:
                        math_mem -= math_mem
                        math_mem += sum
                        print("Result = \u001b[32m" + str(sum) + "\u001b[0m [Refreshed memory]")

            elif math_command == "sub":

                def sub(x, y):
                    return x - y

                if math_mem == 0:

                    try:
                        num1 = float(input("Value 1 <> "))
                        num2 = float(input("Value 2 <> "))
                        sum = sub(num1, num2)

                    except OverflowError:
                        print("\u001b[31mValue too large to solve!\u001b[0m")

                    except ValueError:
                        print("\u001b[31mValue invalid! Try again with a valid number.\u001b[0m")

                    else:
                        math_mem += sum
                        print("Result = \u001b[32m" + str(sum) + "\u001b[0m [Added to memory]")

                else:

                    try:
                        print("Using previous memory result for main value.")
                        num1 = float(input("Value <> "))
                        sum = sub(math_mem, num1)

                    except OverflowError:
                        print("\u001b[31mValue too large to solve!\u001b[0m")

                    except ValueError:
                        print("\u001b[31mValue invalid! Try again with a valid number.\u001b[0m")

                    else:
                        math_mem -= math_mem
                        math_mem += sum
                        print("Result = \u001b[32m" + str(sum) + "\u001b[0m [Refreshed memory]")

            elif math_command == "div":

                def div(x, y):
                    return x / y

                if math_mem == 0:

                    try:
                        num1 = float(input("Value 1 <> "))
                        num2 = float(input("Value 2 <> "))
                        sum = div(num1, num2)

                    except OverflowError:
                        print("\u001b[31mValue too large to solve!\u001b[0m")

                    except ValueError:
                        print("\u001b[31mValue invalid! Try again with a valid number.\u001b[0m")

                    else:
                        math_mem += sum
                        print("Result = \u001b[32m" + str(sum) + "\u001b[0m [Added to memory]")

                else:

                    try:
                        print("Using previous memory result for main value.")
                        num1 = float(input("Value <> "))
                        sum = div(math_mem, num1)

                    except OverflowError:
                        print("\u001b[31mValue too large to solve!\u001b[0m")

                    except ValueError:
                        print("\u001b[31mValue invalid! Try again with a valid number.\u001b[0m")

                    else:
                        math_mem -= math_mem
                        math_mem += sum
                        print("Result = \u001b[32m" + str(sum) + "\u001b[0m [Refreshed memory]")

            elif math_command == "multi":

                def multi(x, y):
                    return x * y

                if math_mem == 0:

                    try:
                        num1 = float(input("Value 1 <> "))
                        num2 = float(input("Value 2 <> "))
                        sum = multi(num1, num2)

                    except OverflowError:
                        print("\u001b[31mValue too large to solve!\u001b[0m")

                    except ValueError:
                        print("\u001b[31mValue invalid! Try again with a valid number.\u001b[0m")

                    else:
                        math_mem += sum
                        print("Result = \u001b[32m" + str(sum) + "\u001b[0m [Added to memory]")

                else:

                    try:
                        print("Using previous memory result for main value.")
                        num1 = float(input("Value <> "))
                        sum = multi(math_mem, num1)

                    except OverflowError:
                        print("\u001b[31mValue too large to solve!\u001b[0m")

                    except ValueError:
                        print("\u001b[31mValue invalid! Try again with a valid number.\u001b[0m")

                    else:
                        math_mem -= math_mem
                        math_mem += sum
                        print("Result = \u001b[32m" + str(sum) + "\u001b[0m [Refreshed memory]")

            else:
                print("\u001b[31mWhoa! Command not found. Type 'help' to show executable commands.\u001b[0m")

    elif user_command == "speak":
        speech_text = input("\u001b[0mText to speak <> ")
        S.Speak(speech_text)

    elif user_command == "clock":
        now = datetime.now()
        date_time = now.strftime("\u001b[0mDate: " + "%d/%m/%Y" + " | Time: " + "%H:%M:%S")
        print(date_time)

    elif user_command == "web":
        print("\u001b[0mExecuted web console! Type 'help' to show executable commands.")

        while True:
            web_command = input("\nWeb> ").lower().replace(" ", "")

            if web_command == "help":
                print("\n\nCLS      Refreshes the screen.")
                print("CSITE    Opens a custom webpage given by user.")
                print("EXIT     Closes web console.")
                print("SEARCH   Searches the web for a particular object given by user.")
                print("SITES    Shows a list of popular sites to open.\n")

            elif web_command == "csite":
                website = input("Website link / URL <> ")
                webbrowser.open(website, new=2)
                print("\u001b[32mWeb page opened successfully!\u001b[0m")
                break

            elif web_command == "search":
                search_topic = input("Search <> ")
                website = "https://www.google.com/search?q=" + search_topic
                webbrowser.open(website, new=2)
                print("Showing results found for \u001b[32m'" + search_topic + "'\u001b[0m.")
                break

            elif web_command == "exit":
                break

            elif web_command == "cls":
                windowcls()

            elif web_command == "sites":

                print("\n\nEnter site name in-line to open.\n")
                print("1  YouTube")
                print("2  Facebook")
                print("3  Wikipedia")
                print("4  Google")
                print("5  LinkedIn")
                print("6  GitHub\n\n")

                sites_execute = input("Site Name <> ").lower().replace(" ", "")

                if sites_execute == "youtube":
                    webbrowser.open('www.youtube.com', new=2)
                    print("\u001b[32mWeb page opened successfully!\u001b[0m")
                    break

                elif sites_execute == "facebook":
                    webbrowser.open('www.facebook.com', new=2)
                    print("\u001b[32mWeb page opened successfully!\u001b[0m")
                    break

                elif sites_execute == "wikipedia":
                    webbrowser.open('www.wikipedia.org', new=2)
                    print("\u001b[32mWeb page opened successfully!\u001b[0m")
                    break

                elif sites_execute == "google":
                    webbrowser.open('www.google.com', new=2)
                    print("\u001b[32mWeb page opened successfully!\u001b[0m")
                    break

                elif sites_execute == "linkedin":
                    webbrowser.open('www.linkedin.com', new=2)
                    print("\u001b[32mWeb page opened successfully!\u001b[0m")
                    break

                elif sites_execute == "github":
                    webbrowser.open('www.github.com', new=2)
                    print("\u001b[32mWeb page opened successfully!\u001b[0m")
                    break

                else:
                    print("\u001b[31mWebsite didn't found in list, try again!\u001b[0m")

            else:
                print("\u001b[31mWhoa! Command not found. Type 'help' to show executable commands.\u001b[0m")

    elif user_command == "cls":
        windowcls()

    elif user_command == "crdir":

        try:
            dir_name = input("\u001b[0mDirectory Name <> ")
            os.mkdir(dir_name)
            print("\u001b[32mDirectory created successfully!\u001b[0m")

        except:
            print("\u001b[31mDirectory name can't be empty!\u001b[0m")

    elif user_command == "del":

        while True:
            filetype = input("\u001b[0mFile Type ('help' to see filetypes) <> ").lower().replace(" ", "")

            if filetype == "help":
                print("\n\nCLS    Refreshes the screen.")
                print("DIR    Assigns file type as directory.")
                print("DOC    Assigns file type as document.")
                print("EXIT   Returns to home.\n\n")

            elif filetype == "cls":
                windowcls()

            elif filetype == "dir":
                mydir = input("Directory Path <> ")

                try:
                    shutil.rmtree(mydir)
                    print("\u001b[32mDeleted directory successfully!\u001b[0m")
                    break

                except OSError:
                    print("\u001b[31mDirectory not found, try again.\u001b[0m\n")

            elif filetype == "doc":
                mydoc = input("File Path <> ")

                if os.path.isfile(mydoc):
                    os.remove(mydoc)
                    print("\u001b[32mDeleted file successfully!\u001b[0m")
                    break

                else:
                    print("\u001b[31mFile not found, try again.\u001b[0m\n")

            elif filetype == "exit":
                break

            else:
                print("\u001b[31mFile type / command not recognized! Type 'help' to show executable commands.\u001b[0m")

    elif user_command == "sys":
        print("\u001b[0m\n\nDevice platform  : \u001b[32m" + device_platform + "\u001b[0m")
        print("Chipset          : \u001b[32m" + processor + "\u001b[0m")
        print("Operating system : \u001b[32m" + operating_system + "\u001b[0m")
        print("Build            : \u001b[32m" + build + "\u001b[0m\n")

    elif user_command == "vdl":

        def dwl_vid():
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([vidmain])

        vidformat = input("\u001b[0mDownload As ('help' to see formats) <> ").lower().replace(" ", "")

        if vidformat == "help":
            print("\n\nVIDEO    Refreshes the screen.")
            print("AUDIO    Assigns file type as directory.")
            print("DOC      Assigns file type as document.")
            print("EXIT     Returns to home.\n\n")

        elif vidformat == "video":

            try:
                ydl_opts = {}
                vidlink = input("Video link / URL <> ")
                vidmain = vidlink.strip()
                dwl_vid()

            except:
                print("\u001b[31mUnexpected error occured! Try again after ensuring stable internet connection and a valid video link.\u001b[0m")

            else:
                print("\u001b[32mVideo downloaded successfully!\u001b[0m")

        elif vidformat == "audio":

            try:
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                }

                vidlink = input("Video link / URL <> ")
                vidmain = vidlink.strip()
                dwl_vid()
                
            except:
                print("\u001b[31mUnexpected error occured! Try again after ensuring stable internet connection and a valid video link.\u001b[0m")

            else:
                print("\u001b[32mVideo successfully downloaded as audio.\u001b[0m")

        else:
            print("\u001b[31mFormat not recognised! Type either video or audio for format selection.\u001b[0m")

    else:
        print("\u001b[31mWhoa! Command not found. Type 'help' to show executable commands.\u001b[0m")