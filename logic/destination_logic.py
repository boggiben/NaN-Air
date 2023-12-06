from model.destination import Destination
from data.data_wrapper import DataWrapper


class DestinationLogic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def add_new_destination(self, destination):
        return self.data_wrapper.add_new_destination(destination)

    def get_all_destinations(self):
        return self.data_wrapper.get_all_destinations()
