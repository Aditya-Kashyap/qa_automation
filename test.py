import json


with open('test_cases/test_case2.json', 'r') as JsonFile:
    data = json.load(JsonFile)
    name = data["name"]
    if name[0].islower():
        print("Test Case Passed")
    else:

        print("Test Case Failed")
