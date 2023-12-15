from data.data_wrapper import DataWrapper
from model.employee import Employee
import csv
from model.voyage import Voyage
from datetime import datetime

file_name = "files/staff.csv"


class Staff_Logic:
    def __init__(self, data_wrapper):
        self.data_wrapper = data_wrapper

    def get_all_staff(self):
        return self.data_wrapper.get_all_staff()

    def get_all_pilots(self):
        return self.data_wrapper.get_all_pilots()

    def get_all_flight_attendants(self):
        return self.data_wrapper.get_all_flight_attendants()

    def get_employee_by_ssn(self, ssn):
        """Fall sem við notum til að fletta starfsmann upp út frá kennitölu."""
        all_employees = self.get_all_staff()

        for emp in all_employees:
            if emp.national_id == ssn:
                return emp

        return None

    def add_new_staff(self, employee):
        return self.data_wrapper.create_staff(employee)

    def add_staff_to_flight(self, employee):
        return self.data_wrapper.add_staff_to_flight(employee)

    def modify_staff(self, employee):
        """Fall sem við notum til að breyta starfsmannaupplýsingum"""
        employees = self.get_all_staff()
        updated = False
        for i, emp in enumerate(employees):
            if emp.national_id == employee.national_id:
                employees[i] = employee
                updated = True
                break

        if updated:
            return self.data_wrapper.write_all_staff(employees)
        else:
            return False

    def see_booked_employees(self):
        return self.data_wrapper.see_booked_staff()