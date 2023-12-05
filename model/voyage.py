class Voyage:
    def __init__(
        self,
        destination="",
        departure_date="",
        departure_time="",
        return_date="",
        return_time="",
        crew_captain="",
        crew_pilot="",
        crew_cabin_manager="",
        crew_flight_attendant="",
    ):
        self.destination = destination
        self.departure_date = departure_date
        self.departure_time = departure_time
        self.return_date = return_date
        self.return_time = return_time
        self.crew_captain = crew_captain
        self.crew_pilot = crew_pilot
        self.cabin_manager = cabin_manager
        self.flight_attendant = flight_attendant

    def __str__(self):
        return f"destination: {self.destination}, 
        departure date: {self.departure_date}, 
        departure time: {self.departure_time}, 
        return date: {self.return_date}, 
        return time: {self.return_time}, 
        crew captain: {self.crew_captain}, 
        crew pilot: {self.crew_pilot}, 
        cabin manager: {self.cabin_manager}, 
        flight attendant: {self.flight_attendant}"
