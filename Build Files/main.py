# Please read README.md and LICENSE for more information.

# Program authorship variables.
__author__ = "Anindya Shiddhartha"
__copyright__ = "Copyright 2020 Anindya Shiddhartha"
__version__ = "1.12Pre1"
__license__ = "MIT"

# Modules to import.
import time
try:
    import os
    import socket
    import random
    from datetime import datetime
    from fractions import Fraction
    import webbrowser
    import shutil
    import platform

    import wget
    import youtube_dl
    from playsound import playsound
    from gtts import gTTS
    from gtts.tts import gTTSError

except ModuleNotFoundError:
    print("\u001b[31mUnexpected error occured while loading modules, closing application...\u001b[0m")
    time.sleep(5)
    exit()

# Defining common functions.
def windowcls():
    if "Linux" in operating_system:
        os.system('clear')
    else:
        os.system('cls')

# Defining variables.
dir_path = os.getcwd()
math_mem = int()
host_name = socket.gethostname()

device_platform = platform.machine()
processor = platform.processor()
operating_system = platform.system()
build = platform.version()


# Main interface.
windowcls()
print("    ____  __           __  _____ __         ____")
print("   / __ )/ /___ ______/ /_/ ___// /_  ___  / / /")
print("  / __  / / __ `/ ___/ __/\__ \/ __ \/ _ \/ / / ")
print(" / /_/ / / /_/ (__  ) /_ ___/ / / / /  __/ / /  ")
print("/_____/_/\__,_/____/\__//____/_/ /_/\___/_/_/   \n\n")

print("Type 'help' or 'about' for more information.")
print(f"{__copyright__}.")

while True:
    user_command = input(f"\u001b[0m\n{host_name} <--> \u001b[36m").split()
    argument_count = len(user_command)

    if argument_count < 1:
        print("\u001b[31mCommand area can't be empty!\u001b[0m")

    else:
        if user_command[0].lower() == "about":
            print(f"\n\n\n\u001b[34mBlastShell\u001b[0m | Version: {__version__}")
            print(f"Licensed under {__license__} | {__copyright__}")
            print("\nAn easy-to-use interactive command line interface / shell developed mainly")
            print("for solving complex mathematical problems and for accomplishing day-to-day")
            print("tasks. BlastShell has a handful of useful commands available inside it, so")
            print("that users can use this application freely, without having to use internet")
            print("connection.")
            print("\nBlastShell gets updated frequently in order to maintain stable experience,")
            print("and also to introduce new commands and features to the users of it.")
            print("\n\nPersonal Website  [] shiddharth.github.io")
            print("Facebook          [] www.facebook.com/shiddharth.codes")
            print("Twitter           [] www.twitter.com/shiddharthcodes")
            print("GitHub            [] www.github.com/shiddharth")
            print("LinkedIn          [] www.linkedin.com/in/shiddharth-codes\n\n")

        elif user_command[0].lower() == "help":
            print("\u001b[33m\n\n?\u001b[0m Type '[YOUR_COMMAND] + docs' for more information about that particular command.\n")
            print("BLAST      Starts a new instance of the BlastShell command line.")
            print("CLEAR      Refreshes the screen.")
            print("CRDIR      Creates a directory.")
            print("CHPATH     Displays current working directory and changes it.")
            print("DEL        Removes a file or directory.")
            print("EXIT       Terminates the shell.")
            print("IPCONF     Displays device's hostname and IP address.")
            print("LS         Displays all subdirectories in current working directory.")
            print("MATH       Executes mathematics console.")
            print("PATH       Displays current working directory.")
            print("REPO       Opens the GitHub repository of BlastShell in a browser window.")
            print("RESTART    Restarts device.")
            print("SYS        Displays device specifications.")
            print("SHELL      Runs shell commands from within the program.")
            print("SPEAK      Speaks a text given by user.")
            print("SHUTDOWN   Turns off device.")
            print("TIME       Displays current date and time.")
            print("TBUILD     Executes text file builder which enables user to create & modify")
            print("           custom text files.")
            print("VDL        Downloads a specific video from YouTube as well as from")
            print("           other destinations when executed. (as video or audio)")
            print("WEB        Enables console to enter specific or custom websites.\n")

        elif user_command[0].lower() == "shell":
            if argument_count == 1:
                shell_command = input("\u001b[0mShell> ")
                os.system(shell_command)

            elif argument_count == 2 and user_command[1].lower() == "docs":
                print("\u001b[0mDocumentation for command: SHELL\u001b[0m")
                print("\nDescription:")
                print("    \u001b[33m?\u001b[0m This command is used to run shell commands from within")
                print("    \u001b[33m?\u001b[0m BlastShell.")
                print("\nUsage:")
                print("    \u001b[32m>>>\u001b[0m shell")
                print("    \u001b[32mShell>\u001b[0m [ENTER_COMMAND_HERE]")

            else:
                print("\u001b[31mInvalid argument(s)! Try typing 'shell docs' for it's usage information.\u001b[0m")

        elif user_command[0].lower() == "blast":
            
            if argument_count == 1:
                math_mem = 0
                windowcls()
                print("\u001b[0m    ____  __           __  _____ __         ____")
                print("   / __ )/ /___ ______/ /_/ ___// /_  ___  / / /")
                print("  / __  / / __ `/ ___/ __/\__ \/ __ \/ _ \/ / / ")
                print(" / /_/ / / /_/ (__  ) /_ ___/ / / / /  __/ / /  ")
                print("/_____/_/\__,_/____/\__//____/_/ /_/\___/_/_/   \n\n")

                print("Type 'help' or 'about' for more information.")
                print(__copyright__)
                dir_path = os.getcwd()

            elif argument_count == 2 and user_command[1].lower() == "docs":
                print("\u001b[0mDocumentation for command: BLAST\u001b[0m")
                print("\nDescription:")
                print("    \u001b[33m?\u001b[0m This command is used to start a new instance of BlastShell")
                print("    \u001b[33m?\u001b[0m command line.")
                print("\nUsage:")
                print("    \u001b[32m>>>\u001b[0m blast")

            else:
                print("\u001b[31mInvalid argument(s)! Try typing 'blast docs' for it's usage information.\u001b[0m")

        elif user_command[0].lower() == "exit":

            if argument_count == 1:
                print("\u001b[0mClosing shell...")
                break

            elif argument_count == 2 and user_command[1].lower() == "docs":
                print("\u001b[0mDocumentation for command: EXIT\u001b[0m")
                print("\nDescription:")
                print("    \u001b[33m?\u001b[0m This command is used to exit the application or")
                print("    \u001b[33m?\u001b[0m terminate it.")
                print("\nUsage:")
                print("    \u001b[32m>>>\u001b[0m exit")

            else:
                print("\u001b[31mInvalid argument(s)! Try typing 'exit docs' for it's usage information.\u001b[0m")

        elif user_command[0].lower() == "repo":

            if argument_count == 1:
                webbrowser.open('www.github.com/shiddharth/BlastShell', new=2)
                print("\u001b[0mGitHub repository opened successfully!\u001b[0m")

            elif argument_count == 2 and user_command[1].lower() == "docs":
                print("\u001b[0mDocumentation for command: REPO\u001b[0m")
                print("\nDescription:")
                print("    \u001b[33m?\u001b[0m This command is used to open the official GitHub")
                print("    \u001b[33m?\u001b[0m repository of BlastShell.")
                print("\nUsage:")
                print("    \u001b[32m>>>\u001b[0m repo")

            else:
                print("\u001b[31mInvalid argument(s)! Try typing 'repo docs' for it's usage information.\u001b[0m")

        elif user_command[0].lower() == "ls":

            if argument_count == 1:
                list_dir = os.listdir()
                print("\n\u001b[33m")

                for dir in list_dir:
                    print(dir)

                print()

            elif argument_count == 2 and user_command[1].lower() == "docs":
                print("\u001b[0mDocumentation for command: LS\u001b[0m")
                print("\nDescription:")
                print("    \u001b[33m?\u001b[0m This command is used to display the files and folders")
                print("    \u001b[33m?\u001b[0m of current directory in a vertical list.")
                print("\nUsage:")
                print("    \u001b[32m>>>\u001b[0m ls")

            else:
                print("\u001b[31mInvalid argument(s)! Try typing 'ls docs' for it's usage information.\u001b[0m")

        elif user_command[0].lower() == "shutdown":

            if argument_count == 2:

                if user_command[1].lower() == "docs":
                    print("\u001b[0mDocumentation for command: SHUTDOWN\u001b[0m")
                    print("\nDescription:")
                    print("    \u001b[33m?\u001b[0m This command is used to turn off the device.")
                    print("\nUsage:")
                    print("    \u001b[32m>>>\u001b[0m shutdown + <YES / NO [TYPE_THEM_TO_CONFIRM_OR_ABORT_SHUTDOWN]>")

                elif user_command[1].lower() == "yes":
                    print("\u001b[0mShutting down...\u001b[0m")
                    os.system("shutdown /s /t 1")

                elif user_command[1].lower() == "no":
                    print("\u001b[0mShutdown aborted!\u001b[0m")

                else:
                    print("\u001b[31mInvalid argument(s)! Try typing 'shutdown docs' for it's usage information.\u001b[0m")

            else:
                print("\u001b[31mInvalid argument(s)! Try typing 'shutdown docs' for it's usage information.\u001b[0m")

        elif user_command[0].lower() == "restart":

            if argument_count == 2:

                if user_command[1].lower() == "docs":
                    print("\u001b[0mDocumentation for command: RESTART\u001b[0m")
                    print("\nDescription:")
                    print("    \u001b[33m?\u001b[0m This command is used to restart the device.")
                    print("\nUsage:")
                    print("    \u001b[32m>>>\u001b[0m restart + <YES / NO [TYPE_THEM_TO_CONFIRM_OR_ABORT_RESTART]>")

                elif user_command[1].lower() == "yes":
                    print("\u001b[0mRestarting...\u001b[0m")
                    os.system("shutdown /r /t 1")

                elif user_command[1].lower() == "no":
                    print("\u001b[0mRestart aborted!\u001b[0m")

                else:
                    print("\u001b[31mInvalid argument(s)! Try typing 'restart docs' for it's usage information.\u001b[0m")

            else:
                print("\u001b[31mInvalid argument(s)! Try typing 'restart docs' for it's usage information.\u001b[0m")

        elif user_command[0].lower() == "path":

            if argument_count == 1:
                print(f"\u001b[0mCurrent Path: \u001b[33m{dir_path}\u001b[0m")

            elif argument_count == 2 and user_command[1].lower() == "docs":
                print("\u001b[0mDocumentation for command: PATH\u001b[0m")
                print("\nDescription:")
                print("    \u001b[33m?\u001b[0m This command is used to view the current directory")
                print("    \u001b[33m?\u001b[0m the program is working on.")
                print("\nUsage:")
                print("    \u001b[32m>>>\u001b[0m path")

            else:
                print("\u001b[31mInvalid argument(s)! Try typing 'path docs' for it's usage information.\u001b[0m")

        elif user_command[0].lower() == "chpath":

            if argument_count == 2:

                if user_command[1].lower() == "docs":
                    print("\u001b[0mDocumentation for command: CHPATH\u001b[0m")
                    print("\nDescription:")
                    print("    \u001b[33m?\u001b[0m This command is used to change the current directory")
                    print("    \u001b[33m?\u001b[0m the program is working on.")
                    print("\nUsage:")
                    print("    \u001b[32m>>>\u001b[0m chpath + [ENTER_NEW_PATH_HERE]")
                    print("    \u001b[31m#\u001b[0m Make sure to fill the spaces of directory paths with")
                    print("    \u001b[31m#\u001b[0m underscores (_) or the program may return an error.")

                else:
                    new_dir_path = user_command[1].replace("_", " ")
                    try:
                        os.chdir(new_dir_path)

                    except:
                        print("\u001b[31mPath not found! Reverting back to previous working directory.\u001b[0m")
                        dir_path = os.getcwd()

                    else:
                        print("\u001b[0mPath set as current working directory.\u001b[0m")
                        dir_path = os.getcwd()

            else:
                print("\u001b[31mInvalid argument(s)! Try typing 'chpath docs' for it's usage information.\u001b[0m")

        elif user_command[0].lower() == "ipconf":

            if argument_count == 1:
                try: 
                    host_name = socket.gethostname() 
                    host_ip = socket.gethostbyname(host_name) 

                except: 
                    print("\u001b[31mUnable to get hostname and IP address! Try again later.\u001b[0m")

                else:
                    print(f"\u001b[0m\n\nHostname   : \u001b[32m{host_name}\u001b[0m") 
                    print(f"IP Address : \u001b[32m{host_ip}\u001b[0m\n") 

            elif argument_count == 2 and user_command[1].lower() == "docs":
                print("\u001b[0mDocumentation for command: IPCONF\u001b[0m")
                print("\nDescription:")
                print("    \u001b[33m?\u001b[0m This command is used to view the hostname and the IP")
                print("    \u001b[33m?\u001b[0m address of the device.")
                print("\nUsage:")
                print("    \u001b[32m>>>\u001b[0m ipconf")

            else:
                print("\u001b[31mInvalid argument(s)! Try typing 'ipconf docs' for it's usage information.\u001b[0m")

        elif user_command[0].lower() == "tbuild":

            if argument_count == 2 and user_command[1].lower() == "docs":
                print("\u001b[0mDocumentation for command: TBUILD\u001b[0m")
                print("\nDescription:")
                print("    \u001b[33m?\u001b[0m This command is used to create files with or without")
                print("    \u001b[33m?\u001b[0m text inside them.")
                print("\nArguments:")
                print("    \u001b[33m$\u001b[0m READ - Reads a file.")
                print("    \u001b[33m$\u001b[0m MAKE - Creates a file.")
                print("\nUsage:")
                print("    \u001b[32m>>>\u001b[0m tbuild + [ENTER_ARGUMENT_HERE] + [ENTER_FILE_NAME_HERE]")
                print("    \u001b[31m#\u001b[0m Make sure to replace spaces in file names with")
                print("    \u001b[31m#\u001b[0m underscores (_), or the program may return an error.")

            elif argument_count == 3:

                if user_command[1].lower() == "read":
                    file_name = user_command[2].replace("_", " ")
                    
                    try:
                        file = open(file_name, "r")
                        file_contents = file.read()

                    except:
                        print("\u001b[31mUnable to detect file, invalid name / path!\u001b[0m")

                    else:
                        print(f"\u001b[0mViewing the contents of \u001b[33m{file_name}\u001b[0m")
                        print(f"\n{file_contents}")

                elif user_command[1].lower() == "make":
                    file_name = user_command[2].replace("_", " ")
                    
                    if os.path.isfile(file_name):
                        print("\u001b[31mFile already exists!\u001b[0m")
                        
                    else:
                        with open(file_name, "w+") as file:
                            file_text = input("\u001b[0mText <> ")
                            file.write(file_text)

                else:
                    print("\u001b[31mInvalid argument(s)! Try typing 'tbuild docs' for it's usage information.\u001b[0m")    

            else:
                print("\u001b[31mInvalid argument(s)! Try typing 'tbuild docs' for it's usage information.\u001b[0m")    

        elif user_command[0].lower() == "math":

            if argument_count == 1:
                print("\u001b[0mMathematics console enabled! Type 'help' to show executable commands.")

                while True:
                    math_command = input("\u001b[0m\nMath> ").split()

                    if math_command[0].lower() == "help":
                        print("\n\nADD        Adds value(s) together.")
                        print("AGECONV    Converts age from traditional 'years' format to days, hours and")
                        print("           minutes.")
                        print("CUBE       Cubes a number.")
                        print("CLEAR      Refreshes the screen.")
                        print("DIV        Divides value(s) with each other.")
                        print("EXIT       Quits mathematical console.")
                        print("FACTOR     Factorizes a given number.")
                        print("MEM        Shows values stored in math memory.")
                        print("MULTI      Multiplies value(s) with each other.")
                        print("MEMCLS     Clears application maemory.")
                        print("NUMGEN     Generates a value within given minimum and maximum value.")
                        print("NUMCENT    Converts numbers to percentage based on the given main and the")
                        print("           secondary value.")
                        print("NUMFRAQ    Converts a decimal number to a fraction.")
                        print("NUMSORT    Sorts a list of numbers into multiple orders.")
                        print("PI         Adds the value of pi to memory.")
                        print("PROFLOSS   Detects profit or loss by using purchase and selling value(s) of")
                        print("           an object or product.")
                        print("SQ         Squares a given value.")
                        print("SUB        Subtracts value(s) from other one(s).")
                        print("XQ         Modify a number with a to-the-power value.\n")

                    elif math_command[0].lower() == "exit":
                        break

                    elif math_command[0].lower() == "mem":
                        
                        if math_mem == 0:
                            math_mem_status = "[Empty]"

                        else:
                            math_mem_status = "[Used]"

                        print(f"Stored value = \u001b[33m{math_mem}\u001b[0m {math_mem_status}")

                    elif math_command[0].lower() == "memcls":
                        math_mem -= math_mem
                        print("Cleared math memory!")

                    elif math_command[0].lower() == "clear":
                        windowcls()

                    elif math_command[0].lower() == "factor":
                        num = int(input("Value <> "))
                        num_factors = list()

                        for num_factored in range(1, num + 1):
                            if num % num_factored == 0:
                                num_factors.append(num_factored)

                        print("Factors of " + str(num) + " = \u001b[32m" + str(num_factors).replace("[", "").replace("]", "") + "\u001b[0m")

                    elif math_command[0].lower() == "numcent":
                        def numcent(num1, num2):
                            num1 = float(num1)
                            num2 = float(num2)
                            percentage = '{0:.2f}'.format((num1 / num2 * 100))
                            return percentage

                        try:
                            num1 = int(input("Value 1 <> "))
                            num2 = int(input("Value 2 <> "))
                            res = numcent(num1, num2)

                        except OverflowError:
                            print("\u001b[31mValue(s) too big to be calculated!\u001b[0m")

                        except ValueError:
                            print("\u001b[31mInvalid value! Try again with a valid number.\u001b[0m")

                        else:
                            print(f"Result = \u001b[32m{res}%\u001b[0m")

                    elif math_command[0].lower() == "numsort":
                        value_num = 0
                        list_num = list() 

                        try:
                            value_qty = int(input("Value Quantity <> "))

                            for i in range(0, value_qty): 
                                value_num += 1
                                value = int(input(f"Value {value_num} <> ")) 
                                list_num.append(value)

                        except OverflowError:
                            print("\u001b[31mValue(s) too big to be calculated!\u001b[0m")

                        except ValueError:
                            print("\u001b[31mInvalid value! Try again with a valid number.\u001b[0m")

                        else:
                            sort_type = input("\nSort Order (Ascending / Descending / Even / Odd) <> ").lower().replace(" ", "")

                            if sort_type == "ascending":
                                list_res = sorted(list_num)
                                print("Result (Ascending Order) = \u001b[32m" + str(list_res).replace("[", "").replace("]", "") + "\u001b[0m")

                            elif sort_type == "descending":
                                list_res = sorted(list_num, reverse=True)
                                print("Result (Descending Order) = \u001b[32m" + str(list_res).replace("[", "").replace("]", "") + "\u001b[0m")

                            elif sort_type == "even":
                                only_even = list() 

                                for num in list_num:
                                    if num % 2 == 0:  
                                        only_even.append(num) 

                                print("Result (Only Even) = \u001b[32m" + str(only_even).replace("[", "").replace("]", "") + "\u001b[0m")

                            elif sort_type == "odd":
                                only_odd = list()

                                for num in list_num:
                                    if num %2 != 0:
                                        only_odd.append(num)

                                print("Result (Only Odd) = \u001b[32m" + str(only_odd).replace("[", "").replace("]", "") + "\u001b[0m")

                            else:
                                print("\u001b[31mSort order invalid! Try either 'Ascending' or 'Descending'.\u001b[0m")

                    elif math_command[0].lower() == "ageconv":
                
                        try:
                            math_user_age_inyears = float(input("Age (In Years) <> "))

                            math_user_age_indays = math_user_age_inyears * 365
                            math_user_age_inhours = math_user_age_indays * 24
                            math_user_age_inminutes = math_user_age_inhours * 60

                        except OverflowError:
                            print("\u001b[31mAge too big to be calculated!\u001b[0m")

                        except ValueError:
                            print("\u001b[31mInvalid value! Try again with a valid number.\u001b[0m")

                        else:
                            print("\n\nHere's what your age is in...\n")
                            print(f"Days    : \u001b[32m{math_user_age_indays}\u001b[0m days.")
                            print(f"Hours   : \u001b[32m{math_user_age_inhours}\u001b[0m hours.")
                            print(f"Minutes : \u001b[32m{math_user_age_inminutes}\u001b[0m minutes.\n")

                    elif math_command[0].lower() == "numgen":

                        try:
                            gen_minvalue = float(input("Minimum Value <> "))
                            gen_maxvalue = float(input("Maximum Value <> "))
                            gen_res = random.randint(gen_minvalue, gen_maxvalue)
                        
                        except OverflowError:
                            print("\u001b[31mValue(s) too big to be calculated!\u001b[0m")

                        except ValueError:
                            print("\u001b[31mInvalid value! Try again with a valid number.\u001b[0m")

                        else:
                            print(f"\nGenerated Value = \u001b[32m{gen_res}\u001b[0m")
                            value_addtomem = input("Add to memory? (Yes / No) <> ").lower().replace(" ", "")

                            if value_addtomem == "yes":
                                math_mem += gen_res
                                print("Result added to memory.")
                                print(f"Memory = \u001b[33m{math_mem}\u001b[0m")

                            elif value_addtomem == "no":
                                print("Skipped memory addition.")

                            else:
                                print("\u001b[31mUnknown action! Try typing either 'Yes' or 'No'.\u001b[0m")

                    elif math_command[0].lower() == "profloss":

                        try:
                            buy_value = float(input("Purchase Value <> "))
                            sell_value = float(input("Selling Value <> "))

                            if buy_value < sell_value:
                                profloss_value_money = sell_value - buy_value
                                sell_value -= buy_value
                                profloss_value_percentage = sell_value / buy_value * 100
                                output_type = ("Profit \u001b[32m")

                            elif buy_value > sell_value:
                                profloss_value_money = buy_value - sell_value
                                buy_value -= sell_value
                                profloss_value_percentage = buy_value / sell_value * 100
                                output_type = ("Loss \u001b[31m")

                            else:
                                profloss_value_money = buy_value - sell_value
                                buy_value -= sell_value
                                profloss_value_percentage = buy_value / sell_value * 100
                                output_type = ("None \u001b[32m")

                        except ValueError:
                            print("\u001b[31mInvalid value! Try again with a valid number.\u001b[0m")

                        except OverflowError:
                            print("\u001b[31mValue(s) too big to be calculated!\u001b[0m")

                        else:
                            print(f"\nResult = {output_type}({profloss_value_percentage}%) \u001b[0m| Money = \u001b[32m{profloss_value_money}\u001b[0m")
                            value_addtomem = input("Add to memory? (Yes / No) <> ").lower().replace(" ", "")

                            if value_addtomem == "yes":
                                math_mem += profloss_value_money
                                print("Result added to memory.")
                                print(f"Memory = \u001b[33m{math_mem}\u001b[0m")

                            elif value_addtomem == "no":
                                print("Skipped memory addition.")

                            else:
                                print("\u001b[31mUnknown action! Try typing either 'Yes' or 'No'.\u001b[0m")

                    elif math_command[0].lower() == "pi":
                        pi_value = 3.1415926535897932384626433832

                        if math_mem == 0:
                            print(f"Pi = \u001b[32m{pi_value}\u001b[0m")
                            value_addtomem = input("Add to / refresh memory? (Yes / No) <> ").lower().replace(" ", "")

                            if value_addtomem == "yes":
                                math_mem += pi_value
                                print("Result added to memory.")
                                print(f"Memory = \u001b[33m{math_mem}\u001b[0m")

                            elif value_addtomem == "no":
                                print("Skipped memory addition.")

                            else:
                                print("\u001b[31mUnknown action! Try typing either 'Yes' or 'No'.\u001b[0m")

                        else:
                            print(f"Pi = \u001b[32m{pi_value}\u001b[0m")
                            print("Using previous memory result for main value.")
                            pi_action = input("Action (add/sub/div/multi) <> ").lower().replace(" ", "")

                            if pi_action == "add":

                                try:
                                    res = math_mem + pi_value

                                except OverflowError:
                                    print("\u001b[31mResult can't be added to memory, value overflow!\u001b[0m")

                                else:
                                    value_addtomem = input("\nAdd to / refresh memory? (Yes / No) <> ").lower().replace(" ", "")

                                    if value_addtomem == "yes":
                                        math_mem -= math_mem
                                        math_mem += res
                                        print("Result added to memory.")
                                        print(f"Memory = \u001b[33m{math_mem}\u001b[0m")

                                    elif value_addtomem == "no":
                                        print("Skipped memory addition.")

                                    else:
                                        print("\u001b[31mUnknown action! Try typing either 'Yes' or 'No'.\u001b[0m")

                            elif pi_action == "sub":
                                
                                try:
                                    res = math_mem - pi_value

                                except OverflowError:
                                    print("\u001b[31mResult can't be added to memory, value overflow!\u001b[0m")

                                else:
                                    value_addtomem = input("\nAdd to / refresh memory? (Yes / No) <> ").lower().replace(" ", "")

                                    if value_addtomem == "yes":
                                        math_mem -= math_mem
                                        math_mem += res
                                        print("Result added to memory.")
                                        print(f"Memory = \u001b[33m{math_mem}\u001b[0m")

                                    elif value_addtomem == "no":
                                        print("Skipped memory addition.")
                                        
                                    else:
                                        print("\u001b[31mUnknown action! Try typing either 'Yes' or 'No'.\u001b[0m")

                            elif pi_action == "div":
                                
                                try:
                                    res = math_mem / pi_value

                                except OverflowError:
                                    print("\u001b[31mResult can't be added to memory, value overflow!\u001b[0m")

                                else:
                                    value_addtomem = input("\nAdd to / refresh memory? (Yes / No) <> ").lower().replace(" ", "")

                                    if value_addtomem == "yes":
                                        math_mem -= math_mem
                                        math_mem += res
                                        print("Result added to memory.")
                                        print(f"Memory = \u001b[33m{math_mem}\u001b[0m")

                                    elif value_addtomem == "no":
                                        print("Skipped memory addition.")
                                        
                                    else:
                                        print("\u001b[31mUnknown action! Try typing either 'Yes' or 'No'.\u001b[0m")

                            elif pi_action == "multi": 
                                
                                try:
                                    res = math_mem * pi_value

                                except OverflowError:
                                    print("\u001b[31mResult can't be added to memory, value overflow!\u001b[0m")

                                else:
                                    value_addtomem = input("\nAdd to / refresh memory? (Yes / No) <> ").lower().replace(" ", "")

                                    if value_addtomem == "yes":
                                        math_mem -= math_mem
                                        math_mem += res
                                        print("Result added to memory.")
                                        print(f"Memory = \u001b[33m{math_mem}\u001b[0m")

                                    elif value_addtomem == "no":
                                        print("Skipped memory addition.")
                                        
                                    else:
                                        print("\u001b[31mUnknown action! Try typing either 'Yes' or 'No'.\u001b[0m")

                            else:
                                print("\u001b[31mAction not found! Try something predefined.\u001b[0m")

                    elif math_command[0].lower() == "numfraq":

                        try:
                            convfraq_num = float(input("Value <> "))

                        except OverflowError:
                            print("\u001b[31mValue(s) too big to be calculated!\u001b[0m")

                        except ValueError:
                            print("\u001b[31mInvalid value! Try again with a valid number.\u001b[0m")

                        else:
                            print(f"Fraction = \u001b[32m{Fraction(convfraq_num)}\u001b[0m")

                    elif math_command[0].lower() == "xq":
                        def xq(x, y):
                            return x ** y
                        
                        try:
                            xq_num1 = float(input("Primary Value <> "))
                            xq_num2 = float(input("To-The-Power Value <> "))
                            res = xq(xq_num1, xq_num2)

                        except OverflowError:
                            print("\u001b[31mValue(s) too big to be calculated!\u001b[0m")

                        except ValueError:
                            print("\u001b[31mInvalid value! Try again with a valid number.\u001b[0m")

                        else:
                            print(f"\nResult = \u001b[32m{res}\u001b[0m")
                            value_addtomem = input("Add to / refresh memory? (Yes / No) <> ").lower().replace(" ", "")

                            if value_addtomem == "yes":
                                math_mem += res
                                print("Result added to memory.")
                                print(f"Memory = \u001b[33m{math_mem}\u001b[0m")

                            elif value_addtomem == "no":
                                print(f"Skipped memory addition.")

                            else:
                                print("\u001b[31mUnknown action! Try typing either 'Yes' or 'No'.\u001b[0m")

                    elif math_command[0].lower() == "cube":
                        def cube(x):
                            return x ** 3
                        
                        try:
                            cube_input = float(input("Value <> "))
                            res = cube(cube_input)

                        except OverflowError:
                            print("\u001b[31mValue(s) too big to be calculated!\u001b[0m")

                        except ValueError:
                            print("\u001b[31mInvalid value! Try again with a valid number.\u001b[0m")

                        else:
                            print(f"\nResult = \u001b[32m{res}\u001b[0m")
                            value_addtomem = input("Add to / refresh memory? (Yes / No) <> ").lower().replace(" ", "")

                            if value_addtomem == "yes":
                                math_mem += res
                                print("Result added to memory.")
                                print(f"Memory = \u001b[33m{math_mem}\u001b[0m")

                            elif value_addtomem == "no":
                                print(f"Skipped memory addition.")

                            else:
                                print("\u001b[31mUnknown action! Try typing either 'Yes' or 'No'.\u001b[0m")

                    elif math_command[0].lower() == "sq":
                        def sq(x):
                            return x ** 2
                        
                        try:
                            sq_input = float(input("Value <> "))
                            res = sq(sq_input)

                        except OverflowError:
                            print("\u001b[31mValue(s) too big to be calculated!\u001b[0m")

                        except ValueError:
                            print("\u001b[31mInvalid value! Try again with a valid number.\u001b[0m")

                        else:
                            print(f"\nResult = \u001b[32m{res}\u001b[0m")
                            value_addtomem = input("Add to / refresh memory? (Yes / No) <> ").lower().replace(" ", "")

                            if value_addtomem == "yes":
                                math_mem += res
                                print("Result added to memory.")
                                print(f"Memory = \u001b[33m{math_mem}\u001b[0m")

                            elif value_addtomem == "no":
                                print(f"Skipped memory addition.")

                            else:
                                print("\u001b[31mUnknown action! Try typing either 'Yes' or 'No'.\u001b[0m")

                    elif math_command[0].lower() == "add":
                        value_namenum = 0
                        res = 0
                        num = 0

                        try:
                            value_qty = int(input("Value Quantity <> "))

                            for i in range(0, value_qty):
                                value_namenum += 1
                                value_name = "Value " + str(value_namenum) + " <> "
                                num = int(input(value_name))
                                res += num

                        except OverflowError:
                            print("\u001b[31mValue(s) too big to be calculated!\u001b[0m")

                        except ValueError:
                            print("\u001b[31mInvalid value! Try again with a valid number.\u001b[0m")

                        else:
                            print(f"\nResult = \u001b[32m{res}\u001b[0m")
                            value_addtomem = input("Add to / refresh memory? (Yes / No) <> ").lower().replace(" ", "")

                            if value_addtomem == "yes":
                                math_mem += res
                                print("Result added to memory.")
                                print(f"Memory = \u001b[33m{math_mem}\u001b[0m")

                            elif value_addtomem == "no":
                                print(f"Skipped memory addition.")

                            else:
                                print("\u001b[31mUnknown action! Try typing either 'Yes' or 'No'.\u001b[0m")

                    elif math_command[0].lower() == "sub":
                        value_namenum = 0
                        res = 0
                        num = 0

                        try:
                            value_qty = int(input("Value Quantity <> "))

                            for i in range(0, value_qty):
                                value_namenum += 1
                                value_name = "Value " + str(value_namenum) + " <> "
                                num = int(input(value_name))
                                res -= num

                        except OverflowError:
                            print("\u001b[31mValue(s) too big to be calculated!\u001b[0m")

                        except ValueError:
                            print("\u001b[31mInvalid value! Try again with a valid number.\u001b[0m")

                        else:
                            print(f"\nResult = \u001b[32m{res}\u001b[0m")
                            value_addtomem = input("Add to / refresh memory? (Yes / No) <> ").lower().replace(" ", "")

                            if value_addtomem == "yes":
                                math_mem += res
                                print("Result added to memory.")
                                print(f"Memory = \u001b[33m{math_mem}\u001b[0m")

                            elif value_addtomem == "no":
                                print(f"Skipped memory addition.")

                            else:
                                print("\u001b[31mUnknown action! Try typing either 'Yes' or 'No'.\u001b[0m")

                    elif math_command[0].lower() == "div":
                        value_namenum = 0
                        num = 0
                        res = 0

                        try:
                            res = int(input("Primary Value <> "))
                            value_qty = int(input("Secondary Value Quantity <> "))

                            for i in range(0, value_qty):
                                value_namenum += 1
                                value_name = "Secondary Value " + str(value_namenum) + " <> "
                                num = int(input(value_name))
                                res /= num

                        except OverflowError:
                            print("\u001b[31mValue(s) too big to be calculated!\u001b[0m")

                        except ValueError:
                            print("\u001b[31mInvalid value! Try again with a valid number.\u001b[0m")

                        else:
                            print(f"\nResult = \u001b[32m{res}\u001b[0m")
                            value_addtomem = input("Add to / refresh memory? (Yes / No) <> ").lower().replace(" ", "")

                            if value_addtomem == "yes":
                                math_mem += res
                                print("Result added to memory.")
                                print(f"Memory = \u001b[33m{math_mem}\u001b[0m")

                            elif value_addtomem == "no":
                                print(f"Skipped memory addition.")

                            else:
                                print("\u001b[31mUnknown action! Try typing either 'Yes' or 'No'.\u001b[0m")

                    elif math_command[0].lower() == "multi":
                        value_namenum = 0
                        num = 0
                        res = 0

                        try:
                            res = int(input("Primary Value <> "))
                            value_qty = int(input("Secondary Value Quantity <> "))

                            for i in range(0, value_qty):
                                value_namenum += 1
                                value_name = "Secondary Value " + str(value_namenum) + " <> "
                                num = int(input(value_name))
                                res *= num

                        except OverflowError:
                            print("\u001b[31mValue(s) too big to be calculated!\u001b[0m")

                        except ValueError:
                            print("\u001b[31mInvalid value! Try again with a valid number.\u001b[0m")

                        else:
                            print(f"\nResult = \u001b[32m{res}\u001b[0m")
                            value_addtomem = input("Add to / refresh memory? (Yes / No) <> ").lower().replace(" ", "")

                            if value_addtomem == "yes":
                                math_mem += res
                                print("Result added to memory.")
                                print(f"Memory = \u001b[33m{math_mem}\u001b[0m")

                            elif value_addtomem == "no":
                                print(f"Skipped memory addition.")

                            else:
                                print("\u001b[31mUnknown action! Try typing either 'Yes' or 'No'.\u001b[0m")

                    else:
                        print("\u001b[31mWhoa! Command not found. Type 'help' to show executable commands.\u001b[0m")

            elif argument_count == 2 and user_command[1].lower() == "docs":
                print("\u001b[0mDocumentation for command: MATH\u001b[0m")
                print("\nDescription:")
                print("    \u001b[33m?\u001b[0m This command is used to solve mathematical problems")
                print("    \u001b[33m?\u001b[0m from within the command line.")
                print("\nArguments:")
                print("    \u001b[33m$\u001b[0m HELP - Shows usable commands.")
                print("\nUsage:")
                print("    \u001b[32m>>>\u001b[0m math")
                print("    Math\u001b[32m>\u001b[0m help [TYPE_IT_TO_SEE_COMMANDS]")
                
            else:
                print("\u001b[31mInvalid argument(s)! Try typing 'math docs' for it's usage information.\u001b[0m")

        elif user_command[0].lower() == "speak":

            if argument_count >= 3 and argument_count <= 4:
                def tts_action_start(text):
                    tts = gTTS(text)

                    if user_command[1].lower() == "say":
                        file_name = "blastshell-speak-" + str(random.randint(1, 100)) + ".mp3"
                        tts.save(file_name)
                        playsound(file_name)
                        os.remove(file_name)

                    elif user_command[1].lower() == "save":
                        file_name = user_command[3].replace("_", " ")
                        try:
                            tts.save(user_command[3])

                        except FileExistsError:
                            print("\u001b[31mFile already exists! Try again with a different file name.\u001b[0m")

                        except IndexError:
                            print("\u001b[31mInvalid argument(s)! Try typing 'speak docs' for it's usage information.\u001b[0m")
                            
                        else:
                            print(f"\u001b[0mSuccessfully converted text to speech and saved as \u001b[33m{user_command[3]}\u001b[0m.")

                    else:
                        print("\u001b[31mInvalid argument(s)! Try typing 'speak docs' for it's usage information.\u001b[0m")

                speech_text = user_command[2].replace("_", "")
                try:
                    tts_action_start(speech_text)

                except gTTSError:
                    print("\u001b[31mUnexpected error occured during code execution! Make sure that you have stable internet connection and try again.\u001b[0m")

            elif argument_count == 2 and user_command[1].lower() == "docs":
                print("\u001b[0mDocumentation for command: SPEAK\u001b[0m")
                print("\nDescription:")
                print("    \u001b[33m?\u001b[0m This command is used to convert text into speech.")
                print("\nArguments and usage:")
                print("    \u001b[33m$\u001b[0m SAY - Converts text to speech and starts speaking it.")
                print("        \u001b[32m>>>\u001b[0m speak + say + [ENTER_TEXT_HERE]")
                print("    \u001b[33m$\u001b[0m SAVE - Converts text to speech and saves it.")
                print("        \u001b[32m>>>\u001b[0m speak + save + [ENTER_TEXT_HERE] + [ENTER_FILE_NAME_HERE]")

            else:
                print("\u001b[31mInvalid argument(s)! Try typing 'speak docs' for it's usage information.\u001b[0m")

        elif user_command[0].lower() == "time":

            if argument_count == 1:
                now = datetime.now()
                date_time = now.strftime("\u001b[0mDate: " + "%d/%m/%Y" + " | Time: " + "%H:%M:%S")
                print(date_time)

            elif argument_count == 2 and user_command[1].lower() == "docs":
                print("\u001b[0mDocumentation for command: TIME\u001b[0m")
                print("\nDescription:")
                print("    \u001b[33m?\u001b[0m This command is used to display current date and time.")
                print("\nUsage:")
                print("    \u001b[32m>>>\u001b[0m time")

            else:
                print("\u001b[31mInvalid argument(s)! Try typing 'time docs' for it's usage information.\u001b[0m")

        elif user_command[0].lower() == "web":

            if argument_count == 3:
                if user_command[1].lower() == "search":
                    search_topic = user_command[2].replace("_", " ")
                    webbrowser.open(("https://www.google.com/search?q=" + search_topic), new=2)

                elif user_command[1].lower() == "open":
                    webbrowser.open(user_command[2], new=2)

                else:
                    print("\u001b[31mInvalid argument(s)! Try typing 'web docs' for it's usage information.\u001b[0m")

            elif argument_count == 4 and user_command[1].lower() == "dwl":
                try:
                    print(f"\u001b[0m\nPath: {dir_path}\u001b[0m")
                    print("\u001b[0mDownload started!\u001b[0m\n")
                    wget.download(user_command[2], user_command[3])

                except ValueError:
                    print("\u001b[31mUnexpected error occured! Make sure the link is valid before you continue.\u001b[0m")
                
                else:
                    print("\u001b[0mDownload finished!\u001b[0m")

            elif argument_count == 2 and user_command[1].lower() == "docs":
                print("\u001b[0mDocumentation for command: WEB\u001b[0m")
                print("\nDescription:")
                print("    \u001b[33m?\u001b[0m This command is used to execute web-based tasks from")
                print("    \u001b[33m?\u001b[0m within the command line. It's a group of sub-commands.")
                print("\nArguments and usage:")
                print("    \u001b[33m$\u001b[0m DWL - Downloads files from the web.")
                print("        \u001b[32m>>>\u001b[0m web + dwl + [ENTER_FILE_URL_HERE] + [ENTER_FILE_NAME_HERE]")
                print("    \u001b[33m$\u001b[0m SEARCH - Searches the web for a particular topic.")
                print("        \u001b[32m>>>\u001b[0m web + search + [ENTER_TOPIC_HERE]")
                print("        \u001b[31m#\u001b[0m Make sure to replace spaces in search topics with underscores (_),")
                print("        \u001b[31m#\u001b[0m or the program may return an error.")
                print("    \u001b[33m$\u001b[0m OPEN - Opens a particular URL in a new browser window.")
                print("        \u001b[32m>>>\u001b[0m web + open + [ENTER_URL_HERE]")
                
            else:
                print("\u001b[31mInvalid argument(s)! Try typing 'web docs' for it's usage information.\u001b[0m")

        elif user_command[0].lower() == "clear":

            if argument_count == 1:
                windowcls()

            elif argument_count == 2 and user_command[1].lower() == "docs":
                print("\u001b[0mDocumentation for command: CLEAR\u001b[0m")
                print("\nDescription:")
                print("    \u001b[33m?\u001b[0m This command is used to clear or refresh the program")
                print("    \u001b[33m?\u001b[0m window.")
                print("\nUsage:")
                print("    \u001b[32m>>>\u001b[0m clear")

            else:
                print("\u001b[31mInvalid argument(s)! Try typing 'clear docs' for it's usage information.\u001b[0m")

        elif user_command[0].lower() == "crdir":

            if argument_count == 3 and user_command[1].lower() == "make":
                os.mkdir(user_command[2])

            elif argument_count == 2 and user_command[1].lower() == "docs":
                print("\u001b[0mDocumentation for command: CRDIR\u001b[0m")
                print("\nDescription:")
                print("    \u001b[33m?\u001b[0m This command is used to create folders.")
                print("\nArguments:")
                print("    \u001b[33m$\u001b[0m MAKE - Creates folders.")
                print("\nUsage:")
                print("    \u001b[32m>>>\u001b[0m crdir + [ENTER_ARGUMENT_HERE] + [ENTER_FOLDER_NAME_HERE]")

            else:
                print("\u001b[31mInvalid argument(s)! Try typing 'crdir docs' for it's usage information.\u001b[0m")

        elif user_command[0].lower() == "del":

            if argument_count == 3:

                if user_command[1].lower() == "fold":
                    try:
                        shutil.rmtree(user_command[2])
                
                    except:
                        print("\u001b[31mDirectory not found, try again.\u001b[0m")

                elif user_command[1].lower() == "file":
                    if os.path.isfile(user_command[2]):
                        os.remove(user_command[2])

                    else:
                        print("\u001b[31mFile not found, try again.\u001b[0m")

            elif argument_count == 2 and user_command[1].lower() == "docs":
                print("\u001b[0mDocumentation for command: CLEAR\u001b[0m")
                print("\nDescription:")
                print("    \u001b[33m?\u001b[0m This command is used to delete files and folders.")
                print("\nArguments:")
                print("    \u001b[33m$\u001b[0m FILE - Assigns object as file.")
                print("    \u001b[33m$\u001b[0m FOLD - Assigns object as folder.")
                print("\nUsage:")
                print("    \u001b[32m>>>\u001b[0m del + [ENTER_ARGUMENT_HERE] + [ENTER_FILE_NAME_HERE]")

            else:
                print("\u001b[31mInvalid argument(s)! Try typing 'del docs' for it's usage information.\u001b[0m")
   
        elif user_command[0].lower() == "sys":

            if argument_count == 1:
                print(f"\u001b[0m\n\nDevice platform  : \u001b[32m{device_platform}\u001b[0m")
                print(f"Chipset          : \u001b[32m{processor}\u001b[0m")
                print(f"Operating system : \u001b[32m{operating_system}\u001b[0m")
                print(f"Build            : \u001b[32m{build}\u001b[0m\n")
            
            elif argument_count == 2 and user_command[1].lower() == "docs":
                print("\u001b[0mDocumentation for command: SYS\u001b[0m")
                print("\nDescription:")
                print("    \u001b[33m?\u001b[0m This command is used to display system configuration.")
                print("\nUsage:")
                print("    \u001b[32m>>>\u001b[0m sys")

            else:
                print("\u001b[31mInvalid argument(s)! Try typing 'sys docs' for it's usage information.\u001b[0m")

        else:
            print("\u001b[31mWhoa! Command not found. Type 'help' to show executable commands.\u001b[0m")