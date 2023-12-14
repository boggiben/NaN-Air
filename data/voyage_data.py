import csv
from model.voyage import Voyage

# from model.staff import Staff


class Voyage_Data:
    def __init__(self):
        self.file_name = "files/past_flights.csv"

    def create_voyage(self, voyage):
        with open(self.file_name, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = [
                "flight_number",
                "departure",
                "arrival",
                "departure_time",
                "arrival_time",
                "aircraft_id",
                "captain",
                "copilot",
                "fsm",
                "fa1",
                "fa2",
                "staffed",
                # Add other necessary fields if they are part of the Voyage object
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow(
                {
                    "flight_number": voyage.flight_number,
                    "departure": voyage.departure,
                    "arrival": voyage.arrival,
                    "departure_time": voyage.departure_time,
                    "arrival_time": voyage.arrival_time,
                    "aircraft_id": voyage.aircraft_id,
                    "captain": voyage.captain,
                    "copilot": voyage.copilot,
                    "fsm": voyage.flight_service_manager,
                    "fa1": voyage.flight_attendant_one,
                    "fa2": voyage.flight_attendant_two,
                    "staffed": voyage.staffed,
                    # Add other necessary fields if they are part of the Voyage object
                }
            )
            return True

    def read_all_voyages(self):
        voyage_list = []
        with open(
            self.file_name, mode="r", newline="", encoding="utf-8-sig"
        ) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                voyage_list.append(
                    Voyage(
                        row["flight_number"],
                        row["departure"],
                        row["arrival"],
                        row["departure_time"],
                        row["arrival_time"],
                        row["aircraft_id"],
                        row["captain"],
                        row["copilot"],
                        row["fsm"],
                        row["fa1"],
                        row["fa2"],
                        row["staffed"],
                    )
                )
        return voyage_list

    def add_staff_to_flight(self, voyage):
        with open(self.file_name, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["captain" "copilot" "fsm" "fa1" "fa2"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow(
                {
                    "captain": voyage.captain,
                    "copilot": voyage.copilot,
                    "fsm": voyage.fsm,
                    "fa1": voyage.fsm,
                    "fa2": voyage.fa2,
                }
            )
            return True

    # def read_all_customers(self):
    #     ret_list = []
    #     with open(self.file_name, newline='', encoding="utf-8") as csvfile:
    #         reader = csv.DictReader(csvfile)
    #         for row in reader:
    #             ret_list.append(Customer(row["name"], row["birth_year"]))
    #     return ret_list
