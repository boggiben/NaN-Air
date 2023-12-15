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
                print("Þú valdir að afrita skráningu á vinnuferð (Óklárað)")
                voyage1 = input("Veldu flugnúmer á brottfararflugi sem þú vilt endurtaka: ")
                voyage2 = input("Veldu flugnúmer á heimkomuflugi sem þú vilt endurtaka: ")
                new_date = input("Dagsetning endurtakningar(YYYY-MM-DD): ")
                self.logic_wrapper.duplicate_voyage(voyage1, new_date)
                self.logic_wrapper.duplicate_voyage(voyage2, new_date)
                

            elif user_input.lower() == "6":
                result = self.modify_voyage_ui()

            elif user_input == "b":
                break

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
        voy1_date_input = input("Sláðu inn dagsetningu (í sniðinu YYYY-MM-DD): ")
        voy1_time_input = input("Sláðu inn brottafartíma (í sniðnu HH:MM:SS)")
        voy1_departure_time_str = voy1_date_input + " " + voy1_time_input
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
        voyage1.aircraft_id = input("Aircraft ID fyrir flugið út: ")

        # Flight crew
        voyage1.captain = input("Flugstjóri:  ")
        voyage1.copilot = input("Flugmaður í vinnuferðinni: ")
        voyage1.flight_service_manager = input("Yfirflugþjónn í vinnuferðinni: ")
        voyage1.flight_attendant_one = input("Flugþjónn 1 í vinnuferðinni: ")
        voyage1.flight_attendant_two = input("Flugþjónn 2 í vinnuferðinni: ")
        voyage1.staffed = input("1 ef flugið er mannað, 0 ef flugið er ómannað")

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

        voy2_arrival_time_str = input("Komutími (snið: YYYY-MM-DD HH:MM:SS): ")
        voy2_arrival_time = datetime.strptime(
            voy2_arrival_time_str, "%Y-%m-%d %H:%M:%S"
        )
        voyage2.arrival_time = voy2_arrival_time
        voyage2.aircraft_id = voyage1.aircraft_id

        # Additional input for the flight back (voyage2)
        # # Essential flight crew
        voyage2.captain = voyage1.captain
        voyage2.copilot = voyage1.copilot
        voyage2.flight_service_manager = voyage1.flight_service_manager
        # # Additional flight crew

        voyage2.flight_attendant_one = voyage1.flight_attendant_one
        voyage2.flight_attendant_two = voyage1.flight_attendant_two
        voyage2.staffed = voyage1.staffed


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
            

    def modify_voyage_ui(self):
        voyage1_flight_number = input("Skrá flugnúmer brottfarar til að breytinga vinnuferð: ")
        voyage2_flight_number = input("Skrá flugnúmer heim til að breytinga vinnuferð: ")
        voyage_date = input("Dagsetning flugs (YYYY-MM-DD): ")
        year, month, day = voyage_date.split("-")
        date = datetime(int(year), int(month), int(day))

        voyage1 = self.logic_wrapper.check_flight_number(voyage1_flight_number)
        voyage2 = self.logic_wrapper.check_flight_number(voyage2_flight_number)
        
        if voyage1 is None or voyage2 is None:
            print("Enginn vinnuferð er með þetta flugnúmer")
            return

        print("Upplýsingar um flugstjóra, flugmann, yfirflugþjón, flugþjón 1 og flugþjón 2 verða uppfærðar fyrir báðar ferðir.")
        print(f"Núverandi upplýsingar fyrir fyrri ferð: {voyage1}")
        print(f"Núverandi upplýsingar fyrir seinni ferð: {voyage2}")
        while True:
            new_captain = input("Nýr flugstjóri: ") or voyage1.captain
            booked_staff = self.logic_wrapper.see_booked_employees(date)
            if new_captain in booked_staff:
                print("starfsmaður er nú þegar bókaður")
            else:
                break
        while True:
            new_copilot = input("Nýr flugmaður: ") or voyage1.copilot
            booked_staff = self.logic_wrapper.see_booked_employees(date)
            if new_copilot in booked_staff:
                print("starfsmaður er nú þegar bókaður")
            else:
                break
        while True:
            new_flight_service_manager = input("Nýr yfirflugþjónn: ") or voyage1.fsm
            booked_staff = self.logic_wrapper.see_booked_employees(date)
            if new_flight_service_manager in booked_staff:
                print("starfsmaður er nú þegar bókaður")
            else:
                break
        while True:
            new_fa1 = input("Nýr flugþjónn 1: ") or voyage1.fa1
            booked_staff = self.logic_wrapper.see_booked_employees(date)
            if new_fa1 in booked_staff:
                print("starfsmaður er nú þegar bókaður")
            else:
                break
        while True:
            new_fa2 = input("Nýr flugþjónn 2: ") or voyage1.fa2
            booked_staff = self.logic_wrapper.see_booked_employees(date)
            if new_fa2 in booked_staff:
                print("starfsmaður er nú þegar bókaður")
            else:
                break
        new_staffed = input("Er vinnuferðin mönnuð? '1' = JÁ, '0' = NEI: ")

        if self.logic_wrapper.combine_flights_voyage(voyage1_flight_number, voyage2_flight_number, new_captain, new_copilot, new_flight_service_manager, new_fa1, new_fa2, new_staffed):
            print("Upplýsingar fyrir vinnuferð uppfærðar.")
        else:
            print("Uppfærsla á upplýsingum mistókst!")