from travel_site.data import raw_data as rd


class DataStorage:
    def __init__(self):
        self.subtitle = rd.subtitle
        self.title = rd.title
        self.description = rd.description
        self.departures = rd.departures
        self.tours = rd.tours
