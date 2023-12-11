from data.data_wrapper import DataWrapper
from logic.destination_logic import DestinationLogic
from logic.staff_logic import Staff_Logic

# from logic.flight_logic import FlightLogic
from logic.voyage_logic import Voyage_Logic


class LogicWrapper:
    def __init__(self):
        self.data_wrapper = DataWrapper()
        self.staff_logic = Staff_Logic(self.data_wrapper)
        self.destination_logic = DestinationLogic(self.data_wrapper)
        # self.flight_logic = FlightLogic(self.data_wrapper)
        self.voyage_logic = Voyage_Logic(self.data_wrapper)

    def get_employee_by_ssn(self, ssn):
        return self.staff_logic.get_employee_by_ssn(ssn)

    def get_all_flights(self):
        return self.data_wrapper.get_all_flights()

    def get_flights_by_week(self):
        pass

    def get_all_staff(self):
        return self.staff_logic.get_all_staff()

    def get_all_pilots(self):
        return self.staff_logic.get_all_pilots()

    def get_all_flight_attendants(self):
        return self.staff_logic.get_all_flight_attendants()

    def get_all_voyages(self):
        return self.voyage_logic.get_all_voyages()

    def add_new_flight(self):
        pass

    def add_staff_to_flight(self, employee):
        return self.staff_logic.add_staff_to_flight(employee)

    def add_new_staff(self, employee):
        return self.staff_logic.add_new_staff(employee)

    def add_new_voyage(self, voyage):
        return self.voyage_logic.add_new_voyage(voyage)

    def get_all_destinations(self):
        return self.data_wrapper.get_all_destinations()

    def add_new_destination(self, destination):
        return self.destination_logic.add_new_destination(destination)

    def modify_staff(self, employee):
        return self.staff_logic.modify_staff(employee)
