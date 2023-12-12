from data.data_wrapper import DataWrapper
from model.voyage import Voyage
import csv
from datetime import datetime

file_name = "files/past_flights.csv"


class Voyage_Logic:
    def __init__(self, data_wrapper):
        self.data_wrapper = data_wrapper

    def create_voyage(self, voyage):
        """Takes in a voyage object and forwards it to the data layer"""

        self.data_wrapper.create_voyage(voyage)

    def get_all_voyages(self):
        return self.data_wrapper.get_all_voyages()

    def add_new_voyage(self, voyage):
        return self.data_wrapper.create_voyage(voyage)

    def get_voyage_by_date(self, voyage_date):
        all_voyages = self.get_all_voyages()
        voyages_list = []

        for voyage in all_voyages:
            date, time = voyage.departure_time.split()
            year, month, day = date.split("-")
            date = datetime(int(year), int(month), int(day))
            # if voyage.departure == voyage_date:
            if date == voyage_date:
                voyages_list.append(voyage)

        return voyages_list
    

    def see_booked_employees(self, voyage_date):
        all_voyages = self.get_all_voyages()
        employee_list = []
        # voyage_date = datetime.strptime(voyage_date, '%Y-%m-%d')
        
        for voy in all_voyages:
            dep_time = datetime.strptime(voy.departure_time, '%Y-%m-%d %H:%M:%S')
            arr_time = datetime.strptime(voy.arrival_time, '%Y-%m-%d %H:%M:%S')
            if voyage_date.date() == dep_time.date() or voyage_date.date() == arr_time.date():
                employee_list.append(voy.captain)
                employee_list.append(voy.copilot)
                employee_list.append(voy.fsm)
                #
                if voy.fa1 != "":
                    employee_list.append(voy.fa1)
                if voy.fa2 != "":
                    employee_list.append(voy.fa2)
        unique_list = list(set(employee_list))

        return unique_list
