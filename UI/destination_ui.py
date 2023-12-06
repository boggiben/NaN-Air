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
                # self.logic_wrapper.add_new_destination()
                self.create_destination_ui()
            elif action == "2":
                self.logic_wrapper.get_all_destinations()
            elif action == "b":
                print("Til baka í aðalvalmynd")
                break
            else:
                print("Rangur innsláttur")
                self.destination_menumenu()

    def create_destination_ui(self):
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
