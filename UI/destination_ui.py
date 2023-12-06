from logic.destination_logic import DestinationLogic
from model.destination import Destination
from logic.logic_wrapper import LogicWrapper


class Destination_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def destination_menu(self):
        print("Áfangastaðir")
        print("1. Stofna nýjan áfangastað")
        print("2. Sjá alla áfangastaði")
        print("b. Til baka")

    def input_destination(self):
        while True:
            self.destination_menu()
            action = input("Veldu aðgerð: ")

            if action == "1":
                success = self.add_new_destination_ui()
                if success:
                    print("Aðgerð tókst!")
            elif action == "2":
                all_destinations = self.logic_wrapper.get_all_destinations()
                self.display_destinations(all_destinations)
            elif action == "b":
                print("Til baka í aðalvalmynd")
                break
            else:
                print("Rangur innsláttur")
                self.destination_menu()

    def display_destinations(self, destinations):
        for dest in destinations:
            print(dest)

    def add_new_destination_ui(self):
        new_destination = Destination()
        country = input("Land: ")
        new_destination.country = country
        airport = input("Flugvöllur: ")
        new_destination.airport = airport
        duration = input("Flugtími: ")
        new_destination.flight_duration = duration
        distance = input("Fjarlægð: ")
        new_destination.distance = distance
        contact = input("Nafn tengiliðs: ")
        new_destination.contact_name = contact
        number = input("Neyðarnúmer tengiliðs: ")
        new_destination.contact_number = number
        return self.logic_wrapper.add_new_destination(new_destination)
