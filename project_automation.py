
from check_function import CheckFunctions

# Creating the Object for CheckFunctions
check = CheckFunctions()


class CreateProject:

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
            print("After Dependencies Component is not present in the Pipeline Components")
            return 0


