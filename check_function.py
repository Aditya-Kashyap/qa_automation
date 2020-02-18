class CheckFunctions:

    @staticmethod
    def check_name(pro_name):
        status = 0
        for j in range(len(pro_name)):
            if pro_name[j].islower() or pro_name[j].isnumeric() or pro_name[j] == '_':
                status = 1
            else:
                status = 0
                break
        return status

    @staticmethod
    def check_user(user):
        status = 0
        sample_user = ["aditya.kashyap", 'reyaz35', 'ASahu2', 'asarkar', 'krishna.kumar']
        for i in range(len(sample_user)):
            if user in sample_user:
                status = 1
            else:
                status = 0
        return status

    @staticmethod
    def check_environments(env):
        status = 0
        env_lib = ["DEV", "INT", "QA", "UAT", "PROD"]
        print(env)
        for i in range(len(env_lib)):
            if env in env_lib:
                status = 1
            else:
                status = 0
        return status

    @staticmethod
    def check_persistent_volume(vol):
        if 10 >= vol > 0:
            return 1
        else:
            return 0

    @staticmethod
    def check_comp_type(comp_type):
        status = 0
        type_lib = ["job", "pipeline_job", "service", "inference_service", "library", "database"]
        for i in range(len(type_lib)):
            if comp_type in type_lib:
                status = 1
            else:
                status = 0
        return status

    @staticmethod
    def check_comp_flavor(comp_flavor):
        status = 0
        flavor_lib = ["java", "python", "sql", "pyspark"]
        for i in range(len(flavor_lib)):
            if comp_flavor in flavor_lib:
                status = 1
            else:
                status = 0
        return status

    @staticmethod
    def check_branch(branch):
        branch_list = ["master", "branch"]
        if branch in branch_list:
            return 1
        else:
            return 0

    @staticmethod
    def check_comp_in_comp_list(comp_list, comps):
        res = 0
        for i in range(len(comps)):
            for j in range(len(comp_list)):
                if comps[i] == comp_list[j]:
                    res = 1
        if res == 1:
            return 1
        else:
            return 0

    @staticmethod
    def project_values(self, name, u_id, env, per_vol):
        # Checking the Project Name
        if name.islower() and name[-1] != '_':
            if self.check_name(name) == 0:
                print("Error in the Name")
                return 0
            else:
                # Checking the Owner
                if self.check_user(u_id) == 0:
                    print("Error in the User ID")
                    return 0
                else:
                    # Checking The Environment
                    if self.check_environments(env) == 0:
                        print("Error in the Environment Specified")
                        return 0
                    else:
                        # Checking the Persistent Volume
                        if self.check_persistent_volume(per_vol) == 0:
                            print("Error in the Persistent Volume")
                            return 0
                        else:
                            return 1
        else:
            print("Error in Project Name: Capital Letter")
            return 0

    @staticmethod
    def components_values(self, name, comp_type, flavor):
        comp_name = self.check_name(name)
        if comp_name == 0:
            print("There is an Error in Name")
            return 0
        comp_type = self.check_comp_type(comp_type)
        if comp_type == 0:
            print("There is an Error in Component Type")
            return 0
        comp_flavour = self.check_comp_flavor(flavor)
        if comp_flavour == 0:
            print("There is an Error is the Component Flavor")
            return 0
        else:
            return 1

    @staticmethod
    def pipeline_name_check(pipe_total, name):
        res = 0
        print(name)
        print(pipe_total)
        for i in range(len(name)):
            for j in range(len(pipe_total)):
                if name[i] == pipe_total[j]:
                    res = 1
        if res == 1:
            return 1
        else:
            return 0

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
