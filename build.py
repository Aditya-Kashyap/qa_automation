from check_function import CheckFunctions
from create import CreateProject

create_obj = CreateProject()
# Creating the Object for CheckFunctions
check = CheckFunctions()


class BuildProject:

    @staticmethod
    def build_project(data):
        # Checking the Name of the Project
        name = check.check_name(data["name"])
        if name == 0:
            print("Failed in Name")
            return 0
        else:
            # Taking all the components from the Create Project Files:
            comp_lib = create_obj.get_comp()
            # comp_flavor = create_obj.get_comp_flavor()
            # comp_type = create_obj.get_comp_type()

            # Taking a list of all the Build Components:
            comp_list = list(data["components"].keys())

            print(comp_lib)
            print(comp_list)

            # Now Checking weather the Build Components are Present in the Create Project:
            che = check.check_comp_in_comp_list(comp_lib, comp_list)
            if che == 0:
                print("Failed in Component Check")
                return 0
            else:
                data1 = data["components"]
                name = data1.keys()
                branch = ""
                desc = ""
                xp_dep = ""
                for comp in name:
                    val = data1[comp]
                    for comp_name in val.keys():
                        val2 = data1[comp][comp_name]
                        if comp_name == 'branch':
                            branch = val2
                        if comp_name == 'description':
                            desc = val2
                        if comp_name == 'xpresso_dependencies':
                            xp_dep = val2
                    # print("branch = " + branch)
                    # print("desc = " + desc)
                    # print(xp_dep)

                    branch = check.check_branch(branch)
                    if branch == 0:
                        print("Failed in Branch")
                        return 0
                    else:
                        # Checking if Description is not Empty
                        if desc == "":
                            print("Failed in Description")
                            return 0
                        else:
                            # Checking the Xpresso Dependencies:
                            if xp_dep == "":
                                print("No Xpresso Dependencies")
                                pass
                            else:
                                pass

            # Checking the Pipeline
            # Checking if the Pipeline is present or not:
            if data.get("pipelines") is None:
                return 1
            else:
                # Checking the Total Pipelines
                pipe_total = create_obj.get_pipelines()
                # Taking out all the name of Pipeline in the Build Json
                names_pipe = list(data["pipelines"].keys())
                # Sending the name to check weather it is present in the Create Project or Not:
                pipe_name = check.pipeline_name_check(pipe_total, names_pipe)
                if pipe_name == 0:
                    print("Failed in Pipeline Name: NOt Present in Create Project")
                    return 0
                else:
                    # Now iterating to the Pipeline Components
                    data2 = data["pipelines"]
                    print(data2)

                    branch = ""
                    desc = ""
                    for pipe in data2.keys():
                        val = data2[pipe]
                        for pipe_comp in val.keys():
                            val1 = data2[pipe][pipe_comp]
                            if pipe_comp == 'branch':
                                branch = val1
                            if pipe_comp == 'description':
                                desc = val1

                    pipe_branch = check.check_branch(branch)
                    if pipe_branch == 0:
                        print("Failed in Pipeline Branch")
                        return 0
                    else:
                        if desc == "":
                            print("Failed in Pipeline Description")
                            return 0
                        else:
                            print("Successfully Parsed")
                            return 1
