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
