import json
from check_function import CheckFunctions
# Creating the Object for CheckFunctions
check = CheckFunctions()


class CheckCreateProject:

    @staticmethod
    def check_project_name():

        # Reading the JSON Files:
        print("Enter the Number of Json Files")
        num = input()

        for i in range(int(num)):
            pro = 'test_cases/test_case' + str(i + 1) + '.json'
            with open(pro, 'r') as JsonFile:
                data = json.load(JsonFile)

                # Checking the Project Name
                if data["name"][0].islower():
                    if check.check_name(data["name"]) == 0:
                        return 0
                    else:
                        # Checking the Owner
                        if check.check_user(data["owner"]["uid"]) == 0:
                            return 0
                        else:
                            # Checking The Environment
                            if check.check_environments(data["environments"]) == 0:
                                return 0
                            else:
                                # Checking the Persistent Volume
                                if check.check_persistent_volume(data["persistent_volume_size"]) == 0:
                                    return 0
                                else:
                                    # Iterating for the Number of Components Present
                                    comp = []
                                    if data["components"].len() > 1:
                                        for j in range(len(data["comp"])):
                                            comp_name = check.check_name(data["components"][j]["name"])
                                            comp_type = check.check_comp_type(data["components"][j]["type"])
                                            comp_flavour = check.check_comp_flavor(data["components"][j]["flavor"])
                                            comp = comp + data["components"][j+1]
                                            comp_res = comp_name * comp_flavour * comp_type
                                            if comp_res == 0:
                                                return 0
                                            else:
                                                # Checking for the Pipeline:
                                                pipe_comp = []
                                                if check.check_name(data["pipeline"]["name"]) == 0:
                                                    return 0
                                                else:
                                                    # Checking the Pipeline Components
                                                    if data["pipelines"].len() > 0:
                                                        for k in range(len(data["pipelines"])):
                                                            pipe_comp = pipe_comp + data["pipeline"][k]["name"]
                                                            if data["pipeline"][k]["name"] != comp[k]:
                                                                return 0
                                                            else:
                                                                continue

                                                    elif data["pipelines"].len() == 1:
                                                        if data["pipelines"][0]["name"] != data["components"][0]["name"]:
                                                            return 0
                                                    else:
                                                        pass

                                                    # After Dependencies
                                                    # for k in range(len(data["pipelines"])):
                                                    #     if pipe_comp == data["pipelines"]["after_dependencies"]:
                                                    #         after_dep = 1
                                                    #     else:
                                                    #         after_dep = 0

                                                    print("Hello")
                else:
                    return 0


def main():
    if __name__ == "__main__":
        obj = CheckCreateProject()
        result = obj.check_project_name()
        print(result)


main()
