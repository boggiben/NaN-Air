class Flight:
    def __init__(self, flight_nr="", dep_from="", arr_at="", departure="", arrival=""):
        self.flight_nr = flight_nr
        self.dep_from = dep_from
        self.arr_at = arr_at
        self.departure = departure
        self.arrival = arrival

    def __str__(self):
        return f"Flight number: {self.flight_nr}, departing from: {self.dep_from}, arriving at: {self.arr_at}, departure location: {self.departure}, arrival location: {self.arrival}"
