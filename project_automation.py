import json
from create import *
from build import BuildProject
from subprocess import *

# Creating Objects for both the Classes

create_obj = CreateProject()
main_obj = Main()

build_obj = BuildProject()

# The number of files to be executed
num = 1

# Reading the JSON Files:
pro = 'test_cases/create/test_case' + str(4) + '.json'
with open(pro, 'r') as JsonFile:
    create = json.load(JsonFile)
    result = main_obj.main(create)

if result == 1:
    for no in range(int(num)):
        # command_string = 'xprctl create_project -f test_cases/test_case4.json'
        command_string = "xprctl --help"
        create_pro = Popen(command_string, shell=True)
        create_pro.wait()

    # Calling the Build
    with open('test_cases/build/test_case1.json', 'r') as JsonFile:
        build_pro = json.load(JsonFile)
        res = build_obj.build_project(build_pro)
        print("Build Result")
        print(res)
        if res == 1:
            command_string = "xprctl info"
            create_pro = Popen(command_string, shell=True)
            create_pro.wait()
