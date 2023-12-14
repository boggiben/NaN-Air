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
        return self.data_wrapper.add_staff_to_flight(employee)

    def modify_staff(self, employee):
        return self.data_wrapper.modify_staff(employee)

    def get_all_flights(self):
        pass

    def get_flights_by_week(self):
        pass

    def see_booked_employees(self):
        return self.data_wrapper.see_booked_staff()

    def add_staff_to_flight(self, employee, voyage_date):
        if self.data_wrapperr.is_employee_booked_on_date(
            employee.national_id, voyage_date
        ):
            return False
        return self.data_wrapper.add_staff_to_flight(employee)
