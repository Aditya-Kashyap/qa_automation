from subprocess import *


while True:
    print("What do you want to do with your git file")
    print("Please Select from the following Input")
    print("1. To Check the Status of the Git")
    print("2. To add files to the Git Repository")
    print("3. To Commit your Files")
    print("4. To Pull files from Git Repository")
    print("5. To Push the files into the repository")
    print("Anything Else to Exit")
    user_choice = input()

    if user_choice == '1':
        status = Popen("git status", shell=True)
        status.wait()

    elif user_choice == '2':
        add = Popen('git add .', shell=True)
        add.wait()

    elif user_choice == '3':
        print("Enter you committing message")
        message = input()
        comm = 'git commit -m ' + '"' + message + '"'
        commit = Popen(comm, shell=True)
        commit.wait()

    elif user_choice == '4':
        pull = Popen('git pull', shell=True)
        pull.wait()

    elif user_choice == '5':
        push = Popen('git push', shell=True)
        push.wait()

    else:
        break
