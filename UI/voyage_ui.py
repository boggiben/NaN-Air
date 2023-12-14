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
        print("6. Skrá starfsfólk í vinnuferð")
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
                            self.print_voyage_details(voyage2)

                            work_trip_number += 1
                except ValueError:
                    print("Villa. Dagsetning slegin inn í vitlausu sniði.")

            elif user_input.lower() == "4":
                print("Þú valdir að sjá vinnuferðir út frá viku")
                try:
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
                        self.print_voyage_details(voyage2)

                        work_trip_number += 1

                    if work_trip_number == 1:
                        print("Engin vinnuferð í þessari viku")
                except ValueError:
                    print(
                        "Vitlaus innsláttur. Þú slóst mögulega inn dagsetningu í vitlausu sniði"
                    )

            elif user_input.lower() == "5":
                print("Þú valdir að afrita skráningu á vinnuferð")
                duplicate_voyage = input("Veldu vinnuferð sem þú vilt afrita")

            elif user_input.lower() == "6":
                print("Þú valdir að skrá starfsfólk í vinnuferð")
                flight_number = input("Flugnúmer í brottför: ")
                flight_number2 = input("Flugnúmer á heimleið: ")
                flight_check = self.logic_wrapper.check_flight_number(flight_number)
                flight_check2 = self.logic_wrapper.check_flight_number(flight_number2)
                if flight_check and flight_check2 == True:
                    print(f"bæta starfsfólki í flug {flight_number}:")
                    date = input("Dagsetning flugs (YYYY-MM-DD): ")
                    captain = input("kt. Flugstjóra: ")
                    copilot = input("kt. Flugmanns: ")
                    flight_service_manager = input("kt. Yfirflugþjóns: ")
                    flight_attendant_one = input("kt. flugþjóns 1: ")
                    flight_attendant_two = input("kt. flugþjóns 2: ")
                    self.logic_wrapper.add_staff_to_voyage(
                        flight_number, 
                        flight_number2,
                        captain,
                        copilot,
                        flight_service_manager,
                        flight_attendant_one,
                        flight_attendant_two,
                    )
                else:
                    print ("!!!")
                    print ("Flugið er ekki til")

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
        voy1_departure_time_str = input("Brottfarartími (snið: YYYY-MM-DD HH:MM:SS): ")
        voy1_departure_time = datetime.strptime(
            voy1_departure_time_str, "%Y-%m-%d %H:%M:%S"
        )
        voyage1.departure_time = voy1_departure_time

        # Arrival time for voyage1
        voy_1_arrival_time_str = input("Komutími (snið: YYYY-MM-DD HH:MM:SS): ")
        voy_arrival_time = datetime.strptime(
            voy_1_arrival_time_str, "%Y-%m-%d %H:%M:%S"
        )
        voyage1.arrival_time = voy_arrival_time
        voyage1.aircraft_id = input("Aircraft ID fyrir flugið út")

        # Flight crew
        # voyage1.aircraft_id = input("Aircraft ID fyrir fyrsta flug: ")
        # voyage1.captain = input("Flugstjóri:  ")
        # voyage1.copilot = input("Flugmaður í vinnuferðinni: ")
        # voyage1.flight_service_manager = input("Yfirflugþjónn í vinnuferðinni: ")
        # voyage1.flight_attendant_one = input("Flugþjónn 1 í vinnuferðinni: ")
        # voyage1.flight_attendant_two = input("Flugþjónn 2 í vinnuferðinni: ")

        # voyage1.staffed = (
        #     1
        #     if all([voyage1_captain_input, voyage1_copilot_input, voyage1_fsm_input])
        #     else 0
        # )

        # Setting return trip (voyage2) based on the outbound trip (voyage1)
        voyage2.flight_number = input("Flugnúmer fyrir heimferð: ")
        voyage2.departure = voyage1.arrival
        voyage2.arrival = voyage1.departure

        # Setting departure time for voyage2
        voy2_departure_time_str = input("Brottfarartími (snið: YYYY-MM-DD HH:MM:SS): ")
        voy2_departure_time = datetime.strptime(
            voy2_departure_time_str, "%Y-%m-%d %H:%M:%S"
        )
        voyage2.departure_time = voy2_departure_time

        voy2_arrival_time_str = input("Brottfarartími (snið: YYYY-MM-DD HH:MM:SS): ")
        voy2_arrival_time = datetime.strptime(
            voy2_arrival_time_str, "%Y-%m-%d %H:%M:%S"
        )
        voyage2.arrival_time = voy2_arrival_time
        voyage2.aircraft_id = input("Aircraft ID fyrir flugið heim")

        # Additional input for the flight back (voyage2)
        # voyage2.aircraft_id = voyage1.aircraft_id

        # # Essential flight crew
        # voyage2.captain = voyage1.captain
        # voyage2.copilot = voyage1.copilot
        # voyage2.flight_service_manager = voyage1.flight_service_manager
        # # Additional flight crew

        # voyage2.flight_attendant_one = voyage1.flight_attendant_one
        # voyage2.flight_attendant_two = voyage1.flight_attendant_two
        # voyage2.staffed = (
        #     1 if all([voyage2.captain, voyage2.copilot, voyage2.fsm]) else 0
        # )

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
