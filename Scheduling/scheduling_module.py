"""Class to manipulate the json file.
    This class there are functions to load the json record, manipulate and save scheduling. 
"""

import json

class Schedule_module:
    def __init__(self):
        self.name_file = "schedule.json"
        self.count = 0
        # self.load()
        self.data = {
            "Counter" : 0,
            "Record" : [self.load()]
        }

    def load(self):
        try:
            with open(self.name_file, encoding="utf-8") as opened:
                if opened.readline() != '':
                    json_file = json.load(opened)
                    print("Your appointments saved are:")
                    for date, appointments in json_file.items():
                        print(f"{self.count} : {date} |=> {appointments}")
                    print()
                else:
                    return print("No appointments saved yet.\n")
        except FileNotFoundError:
            return None
        else:
            return json_file

    def save(self, date = str, appointments = str):
        file = self.load()

        self.data["Counter"] += 1
        if file:
            file[date] = appointments
            with open(self.name_file, "w", encoding="utf-8") as opened:
                json.dump(file, opened, indent=4)
        else:
            file = {date: appointments}
            with open(self.name_file, "w", encoding="utf-8") as opened:
                json.dump(file, opened, indent=4)

s = Schedule_module()
# arq = s.load()
# print(s.data)

# with open('schedule.json', encoding="utf-8") as opened:
#     # json_file = json.load(opened)
#     if opened.readline() == '':
#         print("Empty")
#     else:
#         print("There are records")