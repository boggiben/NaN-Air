from model.flight import Flight
from logic.logic_wrapper import LogicWrapper


class FlightUI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def flight_menu(self):
        print("Flugferðir")
        print("1. Sjá allar flugferðir")
        print("b. Til baka")

    def input_flight(
        self,
    ):
        while True:
            self.flight_menu()
            action = input("Veldu aðgerð: ")

            if action == "1":
                all_flights = self.logic_wrapper.get_all_flights()
                self.display_flight(all_flights)

            if action == "b":
                print("Til baka í aðalvalmynd")
                break

    def display_flight(self, all_flights):
        print(f"{'Flugferðir':^100}")
        print("*" * 120)
        print(
            f"{'Flight Number':<20} {'Departing From':<20} {'Arriving at':<20} {'Departure Location':<20} {'Arrival Location':<20}")
        for flight in all_flights:
            print(
                f"{flight.flight_nr:<20} {flight.dep_from:<20} {flight.arr_at:<20} {flight.departure:<20} {flight.arrival:<20}"
            )
        print("*" * 120)
        print()
