import scheduling_module

class Schedule:
    """Principal Class"""
    def __init__(self):
        self.oSchedule = scheduling_module.Schedule_module()
        print("Schedule your appointments")
        while True:
            option = input("Enter:\n0: to go out\n1: to save a new appointment\n2: to load all appointments\n")
            if option == "0":
                break
            elif option == "1":
                self.add()
            elif option == "2":
                self.oSchedule.load()
            else:
                print("Option not accepted, enter again\n\n")
                continue

    def delete(self):
        pass

    def add(self):
        date = input("\nEnter with the date of your appointment(MM/DD/YYYY): ")
        appoint = input("Enter your appointment: ")
        self.oSchedule.save(date, appoint)
        print(f"Appointment for {date} was saved successfully\n")

s = Schedule()
