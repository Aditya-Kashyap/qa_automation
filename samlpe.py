a = \
    {
        "pipelines":
            {
                "dnn_training_pipeline":
                    {
                        "components": {
                            "data_fetch": {
                                "mount_path": "/data",
                                "custom_docker_image": "dockerregistrysb.xpresso.ai/library/xpresso_version:2.0.0",
                                "command": ["python", "app.py"],
                                "args": [
                                    "data_pull",
                                    "-in",
                                    {
                                        "inputValue": "inpath"
                                    },
                                    "-out",
                                    {
                                        "inputValue": "outpath"
                                    },
                                    "-r",
                                    {
                                        "inputValue": "repo_name"
                                    },
                                    "-b",
                                    {
                                        "inputValue": "branch_name"
                                    },
                                    "-c",
                                    {
                                        "inputValue": "commit"
                                    },
                                    "--type",
                                    "files",
                                    "-env",
                                    "sandbox"
                                ]
                            },
                            "dnn_data_prep": {
                                "build_version": 1,
                                "mount_path": "/data",
                                "command": [],
                                "args": []
                            },
                            "dnn_train": {
                                "build_version": 1,
                                "mount_path": "/data",
                                "command": [],
                                "args": [
                                    {
                                        "inputValue": "xpresso_run_name"
                                    },
                                    {
                                        "inputValue": "batch_size"
                                    },
                                    {
                                        "inputValue": "train_epochs"
                                    }
                                ]
                            }
                        }
                    }
            }
    }

data = a["pipelines"]
pipe_name = list(data.keys())
print(pipe_name)

# Looping through the Pipeline
for pipe in data.keys():
    val = data[pipe]
    print("Components of Pipeline")
    print(val)

    data2 = val.keys()

    for pipe_comp in data2:
        val1 = data[pipe][pipe_comp]
        print(val1)
        print("The Name of all the Components in the Pipeline")
        comp_name = list(val1.keys())
        

