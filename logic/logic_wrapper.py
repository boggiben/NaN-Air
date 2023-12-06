from data.data_wrapper import DataWrapper
from logic.destination_logic import DestinationLogic
from logic.staff_logic import Staff_Logic


class LogicWrapper:
    def __init__(self):
        self.data_wrapper = DataWrapper()
        self.staff_logic = Staff_Logic(self.data_wrapper)
        self.destination_logic = DestinationLogic(self.data_wrapper)

    def get_all_flights(self):
        pass

    def get_flights_by_week(self):
        pass

    def get_all_staff(self):
        self.staff_logic.see_all_staff()

    def add_new_flight(self):
        pass

    def add_staff_to_flight(self):
        pass

    def add_new_staff(self):
        pass

    def get_all_destinations(self):
        return self.data_wrapper.get_all_destinations()

    def add_new_destination(self, destination: list):
        self.destination = destination
        return self.data_wrapper.add_new_destination
