from model.destination import Destination
from logic.logic_wrapper import LogicWrapper


class Destination_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def destination_menu(self):
        print("\n")
        print(f'{"Áfangastaðir":>45}')
        print("*" * 80)
        print("1. Stofna nýjan áfangastað")
        print("2. Sjá alla áfangastaði")
        print("b. Til baka")
        print("*" * 80)

    def input_destination(self):
        while True:
            self.destination_menu()
            action = input("Veldu aðgerð: ")

            if action == "1":
                success = self.add_new_destination_ui()
                if success:
                    print("*" * 30)
                    print("Aðgerð tókst!")
                    print("*" * 30)
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
        print(f"{'Áfangastaðir':^120}")
        print("*" * 120)
        print(
            f"{'Land':<20} {'Flugvöllur':<20} {'Flugtími':<20} {'Fjarlægð km':<20} {'Tengiliður':<20} {'Númer tengiliðs':<20}"
        )
        for dest in destinations:
            print(
                f"{dest.country:<20} {dest.airport:<20} {dest.flight_duration:<20} {dest.distance:<20} {dest.contact_name:<20} {dest.contact_number:<20}"
            )
        print("*" * 120)
        print()

    def add_new_destination_ui(self):
        new_destination = Destination()
        country = input("Land: ")
        new_destination.country = country
        airport = input("Flugvöllur: ")
        new_destination.airport = airport
        duration = input("Flugtími klst:mín: ")
        new_destination.flight_duration = duration
        distance = input("Fjarlægð í km: ")
        new_destination.distance = distance
        contact = input("Nafn tengiliðs: ")
        new_destination.contact_name = contact
        number = input("Neyðarnúmer tengiliðs: ")
        new_destination.contact_number = number
        return self.logic_wrapper.add_new_destination(new_destination)
