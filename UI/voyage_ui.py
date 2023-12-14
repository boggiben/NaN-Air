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
        print("5. Afrita skráningu á vinnuferð")
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

                    self.print_voyage_details(
                        voyage1, print_crew=False, print_staffed=False
                    )
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

                            self.print_voyage_details(
                                voyage1, print_crew=False, print_staffed=False
                            )
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

                    self.print_voyage_details(
                        voyage1, print_crew=False, print_staffed=False
                    )
                    self.print_voyage_details(voyage1)

                    work_trip_number += 1

                if work_trip_number == 1:
                    print("Engin vinnuferð í þessari viku")

            elif user_input.lower() == "5":
                print("Þú valdir að afrita skráningu á vinnuferð")
                duplicate_voyage = input("Veldu vinnuferð sem þú vilt afrita")

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
    #     new_voyage.departure_time = departure_txime
    #     arrival_time = input("Komutími: ")
    #     new_voyage.arrival_time = arrival_time
    #     return self.logic_wrapper.add_new_voyage(new_voyage)

    def input(prompt, default=0):
        """Get input with a default value if blank."""
        value = input(prompt)
        return value if value.strip() else default

    def add_new_voyage_ui(self):
        """Function used to create a new work trip."""
        voyage1 = Voyage()
        voyage2 = Voyage()

        voyage1.flight_number = input("Settu inn flugnúmer: ")
        voyage1.departure = input("Frá: ")
        voyage1.arrival = input("Til: ")

        # Ensuring correct format for departure time
        departure_time_str = input("Brottfarartími (snið: YYYY-MM-DD HH:MM:SS): ")
        departure_time = datetime.strptime(departure_time_str, "%Y-%m-%d %H:%M:%S")
        voyage1.departure_time = departure_time

        # Arrival time for voyage1
        voyage_1_arrival_time = input("Komutími (snið: YYYY-MM-DD HH:MM:SS): ")
        arrival_time = datetime.strptime(voyage_1_arrival_time, "%Y-%m-%d %H:%M:%S")
        voyage1.arrival_time = arrival_time

        # Optional input. Value set to 0 if blank.
        voyage1.aircraft_id = input("Aircraft ID fyrir fyrsta flug: ")
        # voyage1.aircraft_id = voyage1_aircraft_input if voyage1_aircraft_input else "0"
        print(voyage1.aircraft_id)

        voyage1_captain_input = input("Flugstjóri í vinnuferðinni: ").strip()
        voyage1.captain = voyage1_captain_input if voyage1_captain_input else "0"
        print(voyage1.captain)

        voyage1_copilot_input = input("Flugmaður í vinnuferðinni: ").strip()
        voyage1.copilot = voyage1_copilot_input if voyage1_copilot_input else "0"
        print(voyage1.copilot)

        voyage1_fsm_input = input("Yfirflugþjón í vinnuferðinni: ").strip()
        voyage1.flight_service_manager = voyage1_fsm_input if voyage1_fsm_input else "0"
        print(voyage1.flight_service_manager)

        voyage1_fa1_input = input("Flugþjónn í vinnuferðinni: ").strip()
        voyage1.flight_attendant_one = voyage1_fa1_input if voyage1_fa1_input else "0"

        voyage1_fa2_input = input("Flugþjónn í vinnuferðinni: ").strip()
        voyage1.flight_attendant_two = voyage1_fa2_input if voyage1_fa2_input else "0"

        voyage1.staffed = (
            1
            if all([voyage1_captain_input, voyage1_copilot_input, voyage1_fsm_input])
            else 0
        )

        # Setting return trip (voyage2) based on the outbound trip (voyage1)
        voyage2.flight_number = input("Flugnúmer fyrir heimferð: ")
        voyage2.departure = voyage1.arrival
        voyage2.arrival = voyage1.departure

        # Setting departure time for voyage2
        voyage2_departure_time_str = input(
            "Brottfarartími fyrir heimferð (snið YYYY-MM-DD HH:MM:SS): "
        )
        voyage2_departure_time = datetime.strptime(
            voyage2_departure_time_str, "%Y-%m-%d %H:%M:%S"
        )

        arrival_time_str = input("Komutími (snið YYYY-MM-DD HH:MM:SS) fyrir heimferð")

        # Additional input for the flight back (voyage2)
        voyage2.aircraft_id = voyage1.aircraft_id

        # Essential flight crew
        voyage2.captain = voyage1_captain_input if voyage1_captain_input else "0"
        voyage2.copilot = voyage1_copilot_input if voyage1_copilot_input else "0"
        voyage2.flight_service_manager = voyage1_fsm_input if voyage1_fsm_input else "0"

        # Additional flight crew
        voyage2.flight_attendant_one = voyage1_fa1_input if voyage1_fa1_input else "0"
        voyage2.flight_attendant_two = voyage1_fa2_input if voyage1_fa2_input else "0"
        voyage2.staffed = (
            1 if all([voyage2.captain, voyage2.copilot, voyage2.fsm]) else 0
        )

        # Setjum flugið í kerfið og sjáum hvort það hafi virkað
        result1 = self.logic_wrapper.add_new_voyage(voyage1)
        if not result1:
            print("Villa við skráningu á ferðinni út.")
            return False

        result2 = self.logic_wrapper.add_new_voyage(voyage2)
        if not result2:
            print("Villa við skráningu á heimferðinni.")
            return False

        return True

    def print_voyage_details(self, voyage, print_crew=True, print_staffed=True):
        departure_time = datetime.strptime(voyage.departure_time, "%Y-%m-%d %H:%M:%S")
        arrival_time = datetime.strptime(voyage.arrival_time, "%Y-%m-%d %H:%M:%S")

        print(
            f"Flugnúmer: {voyage.flight_number} Frá: {voyage.departure} Til: {voyage.arrival} Brottfarartími: {departure_time}, Komutími: {arrival_time}"
        )

        if print_crew:
            print(
                f"Flugstjóri: {voyage.captain}, Flugmaður: {voyage.copilot}, Yfirflugþjónn: {voyage.fsm}"
            )
        if print_staffed:
            print(
                "Mönnun:", "Fullmönnuð" if voyage.staffed == "1" else "Ekki fullmönnuð"
            )
