pipeline = {
    "pipeline1": {
        "flavor": "kubeflow"
    },
    "pipeline2": {
        "flavor": "pyspark"
    }
}
kube_pipe = None
spark_pipe = None
for pipe in pipeline.keys():
    val = pipeline[pipe]
    for pipe_comp in val.keys():
        val1 = pipeline[pipe][pipe_comp]
        if val1 == 'kubeflow':
            kube_pipe = pipe
        if val1 == 'pyspark':
            spark_pipe = pipe

print("kubeflow pipeline name: "+kube_pipe)
print("pyspark pipeline name: "+spark_pipe)


