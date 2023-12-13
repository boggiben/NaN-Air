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

    # def get_voyage_by_date(self, voyage_date):
    #     all_voyages = self.get_all_voyages()
    #     voyages_list = []

    #     for voyage in all_voyages:
    #         date, time = voyage.departure_time.split()
    #         year, month, day = date.split("-")
    #         date = datetime(int(year), int(month), int(day))
    #         # if voyage.departure == voyage_date:
    #         if date == voyage_date:
    #             voyages_list.append(voyage)

    #     return voyages_list

    def get_voyage_by_date(self, voyage_date):
        all_voyages = self.get_all_voyages()
        voyages_for_date = []
        voyages_by_date = set()

        for i, voyage1 in enumerate(all_voyages):
            date1, _ = voyage1.departure_time.split()
            year1, month1, day1 = date1.split("-")
            date1 = datetime(int(year1), int(month1), int(day1))

            if date1 != voyage_date or i in voyages_by_date:
                continue

            for j, voyage2 in enumerate(all_voyages):
                if j in voyages_by_date or i == j:
                    continue

                date2, _ = voyage2.departure_time.split()
                year2, month2, day2 = date2.split("-")
                date2 = datetime(int(year2), int(month2), int(day2))

                if date2 != voyage_date:
                    continue

                if (
                    voyage1.departure == voyage2.arrival
                    and voyage1.arrival == voyage2.departure
                    and date1 == date2
                ):
                    voyages_for_date.append((voyage1, voyage2))
                    voyages_by_date.update([i, j])

        return voyages_for_date

    def get_voyage_by_week(self, voyage_date):
        pass

    def see_booked_employees(self, voyage_date):
        all_voyages = self.get_all_voyages()
        employee_list = []
        # voyage_date = datetime.strptime(voyage_date, '%Y-%m-%d')

        for voy in all_voyages:
            dep_time = datetime.strptime(voy.departure_time, "%Y-%m-%d %H:%M:%S")
            arr_time = datetime.strptime(voy.arrival_time, "%Y-%m-%d %H:%M:%S")
            if (
                voyage_date.date() == dep_time.date()
                or voyage_date.date() == arr_time.date()
            ):
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

    def see_unbooked_employees(self, voyage_date):
        all_voyages = self.get_all_voyages()
        employee_list = []
        # voyage_date = datetime.strptime(voyage_date, '%Y-%m-%d')

        for voy in all_voyages:
            dep_time = datetime.strptime(voy.departure_time, "%Y-%m-%d %H:%M:%S")
            arr_time = datetime.strptime(voy.arrival_time, "%Y-%m-%d %H:%M:%S")
            if (
                voyage_date.date() != dep_time.date()
                or voyage_date.date() != arr_time.date()
            ):
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

    def see_booked_employees_departure(self, voyage_date):
        all_voyages = self.get_all_voyages()
        arrival = ""
        # voyage_date = datetime.strptime(voyage_date, '%Y-%m-%d')

        for voy in all_voyages:
            dep_time = datetime.strptime(voy.departure_time, "%Y-%m-%d %H:%M:%S")
            arr_time = datetime.strptime(voy.arrival_time, "%Y-%m-%d %H:%M:%S")
            if (
                voyage_date.date() == dep_time.date()
                or voyage_date.date() == arr_time.date()
            ):
                arrival = str(voy.arrival)

            return arrival

    def get_voayges_of_employee(self, ssn):
        all_voyages = self.get_all_voyages()
        voyages_that_employee_works_in = []
        for voyage in all_voyages:
            if (
                voyage.captain == ssn
                or voyage.copilot == ssn
                or voyage.fsm == ssn
                or voyage.fa1 == ssn
                or voyage.fa2 == ssn
            ):
                voyages_that_employee_works_in.append(voyage)
        return voyages_that_employee_works_in
