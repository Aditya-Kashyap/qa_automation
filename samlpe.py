name = ["comp1", "comp2", "comp3", "comp4"]
job = ["job", "job", "pipeline_job", "pipeline_job"]
types = ["python", "java", "python", "java"]

comp_name = ["comp2", "comp3"]
comp_job = []
comp_types = []

for j in range(len(comp_name)):
    for i in range(len(name)):
        if comp_name[j] == name[i]:
            print("Found Ya!")
            comp_job.append(job[i])
            comp_types.append(types[i])

print(comp_job)
print(comp_types)
