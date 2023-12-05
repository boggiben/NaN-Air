from model.employee import Employee
import csv

class Staff_Logic:
    def __init__(self, data_wrapper):
        self.data_wrapper = data_wrapper

    def add_new_staff(self, employee):
        pass
        
    def see_all_staff(self):
        with open("staff.csv", newline="") as csvfile:
            read = csv.DictReader(csvfile)
            for row in read:
                 print(row["first_name"], row["last_name"])

    def add_new_flight(self, plane, employee):
        pass

    def add_staff_to_flight(self, employee):
        pass

    def get_all_flights(self, ):
        pass

    def get_flights_by_week(self,):
        pass 