from logic.destination_logic import DestinationLogic
from model.destination import Destination


class Destination_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection
        
    def menu(self):
        print("Áfangastaðir")
        print("1. Stofna nýjan áfangastað")
        print("2. Sjá alla áfangastaði")
        print("b. Til baka")
    
    def input_destination(self):
        while True:
            self.menu()    
            action = input("Veldu aðgerð: ")
            
            
            if action == "1":
                self.create_destination()
            elif action == "2":
                self.see_all_destinations()
            elif action == "b":
                print("Til baka í aðalvalmynd")
                break
            else:
                print("Rangur innsláttur")
                self.menu()