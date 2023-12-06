from model.employee import Employee
import csv

class Staff_Logic:
    def __init__(self, data_wrapper):
        self.data_wrapper = data_wrapper
        self.file_name = "files/staff.csv"

    def add_new_staff(self, employee):
        pass
        
    def see_all_staff(self):
        staff_list = []
        with open(self.file_name, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                staff_list.append(Employee(row["Nafn"], row["Netfang"]))
        return staff_list

    def add_new_flight(self, plane, employee):
        pass

    def add_staff_to_flight(self, employee):
        pass

    def get_all_flights(self, ):
        pass

    def get_flights_by_week(self,):
        pass 