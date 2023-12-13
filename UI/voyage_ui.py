from logic.logic_wrapper import LogicWrapper
from logic.voyage_logic import Voyage_Logic
from model.voyage import Voyage
from datetime import datetime, timedelta


class Voyage_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        print("\n")
        print(f'{"Vinnuferðir":>45}')
        print("*" * 80)
        print("1. Allar vinnuferðir")
        print("2. Skrá vinnuferð")
        print("3. Skoða vinnuferðir á ákveðinni dagsetningu")
        print("4. Skoða vinnuferðir á ákveðinni viku")
        print("b. Fara í aðalvalmynd")
        print("*" * 80)

    def input_voyage_menu(self):
        while True:
            self.menu_output()
            user_input = input("Veldu aðgerð: ")

            if user_input == "1":
                print("Þú valdir að sjá allar vinnuferðir")
                grouped_voyages = self.logic_wrapper.list_all_voyages()
                work_trip_number = 1

                for voyage1, voyage2 in grouped_voyages:
                    print(f"-----\nVinnuferð {work_trip_number}")

                    self.print_voyage_details(voyage1, print_staffed=False)
                    self.print_voyage_details(voyage2)

                    work_trip_number += 1

            elif user_input.lower() == "2":
                print("Þú valdir að skrá vinnuferð")
                success = self.add_new_voyage_ui()
                if success:
                    print("Aðgerð tókst!")

            elif user_input.lower() == "3":
                print("Þú valdir að sjá vinnuferðir út frá dagsetningu")
                voyage_date = input("Dagsetning: (Í sniðinu YYYY-MM-DD) ")

                try:
                    year, month, day = voyage_date.split("-")
                    date = datetime(int(year), int(month), int(day))
                    voyages = self.logic_wrapper.get_voyage_by_date(date)
                    work_trip_number = 1

                    if not voyages:
                        print("\n--------------------")
                        print("Engar vinnuferðir á \nþessum degi")
                        print("--------------------")
                    else:
                        for voyage1, voyage2 in voyages:
                            print(f"-----\nVinnuferð {work_trip_number}")

                            self.print_voyage_details(voyage1, print_staffe0d=False)
                            self.print_voyage_details(voyage1)

                            work_trip_number += 1
                except ValueError:
                    print("Villa. Dagsetning slegin inn í vitlausu sniði.")

            elif user_input.lower() == "4":
                print("Þú valdir að sjá vinnuferðir út frá viku")
                voyage_date = input("Dagsetning: ")
                year, month, day = voyage_date.split("-")
                date = datetime(int(year), int(month), int(day))

                voyages_by_week = self.logic_wrapper.get_voyage_by_week(date)
                work_trip_number = 1

                for voyage1, voyage2 in voyages_by_week:
                    voyage1_departure_time = datetime.strptime(
                        voyage1.departure_time, "%Y-%m-%d %H:%M:%S"
                    )
                    voyage2_departure_time = datetime.strptime(
                        voyage2.departure_time, "%Y-%m-%d %H:%M:%S"
                    )

                    print(f"-----\nVinnuferð {work_trip_number}")
                    # Print voyage details

                    self.print_voyage_details(voyage1, print_staffed=False)
                    self.print_voyage_details(voyage1)

                    work_trip_number += 1

                if work_trip_number == 1:
                    print("Engin vinnuferð í þessari viku")

            elif user_input == "b":
                break

    # def add_new_voyage_ui(self):
    #     voyage1 = Voyage()
    #     voyage2 = Voyage()
    #     flight_number = input("Flugnúmer: ")
    #     new_voyage.flight_number = flight_number
    #     departure = input("Frá: ")
    #     new_voyage.departure = departure
    #     arrival = input("Til: ")
    #     new_voyage.arrival = arrival
    #     departure_time = input("Brottfarartími: ")
    #     new_voyage.departure_time = departure_time
    #     arrival_time = input("Komutími: ")
    #     new_voyage.arrival_time = arrival_time
    #     return self.logic_wrapper.add_new_voyage(new_voyage)

    def add_new_voyage_ui(self):
        """Fall sem er notað til að búa til nýja vinnuferð"""
        voyage1 = Voyage()
        voyage2 = Voyage()

        flight_number = input("Flugnúmer fyrir fyrsta flug: ")
        voyage1.flight_number = flight_number
        voyage1.departure = input("Frá: ")
        # voyage1.departure = departure
        voyage1.arrival = input("Til: ")
        # voyage1.arrival = arrival

        # Ensure departure_time is in the correct format with hours, minutes, and seconds
        while True:
            departure_time_str = input(
                "Brottfarartími (YYYY-MM-DD HH:MM:SS) fyrir fyrsta flug: "
            )
            try:
                departure_time = datetime.strptime(
                    departure_time_str, "%Y-%m-%d %H:%M:%S"
                )
                break
            except ValueError:
                print(
                    "Rangt snið, vinsamlegast sláðu inn dagsetningu og tíma í sniðinu YYYY-MM-DD HH:MM:SS."
                )

        voyage1.departure_time = departure_time

        # Stillum heimferðina, þ.e. voyage2, út frá ferðinni út (voyage1)
        voyage2.flight_number = input("Flugnúmer fyrir heimferð: ")
        voyage2.departure = voyage1.arrival
        voyage2.arrival = voyage1.departure

        # Heimferðin má ekki vera síðar en 10 tímum eftir flugið út.
        max_arrival_time = departure_time + timedelta(hours=10)
        while True:
            arrival_time_str = input(
                f"Komutími (YYYY-MM-DD HH:MM:SS) fyrir heimferðina (ekki seinna en {max_arrival_time}): "
            )
            try:
                arrival_time = datetime.strptime(arrival_time_str, "%Y-%m-%d %H:%M:%S")
                if departure_time <= arrival_time <= max_arrival_time:
                    break
                else:
                    print(
                        f"Tíminn verður að vera á milli {departure_time} og {max_arrival_time}."
                    )
            except ValueError:
                print(
                    "Rangt snið, vinsamlegast sláðu inn dagsetningu í sniðinu YYYY-MM-DD."
                )

        voyage2.departure_time = input(
            "Brottfarartími fyrir heimferð (YYYY-MM-DD HH:MM:SS)"
        )

        # Bættu fluginu út við kerfinu og kannaðu hvort það hafi gengið.
        result1 = self.logic_wrapper.add_new_voyage(voyage1)
        if not result1:
            print("Error adding the first voyage.")
            return False  # Or handle the error as per your system's design

        # Setja heimferðina líka í kerfið.
        result2 = self.logic_wrapper.add_new_voyage(voyage2)
        if not result2:
            print("Error adding the return voyage.")
            return False  # Or handle this error appropriately

        return True  # Or return both results if needed

    def print_voyage_details(self, voyage, print_staffed=True):
        departure_time = datetime.strptime(voyage.departure_time, "%Y-%m-%d %H:%M:%S")
        arrival_time = datetime.strptime(voyage.arrival_time, "%Y-%m-%d %H:%M:%S")

        print(
            f"Flugnúmer: {voyage.flight_number} Frá: {voyage.departure} Til: {voyage.arrival} Brottfarartími: {departure_time}, Komutími: {arrival_time}"
        )

        print(
            f"Flugstjóri: {voyage.captain}, Flugmaður: {voyage.copilot}, Yfirflugþjónn: {voyage.fsm}"
        )
        if print_staffed:
            print(
                "Mönnun:", "Fullmönnuð" if voyage.staffed == "1" else "Ekki fullmönnuð"
            )
