data = {
    "components": {
        "service_reader": {
            "branch": "master",
            "description": "trial version - 1"
        },
        "database_service": {
            "branch": "master",
            "description": "trial version - 2"
        },
        "crawler_service": {
            "branch": "master",
            "description": "trial version - 3"
        },
        "ds_service_taxi": {
            "branch": "develop",
            "description": "trial version - 4",
            "xpresso_dependencies": ["lib_crawler"]
        }
    }
}

list_val = []

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
    print("branch = " + branch)
    print("desc = " + desc)
    print(xp_dep)

