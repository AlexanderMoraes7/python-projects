import json
import os

class Convertion():
    def __init__(self) -> None:
        self.path = input("Enter the path of json to converto to csv: ")
        self.name_path = ''
        self.name = ''
        self.sep = ','
        self.json2csv(self.path)

    @staticmethod
    def remove_double_quotes(path) -> str:
        if path[0] == "\"":
            path = path[1:]
        if path[-1] == "\"":
            path = path[:-1]
        return path

    def json2csv(self, path = str, sep = ","):
        """path is on your file is,
            sep is the separator by default is ",",
            you can put anything how separator
        """
        try:
            header = []
            self.path = self.remove_double_quotes(path)
            self.name_path = os.path.basename(self.path)    # Get only name.exe
            self.name_path = self.name_path.split(".")      # Split and convert to a list
            self.name = self.name_path[0]                   # Get the index zero that is the name of path without .json
            self.sep = sep
            with open(self.path, 'r') as opened:            # Open the file
                data = json.loads(opened.read())

            for key in data[0]:                             # Get the header or the key
                header.append(key)

            result = sep.join(*[data[0]])+"\n"

            for obj in data:
                for value in header:
                    if value == header[-1]:                 # Validation to see if is the end of the file
                        result += f"\"{obj[value]}\""
                    else:
                        result += f"\"{obj[value]}\"{sep}"  # if not is the end, insert without separator
                else:
                    result += "\n"

            with open(self.name+".csv", "w") as opened:
                opened.write(result)

            print("File created!")

        except Exception as ex:
            print(f"Error: {str(ex)}")

Convertion()