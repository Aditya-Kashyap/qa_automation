import subprocess
from subprocess import *

print("Enter the Number of Test Cases")
num = int(input())

for i in range(num):
    run_cmd = 'xprctl create_project -f test_cases/test_case' + str(i) + '.json'
    run = Popen(run_cmd, stdout=subprocess.PIPE, shell=True)
    return_msg = run.communicate()[0]
    return_code = run.returncode

    if return_code == 0:
        print("Test Case Passed")
    else:
        print("Test Case Failed")
        print(return_msg)
