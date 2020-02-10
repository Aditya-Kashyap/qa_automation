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
