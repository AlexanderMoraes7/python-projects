"""Class to manipulate the json file.
    This class there are functions to load the json record, manipulate and save scheduling. 
"""

import json

class Schedule_module:
    def __init__(self):
        self.name_file = "schedule.json"
        
    def load(self):
        try:
            with open(self.name_file, encoding="utf-8") as opened:
                if opened.readline() != '':
                    isFull = True
                else:
                    isFull = False
                    
            with open(self.name_file, encoding="utf-8") as opened:
                if isFull:
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

        if file:
            file[date] = appointments
            with open(self.name_file, "w", encoding="utf-8") as opened:
                json.dump(file, opened, indent=4)
        else:
            file = {date: appointments}
            with open(self.name_file, "w", encoding="utf-8") as opened:
                json.dump(file, opened, indent=4)
