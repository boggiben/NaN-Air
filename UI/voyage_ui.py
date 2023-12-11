from logic.logic_wrapper import LogicWrapper
from logic.voyage_logic import Voyage_Logic
from model.voyage import Voyage
from datetime import datetime


class Voyage_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        print("\n----Vinnuferðir----")
        print("1. Allar vinnuferðir")
        print("2. Skrá vinnuferð")
        print("3. Sjá vinnuferðir út frá dagsetningu (og skoða mönnun)")
        print("b. Til að fara í aðalvalmynd")

    def input_voyage_menu(self):
        while True:
            self.menu_output()
            user_input = input("Veldu aðgerð: ")
            if user_input == "1":
                print("Þú valdir að sjá allar vinnuferðir")
                result = self.logic_wrapper.get_all_voyages()

                for elem in result:
                    print(
                        f"Flugnúmer: {elem.flight_number:<10} | "
                        f"Frá: {elem.departure:<10} | "
                        f"Til: {elem.arrival:<20} | "
                        f"Brottfarartími: {elem.departure_time:<20} | "
                        f"Komutími: {elem.arrival_time:<20} | "
                        f"Flugvél: {elem.arrival_time:<20} | "
                        f"Flugstjóri: {elem.captain:<20} | "
                        f"Flugmaður: {elem.copilot:<20} | "
                        f"Yfirflugþjónn: {elem.fsm:<20} | "
                        f"Flugþjónn 1: {elem.fa1:<20} | "
                        f"Flugþjónn 2: {elem.fa2:<20} | "
                    )

            elif user_input.lower() == "2":
                print("Þú valdir að skrá vinnuferð")
                success = self.add_new_voyage_ui()
                if success:
                    print("Aðgerð tókst!")

            elif user_input.lower() == "3":
                print("Þú valdir að sjá vinnuferðir út frá dagsetningu")
                voyage_date = input("dagsetning: ")

                try:
                    # Validate date format
                    valid_date = datetime.strptime(voyage_date, "%Y-%m-%d %H:%M:%S")
                    voyage = self.logic_wrapper.get_voyage_by_date(voyage_date)

                    if voyage is None:
                        print("Engin vinnuferð á þessum degi")
                    else:
                        print("Flugnúmer:", voyage.flight_number)
                        print("Brottfarartími:", voyage.departure)
                except ValueError:
                    print("Rangur innsláttur. Reyndu aftur.")

            elif user_input.lower() == "b":
                break

            else:
                print("Rangur innsláttur. Reyndu aftur.")

    def add_new_voyage_ui(self):
        new_voyage = Voyage()
        flight_number = input("Flugnúmer: ")
        new_voyage.flight_number = flight_number
        departure = input("Frá: ")
        new_voyage.departure = departure
        arrival = input("Til: ")
        new_voyage.arrival = arrival
        departure_time = input("Brottfarartími: ")
        new_voyage.departure_time = departure_time
        arrival_time = input("Komutími: ")
        new_voyage.arrival_time = arrival_time
        return self.logic_wrapper.add_new_voyage(new_voyage)
