class Flight:
    def __init__(self, departure_location="", departure_time="", arrival_location="", arrival_time=""):
        self.departure_location = departure_location
        self.departure_time = departure_time
        self.arrival_location = arrival_location
        self.arrival_time = arrival_time

    def __str__(self):
        return f"departure location: {self.departure_location}, 
        departure time: {self.departure_time}, 
        arrival location: {self.arrival_location}, 
        arrival time: {self.arrival_time}"
