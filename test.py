# import json
# import pickle
from subprocess import *

# name = input("Project Name: ")
# cmd = 'xprctl get_project -i \'{ \"name\": \"' + name + '\" }\''
cmd = 'xprctl info'
print("Your Command: " + cmd)

run = Popen(cmd, shell=True, stdout=PIPE)
# out = check_output(cmd, shell=True)
out, err = run.communicate()
print(type(out))
print(out)
print(err)

# pic = open(out, "rb")
# stri = pickle.load(pic)
string = out.decode("utf-8")
print(string)
