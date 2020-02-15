from check_function import CheckFunctions

# Creating the Object for CheckFunctions
check = CheckFunctions()


class BuildProject:

    @staticmethod
    def build_project(data, comp_lib):
        # Checking the Name of the Project
        name = check.check_name(data["name"])
        if name == 0:
            return 0
        else:
            # Checking the Number of Components
            comp_list = []
            for i in range(len(data["components"])):
                comp_list.append(data["components"][i])

            che = check.check_comp_in_comp_list(comp_lib, comp_list)
            if che == 0:
                return 0
            else:
                for i in range(len(data["components"])):
                    branch = check.check_branch(data["components"][i]["branch"])
                    if branch == 0:
                        return 0
                    else:
                        # Checking if Description is not Empty
                        if data["components"][i].get("description") is None:
                            return 0

                        else:
                            # Checking the Xpresso Dependencies:
                            if data["components"][i].get("xpresso_dependencies") is None:
                                return 0
                            else:
                                # Checking the Pipeline
                                # Checking if the Pipeline is present or not:
                                if data.get("pipelines") is None:
                                    return 1
                                else:
                                    for j in range(len(data["pipelines"])):
                                        pipe_name = check.check_name(data["pipelines"][j]["name"])
                                        if pipe_name == 0:
                                            return 0
                                        else:
                                            pipe_branch = check.check_branch(data["pipelines"][j]["branch"])
                                            if pipe_branch == 0:
                                                return 0
                                            else:
                                                if data["pipelines"][j].get(["description"]) is None:
                                                    return 0
                                                else:
                                                    return 1
