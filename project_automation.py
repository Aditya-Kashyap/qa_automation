import json
from check_function import CheckFunctions
# Creating the Object for CheckFunctions
check = CheckFunctions()


class ProjectAutomation:

    @staticmethod
    def project_values(name, u_id, env, per_vol):
        # Checking the Project Name
        if name.islower() and name[-1] != '_':
            if check.check_name(name) == 0:
                return 0
            else:
                # Checking the Owner
                if check.check_user(u_id) == 0:
                    return 0
                else:
                    # Checking The Environment
                    if check.check_environments(env) == 0:
                        return 0
                    else:
                        # Checking the Persistent Volume
                        if check.check_persistent_volume(per_vol) == 0:
                            return 0
                        else:
                            return 1
        else:
            return 0

    @staticmethod
    def components_values(name, comp_type, flavor):
        comp_name = check.check_name(name)
        comp_type = check.check_comp_type(comp_type)
        comp_flavour = check.check_comp_flavor(flavor)
        comp_res = comp_name * comp_flavour * comp_type
        print(comp_res)
        return comp_res

    @staticmethod
    def pipeline_name_check(name):
        res = check.check_name(name)
        return res

    @staticmethod
    def pipeline_comp_check(comp_total, comp):
        found = 0
        for comp_no in range(len(comp_total)):
            if comp_total[comp_no] == comp:
                found = 1
        if found == 1:
            return 1
        else:
            return 0

    @staticmethod
    def after_dependencies(comp_pipe, comp):
        found = 0
        for comp_no in range(len(comp_pipe)):
            if comp == comp_pipe[comp_no]:
                found = 1
        if found == 1:
            return 1
        else:
            return 0


# Defining the main driver program
def main(js):
    # Reading the JSON Files:
    pro = 'test_cases/test_case' + str(js + 1) + '.json'
    with open(pro, 'r') as JsonFile:
        data = json.load(JsonFile)

        # Defining the Object the class
        obj = ProjectAutomation()

        # Calling the Project Values
        pro_val = obj.project_values(data["name"], data["owner"]["uid"], data["environments"],
                                     data["persistent_volume_size"])

        if pro_val == 0:
            return 0
        else:
            # Calling the Component Values
            # Iterating for the Number of Components Present
            # If no components are present then exiting with return code 1
            comp = []
            res = 1
            if len(data["components"]) > 0:
                for j in range(len(data["components"])):
                    compo = obj.components_values(data["components"][j]["name"], data["components"][j]["type"],
                                                  data["components"][j]["flavor"])
                    comp.append(data["components"][j]["name"])
                    res = res * compo

                if res == 0:
                    return 0
                else:
                    # # Checking for the Pipeline
                    # pipe_comp = []
                    # for k in range(len(data["pipelines"])):
                    #     pipe_name = obj.pipeline_name_check
                    #     if pipe_name == 0:
                    #         return 0
                    #     pipe_comp = pipe_comp + data["pipeline"][k]["name"]
                    #
                    # # Checking the Components
                    # for n in range(len(data["pipelines"])):
                    #     res_pipe = obj.pipeline_comp_check(comp, data["pipelines"][n]["components"])
                    #     if res_pipe == 0:
                    #         return 0
                    #
                    # # Checking the After Dependencies:
                    # for m in range(len(data["pipelines"])):
                    #     aft_dep = obj.after_dependencies(pipe_comp, data["pipelines"][m]["after_dependencies"])
                    #     if aft_dep == 0:
                    #         return 0
                    #     else:
                    #         return 1
                    print(comp)
                    return 1

            else:
                return 1


if __name__ == "__main__":
    # print("Enter the Number of Json Files")
    # num = input()

    # for i in range(int(num)):
    #     result = main(i)
    #     print(result)
    result = main(3)
    print(result)
