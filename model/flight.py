class Flight:
    def __init__(self, flight_nr="", dep_from="", arr_at="", departure="", arrival=""):
        self.flight_nr = flight_nr
        self.dep_from = dep_from
        self.arr_at = arr_at
        self.departure = departure
        self.arrival = arrival

    def __str__(self):
        return f"Flugnúmer: {self.flight_nr}, Brottför frá: {self.dep_from}, Koma til: {self.arr_at}, Brottför dags.: {self.departure}, Koma dags.: {self.arrival}"
