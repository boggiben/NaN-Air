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
                    print("*"*30)
                    print("Aðgerð tókst!")
                    print("*"*30)
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
        print(f"{'Áfangastaðir':>60}")
        print(f"{'Country':<20} {'Airport':<20} {'Flight Duration':<20} {'Flight Distance km':<20} {'Contact Name':<20} {'Contact Number':<20}")
        for dest in destinations:           
            print(f"{dest.country:<20} {dest.airport:<20} {dest.flight_duration:<20} {dest.distance:<20} {dest.contact_name:<20} {dest.contact_number:<20}")
            

    def add_new_destination_ui(self):
        destination_list = []
        country = input("Land: ")
        destination_list.append(country)
        airport = input("Flugvöllur: ")
        destination_list.append(airport)
        duration = input("Flugtími: ")
        destination_list.append(duration)
        distance = input("Fjarlægð: ")
        destination_list.append(distance)
        contact = input("Nafn tengiliðs: ")
        destination_list.append(contact)
        number = input("Neyðarnúmer tengiliðs: ")
        destination_list.append(number)
        self.logic_wrapper.add_new_destination(destination_list)
