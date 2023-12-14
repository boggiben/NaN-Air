from data.data_wrapper import DataWrapper
from logic.destination_logic import DestinationLogic
from logic.staff_logic import Staff_Logic
from logic.voyage_logic import Voyage_Logic

# from logic.flight_logic import FlightLogic


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

    def list_all_voyages(self):
        return self.voyage_logic.list_all_voyages()

    def add_new_flight(self):
        pass

    def add_staff_to_flight(self, employee):
        return self.staff_logic.add_staff_to_flight(employee)

    def add_new_staff(self, employee):
        return self.staff_logic.add_new_staff(employee)

    def add_new_voyage(self, voyage):
        return self.voyage_logic.add_new_voyage(voyage)

    def get_voyage_by_date(self, voyage_date):
        return self.voyage_logic.get_voyage_by_date(voyage_date)

    def get_voyage_by_week(self, voyage_date):
        return self.voyage_logic.get_voyage_by_week(voyage_date)

    def get_all_destinations(self):
        return self.data_wrapper.get_all_destinations()

    def add_new_destination(self, destination):
        return self.destination_logic.add_new_destination(destination)

    def modify_staff(self, employee):
        return self.staff_logic.modify_staff(employee)

    def see_unbooked_employees(self, voyage_date):
        return self.voyage_logic.see_unbooked_employees(voyage_date)

    def see_booked_employees(self, voyage_date):
        return self.voyage_logic.see_booked_employees(voyage_date)

    def see_booked_employees_departure(self, voyage_date):
        return self.voyage_logic.see_booked_employees_departure(voyage_date)

    def get_voayges_of_employee(self, ssn, start_date_input):
        return self.voyage_logic.get_voayges_of_employee(ssn, start_date_input)

    def see_voyage_plan(self, ssn):
        return self.voyage_logic.see_voyage_plan(ssn)

    def see_booked_employees_name(self, employee):
        return self.voyage_logic.see_booked_employees_name(employee)

    def see_booked_employees_phone(self, employee):
        return self.voyage_logic.see_booked_employees_phone(employee)

    def is_employee_booked_on_date(self, ssn, voyage_date):
        return self.voyage_logic.is_employee_booked_on_date(ssn, voyage_date)

    def add_staff_to_flight(self, employee, voyage_date):
        return self.staff_logic.add_staff_to_flight(employee, voyage_date)

    def add_staff_to_voyage(self, flight_number, flight_number2, captain, copilot, flight_service_manager, flight_attendant_one, flight_attendant_two):
        return self.voyage_logic.add_staff_to_voyage(flight_number, flight_number2, captain, copilot, flight_service_manager, flight_attendant_one, flight_attendant_two)
    
    def check_flight_number(self, flight_number):
        return self.voyage_logic.check_flight_number(flight_number)
    # def change_date(self, new_departure_time, new_arrival_time):
    #     return self.voyage_logic.change_date(self, new_departure_time, new_arrival_time)
