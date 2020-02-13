from subprocess import *
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
                print("Error in the Name")
                return 0
            else:
                # Checking the Owner
                if check.check_user(u_id) == 0:
                    print("Error in the User ID")
                    return 0
                else:
                    # Checking The Environment
                    if check.check_environments(env) == 0:
                        print("Error in the Environment Specified")
                        return 0
                    else:
                        # Checking the Persistent Volume
                        if check.check_persistent_volume(per_vol) == 0:
                            print("Error in the Persistent Volume")
                            return 0
                        else:
                            return 1
        else:
            print("Error in Project Name: Capital Letter")
            return 0

    @staticmethod
    def components_values(name, comp_type, flavor):
        comp_name = check.check_name(name)
        if comp_name == 0:
            print("There is an Error in Name")
            return 0
        comp_type = check.check_comp_type(comp_type)
        if comp_type == 0:
            print("There is an Error in Component Type")
            return 0
        comp_flavour = check.check_comp_flavor(flavor)
        if comp_flavour == 0:
            print("There is an Error is the Component Flavor")
            return 0
        else:
            return 1

    @staticmethod
    def pipeline_name_check(name):
        if check.check_name(name) == 0:
            print("There is an Error in the Pipeline Name")
            return 0
        else:
            return 1

    @staticmethod
    def pipeline_comp_check(comp, comp_total):
        # pipe_comp_type = ["job", "pipeline_job"]
        found = 0
        # found_comp = 0
        # found_type = 0

        if set(comp).issubset(comp_total):
            found = 1
        # if set(pipe_type).issubset(pipe_comp_type):
        #     found_type = 1
        #     print("Type Found")
        # found = found_comp * found_type
        if found == 0:
            print("Pipeline Component is not present in the Main Components")
            return 0
        else:
            return 1

    @staticmethod
    def after_dependencies(comp_pipe, comp):
        found = 0
        print(comp)
        print(comp_pipe)
        if set(comp).issubset(comp_pipe):
            found = 1
        if found == 1:
            return 1
        else:
            print("After Dependencies is not present in the Pipeline Components")
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
            comp_type = []
            comp_flavor = []
            if len(data["components"]) > 0:
                for j in range(len(data["components"])):

                    # Checking for the Component in PySpark:
                    if data["components"][j]["type"] == "pipeline_job" and data["components"][j]["flavor"] == "pyspark":
                        return 0

                    # Sending the Values of Components for Checking:
                    compo = obj.components_values(data["components"][j]["name"], data["components"][j]["type"],
                                                  data["components"][j]["flavor"])

                    # Taking a List of all the Total Name,Type and Flavor of Components in a List
                    comp.append(data["components"][j]["name"])
                    comp_type.append(data["components"][j]["type"])
                    comp_flavor.append(data["components"][j]["flavor"])

                # print(comp)
                # print(comp_type)
                # print(comp_flavor)

                if compo == 0:
                    return 0
                else:
                    # print("Components are OK")
                    # Now checking about the Pipeline:
                    # At First checking the Number of Pipeline Components:
                    # Pipeline can be present or cannot be!
                    if data.get("pipelines") is None:  # Checking if Pipeline is present or not
                        # print("Pipeline Not Present")
                        return 1
                    else:
                        result_comp = 0
                        # Looping in the Total Number of Pipeline Components
                        for k in range(len(data["pipelines"])):
                            # Checking the Pipeline Name
                            pipe_name = obj.pipeline_name_check(data["pipelines"][k]["name"])
                            # print("Pipeline Name OK")
                            flv = []
                            typ = []
                            # Checking the flavor of the component:
                            for comp_len in range(len(data["pipelines"][k]["components"])):
                                for comp_length in range(len(comp)):
                                    if data["pipelines"][k]["components"][comp_len] == comp[comp_length]:
                                        flv.append(comp_flavor[comp_length])
                                        typ.append(comp_type[comp_length])
                            print(flv)
                            print(typ)
                            # Sending the Components for the Validation
                            pipe_comp = obj.pipeline_comp_check(data["pipelines"][k]["components"], comp)
                            print(pipe_comp)
                            # Checking for the After Dependencies
                            aft_dep = obj.after_dependencies(data["pipelines"][k]["components"],
                                                             data["pipelines"][k]["after_dependencies"])

                            comp_res = pipe_comp * pipe_name * aft_dep
                            print(comp_res)
                            if comp_res == 0:
                                return 0
                            else:
                                result_comp = 1

                        if result_comp == 1:
                            print("Successfully Parsed")
                            return 1

            # Checking if the Length of Components is of Only 1
            elif len(data["components"]) == 1:
                # Checking the Pipeline for only one component
                pipe_name = obj.pipeline_name_check(data["pipelines"][0]["name"])
                pipe_comp = obj.pipeline_comp_check(data["pipelines"][0]["components"], comp)
                comp_res = pipe_comp * pipe_name
                return comp_res

            else:
                # No Components is Present
                return 1


if __name__ == "__main__":
    print("Enter the Number of Json Files")
    num = input()
    wrong = None
    right = None
    # for i in range(int(num)):
    #     result = main(i)
    #     print(result)
    result = main(3)
    # if result == 0:
    #     wrong = 0
    #     right = 1
    # else:
    #     right = 0
    #     wrong = 1
    #
    # print("Truth Table")
    # print("|---- Wrong Input ----|---- Right Input ----|--Test Case Pass/Fail--|")
    # print("|------- Program------|------- XPRCTL ------| ------- ------ ------ |")
    # print("|----Pass--|--Fail----|----Pass--|--Fail----|                       |")
    # print("|    " + str(wrong) + "     |     " + str(right) + "    |")

    if result == 1:
        for no in range(int(num)):
            # command_string = 'xprctl create_project -f test_cases/test_case' + str(no + 1) + '.json'
            command_string = 'xprctl info'
            create = Popen(command_string, shell=True)
            create.wait()
