from data.staff_data import Staff_Data
from data.destination_data import DestinationData
from data.flight_data import FlightData
from data.voyage_data import Voyage_Data


class DataWrapper:
    def __init__(self):
        self.staff_data = Staff_Data()
        self.destination_data = DestinationData()
        self.flight_data = FlightData()
        self.voyage_data = Voyage_Data()

    def create_staff(self, employee):
        return self.staff_data.create_staff(employee)

    def get_all_staff(self):
        return self.staff_data.read_all_staff()

    def get_all_destinations(self):
        return self.destination_data.get_all_destinations()

    def add_new_destination(self, destination):
        return self.destination_data.add_new_destination(destination)

    def get_all_flights(self):
        return self.flight_data.get_all_flights

    def add_new_flight(self, flight):
        return self.flight_data.add_new_flight(flight)
    
    def get_all_voyages(self):
        return self.voyage_data.read_all_voyages()
    
    def create_voyage(self, voyage):
        return self.voyage_data.create_voyage(voyage)

    def add_staff_to_flight(self, employee):
        return self.staff_data.add_staff_to_flight(employee)