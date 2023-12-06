from data.data_wrapper import DataWrapper
from model.employee import Employee
import csv

file_name = "files/staff.csv"


class Staff_Logic:
    def __init__(self, data_wrapper):
        self.data_wrapper = data_wrapper

    def get_all_staff(self):
        return self.data_wrapper.get_all_staff()

    def get_employee_by_ssn(self, ssn):
        all_employees = self.get_all_staff()

        for emp in all_employees:
            if emp.national_id == ssn:
                return emp

        return None

    def add_new_flight(self, plane, employee):
        pass

    def add_new_staff(self, employee):
        return self.data_wrapper.create_staff(employee)

    def add_staff_to_flight(self, employee):
        pass

    def get_all_flights(self):
        pass

    def get_flights_by_week(self):
        pass
