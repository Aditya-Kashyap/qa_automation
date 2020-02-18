a = \
    {
        "pipelines":
            {
                "sample_pipeline":
                    {
                        "branch": "master",
                        "description": "build one"
                    }
            }
    }

data2 = a["pipelines"]
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

print(branch)
print(desc)
