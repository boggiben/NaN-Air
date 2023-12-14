class Voyage:
    def __init__(
        self,
        flight_number="",
        departure="",
        arrival="",
        departure_time="",
        arrival_time="",
        aircraft_id="",
        captain="",
        copilot="",
        flight_service_manager="",
        flight_attendant_one="",
        flight_attendant_two="",
        staffed="",
    ):
        self.flight_number = flight_number
        self.departure = departure
        self.arrival = arrival
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.aircraft_id = aircraft_id
        self.captain = captain
        self.copilot = copilot
        self.fsm = flight_service_manager
        self.fa1 = flight_attendant_one
        self.fa2 = flight_attendant_two
        self.staffed = staffed

    def __str__(self):
        return f"Flugnúmer: {self.flight_number}, Flug frá: {self.departure}, Flug til: {self.arrival}, Brottfaratími: {self.departure_time}, Komu tími: {self.arrival_time}, Flugvél: {self.aircraft_id}, Flugstjóri: {self.captain}, Flugmaður: {self.copilot}, Yfirflugþjónn: {self.fsm}, Flugþjónn 1: {self.fa1}, Flugþjónn 2: {self.fa2}"
