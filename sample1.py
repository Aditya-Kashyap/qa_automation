import json


class DeployProject:

    @staticmethod
    def deploy_project(data1):
        data = data1["pipelines"]
        for i in range(len(data)):
            i
        return 1


class GetProject:

    @staticmethod
    def get_project(data):
        pass


# Opening the Get Project:
with open("test_cases/deploy/get_project.json", 'r') as JsonFile:
    get_pro = json.load(JsonFile)
    get_obj = GetProject()
    get_obj.get_project(get_pro)


# Opening the Deploy Json File
with open("test_cases/deploy/test_case2.json", 'r') as JsonFile:
    deploy = json.load(JsonFile)
    obj = DeployProject()
    result = obj.deploy_project(deploy)
    print(result)


