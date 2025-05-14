#!/usr/bin/python
import subprocess
import os 
def interactive():
    subprocess.run(['python3'])
def script():
    SName = input('Enter script name: ')
    subprocess.run(['touch', SName])
    subprocess.run(['nano', SName])
    choice = input('Run the script, build or none?(r/b/n)')
    if choice == 'y':
        subprocess.run(['python3', SName]) 
    elif choice == 'b':
        # Build into executable
        EName = input('Enter executable name: ')
        installRes = os.system('pip install pyinstaller > /dev/null 2>&1')
        if installRes != 0:
            print("Failed to install pyinstaller")
            os.system('killall IDLE')
        try:
            subprocess.run(['pyinstaller', '--onefile', SName, '--name', EName])
            print(f"Executable made for {SName} as {EName}")
        except:
            print(f"Failed to build {SName} as {EName}")
    else:
        return

def main():
    print('\033[1;32mWelcome to IDLE\033[0m')
    while 1:
        print('1. Interactive mode\n2. Script mode\n3. Exit\nEnter your choice:')
        choice = int(input())
        os.system('clear')
        if choice == 1:
            interactive()
        elif choice == 2:
            script()
        elif choice == 3:
            break
        else:
            continue
        os.system('clear')

        


if __name__ == '__main__':
    main()