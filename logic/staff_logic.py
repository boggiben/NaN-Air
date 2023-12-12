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

    # def see_available_employees(self, voyage_date):
    #     all_voyages = self.get_all_voyages()
    #     employee_list = []

    #     for captain,copilot,fsm,fa1,fa2 in all_voyages:
    #         date, time = captain,copilot,fsm,fa1,fa2.departure_time.split()
    #         year, month, day = date.split("-")
    #         date = datetime(int(year), int(month), int(day))
    #         if date == voyage_date:
    #             employee_list.append(captain,copilot,fsm,fa1,fa2)

    #     return employee_list