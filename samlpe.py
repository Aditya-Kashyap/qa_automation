import json


class HelloWorld:
    def __init__(self):
        pro = 'test_cases/create/test_case4.json'
        with open(pro, 'r') as JsonFile:
            data = json.load(JsonFile)
            self.print_json(data)

    @staticmethod
    def print_json(data):
        print(data["name"])
        for i in range(2):
            print("Helli")
        for i in range(2):
            print("World")


def main():
    HelloWorld()


if __name__ == '__main__':
    main()
