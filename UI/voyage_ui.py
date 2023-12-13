from logic.logic_wrapper import LogicWrapper
from logic.voyage_logic import Voyage_Logic
from model.voyage import Voyage
from datetime import datetime, timedelta


class Voyage_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        print("\n----Vinnuferðir----")
        print("1. Allar vinnuferðir")
        print("2. Skrá vinnuferð")
        print("3. Skoða vinnuferðir á ákveðinni dagsetningu")
        print("4. Skoða vinnuferðir á ákveðinni viku")
        print("b. Fara í aðalvalmynd")

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
                        f"Flugvél: {elem.aircraft_id:<20} | "
                        f"Flugstjóri: {elem.captain:<20} | "
                        f"Flugmaður: {elem.copilot:<20} | "
                        f"Yfirflugþjónn: {elem.fsm:<20} | "
                        f"Flugþjónn 1: {elem.fa1:<20} | "
                        f"Flugþjónn 2: {elem.fa2:<20} | "
                        f"Fullmönnuð: {elem.staffed:<20} | "
                    )

            elif user_input.lower() == "2":
                print("Þú valdir að skrá vinnuferð")
                success = self.add_new_voyage_ui()
                if success:
                    print("Aðgerð tókst!")

            elif user_input.lower() == "3":
                print("Þú valdir að sjá vinnuferðir út frá dagsetningu")
                voyage_date = input("Dagsetning: ")
                year, month, day = voyage_date.split("-")
                date = datetime(int(year), int(month), int(day))
                voyages = self.logic_wrapper.get_voyage_by_date(date)

                if not voyages:
                    print("Engin vinnuferð á þessum degi")
                else:
                    for voyage in voyages:
                        print("-----")
                        print("Flugnúmer:", voyage.flight_number)
                        print("Frá:", voyage.departure)
                        print("Brottfarartími:", voyage.departure_time)
                        print("Til:", voyage.arrival)
                        print("Komutími:", voyage.arrival_time)
                        if voyage.staffed == "1":
                            print("Mönnun: Fullmönnuð")
                        else:
                            print("Mönnun: Ekki fullmönnuð")

            elif user_input.lower() == "4":
                print("Þú valdir að sjá vinnuferðir út frá viku")
                voyage_date = input("Dagsetning: ")
                year, month, day = voyage_date.split("-")
                date = datetime(int(year), int(month), int(day))
                end_date = date + timedelta(days=7)

                # Teljari til að halda utan um tölu vinnuferða fyrir vikuna
                work_trip_number = 1

                while date <= end_date:
                    voyages = self.logic_wrapper.get_voyage_by_date(date)

                    if not voyages:
                        date += timedelta(days=1)
                        continue

                    # Búum til set til að halda utan um vinnuferðir
                    voyages_by_week = set()

                    for i, voyage1 in enumerate(voyages):
                        if i in voyages_by_week:
                            continue

                        # Breytum departure_time úr streng í datetime format fyrir bæði voyage1 og voyage2
                        voyage1_departure_time = datetime.strptime(
                            voyage1.departure_time, "%Y-%m-%d %H:%M:%S"
                        )

                        for j, voyage2 in enumerate(voyages):
                            if j in voyages_by_week or i == j:
                                continue

                            voyage2_departure_time = datetime.strptime(
                                voyage2.departure_time, "%Y-%m-%d %H:%M:%S"
                            )

                            if (
                                voyage1.departure == voyage2.arrival
                                and voyage1.arrival == voyage2.departure
                                and voyage1_departure_time.date()
                                == voyage2_departure_time.date()
                            ):
                                # Prenta vinnuferðir
                                print(f"-----\nVinnuferð {work_trip_number}")
                                print(
                                    f"Flugnúmer: {voyage1.flight_number} Frá: {voyage1.departure} Til: {voyage1.arrival} Brottfarartími: {voyage1_departure_time}"
                                )
                                print(
                                    f"Flugnúmer: {voyage2.flight_number} Frá: {voyage2.departure} Til: {voyage2.arrival} Brottfarartími: {voyage2_departure_time}"
                                )
                                print(
                                    "Mönnun:",
                                    "Fullmönnuð"
                                    if voyage1.staffed == "1"
                                    else "Ekki fullmönnuð",
                                )

                                work_trip_number += 1
                                voyages_by_week.update([i, j])
                                break

                    date += timedelta(days=1)

                if work_trip_number == 1:
                    print("Engin vinnuferð í þessari viku")

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
