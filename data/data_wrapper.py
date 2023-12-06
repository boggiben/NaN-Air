from data.staff_data import Staff_Data
from data.destination_data import DestinationData


class DataWrapper:
    def __init__(self):
        self.staff_data = Staff_Data()
        self.destination_data = DestinationData()

    def create_staff(self, employee):
        self.staff_data.create_staff(employee)

    def get_all_staff(self):
        return self.staff_data.read_all_staff()

    def get_all_destinations(self):
        return self.destination_data.get_all_destinations()

    def add_new_destination(self, destination):
        return self.destination_data.add_new_destination(destination)
