from model.employee import Employee
import csv

file_name = "files/staff.csv"


class Staff_Logic:
    def __init__(self, data_wrapper):
        self.data_wrapper = data_wrapper

    def get_all_staff(self):
        return self.data_wrapper.get_all_staff()

    def add_new_flight(self, plane, employee):
        pass

    def add_new_staff(self, employee):
        return self.data_wrapper.create_staff

    def add_staff_to_flight(self, employee):
        pass

    def get_all_flights(self):
        pass

    def get_flights_by_week(self):
        pass
