class Flight:
    def __init__(self, flight_nr="", dep_from="", arr_at="", departure="", arrival=""):
        self.flight_nr = flight_nr
        self.depa_from = dep_from
        self.arr_at = arr_at
        self.departure = departure
        self.arrival = arrival

    def __str__(self):
        return f"departure location: {self.departure_location}, departure time: {self.departure_time}, arrival location: {self.arrival_location}, arrival time: {self.arrival_time}"
