from model.employee import Employee
import csv

file_name = "files/staff.csv"


class Staff_Logic:
    def __init__(self, data_wrapper):
        self.data_wrapper = data_wrapper

    def see_all_staff(self):
        staff_list = []
        with open(file_name, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                staff_list.append(Employee)

        return staff_list

    def add_new_flight(self, plane, employee):
        pass

    def add_new_staff(self, employee):
        with open(file_name, newline="") as csvfile:
            fieldnames = [
                "Nafn",
                "Símanúmer",
                "Netfang",
                "Heimilisfang",
                "kennitala",
                "Staða",
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    def add_staff_to_flight(self, employee):
        pass

    def get_all_flights(
        self,
    ):
        pass

    def get_flights_by_week(
        self,
    ):
        pass
