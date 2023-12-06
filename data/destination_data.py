import csv

from model.destination import Destination


class DestinationData:
    def __init__(self):
        self.filename = "files/destinations.csv"

    def get_all_destinations(self):
        destination_list = []
        with open(self.filename, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                destination_list.append(
                    Destination(
                        row["country"],
                        row["airport"],
                        row["flight_duration"],
                        row["distance"],
                        row["contact_name"],
                        row["contact_number"],
                    )
                )
        return destination_list

    def add_new_destination(self, destination):
        with open(self.filename, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = [
                "country",
                "airport",
                "flight_duration",
                "distance",
                "contact_name",
                "contact_number",
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow(
                {
                    "country": destination.country,
                    "airport": destination.airport,
                    "flight_duration": destination.flight_duration,
                    "distance": destination.distance,
                    "contact_name": destination.contact_name,
                    "contact_number": destination.contact_number,
                }
            )
            return True
