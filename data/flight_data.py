import csv

from model.flight import Flight


class FlightData:
    def __init__(self):
        self.filename = "files/upcoming_flights.csv"

    def get_all_flights(self):
        flight_list = []
        with open(self.filename, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                flight_list.append(
                    Flight(
                        row["flight_nr"],
                        row["dep_from"],
                        row["arr_at"],
                        row["departure"],
                        row["arrival"],
                    )
                )
        return flight_list

    def add_new_flight(self, flight):
        with open(self.filename, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = [
                "flight_nr",
                "dep_from",
                "arr_at",
                "departure",
                "arrival",
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow(
                {
                    "flight_nr": flight.flight_nr,
                    "dep_from": flight.dep_from,
                    "arr_at": flight.arr_at,
                    "departure": flight.departure,
                    "arrival": flight.arrival,
                }
            )
            return True
