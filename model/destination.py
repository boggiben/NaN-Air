class Destination:
    def __init__(
        self,
        destination="",
        country="",
        airport="",
        flight_duration="",
        distance="",
        contact_name="",
        contact_number="",
    ):
        self.destination = destination
        self.country = country
        self.airport = airport
        self.flight_duration = flight_duration
        self.distance = distance
        self.contact_name = contact_name
        self.contact_number = contact_number

    def __str__(self):
        return f"destination: {self.destination}, national id: {self.country}, airport: {self.airport}, flight duration: {self.flight_duration}, distance: {self.distance}, contact name: {self.contact_name}, contact number: {self.contact_number}"
