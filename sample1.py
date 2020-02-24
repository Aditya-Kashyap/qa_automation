import json


class DeployProject:

    @staticmethod
    def deploy_project(data):

        return 1


with open("test_cases/deploy/test_case2.json", 'r') as JsonFile:
    deploy = json.load(JsonFile)
    obj = DeployProject()
    result = obj.deploy_project(deploy)
    print(result)
