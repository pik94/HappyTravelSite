from typing import Dict, Union

from travel_site.data import raw_data as rd


class DataStorage:
    def __init__(self):
        self.subtitle = rd.subtitle
        self.title = rd.title
        self.description = rd.description

        self._tours = None
        self._departures = None

    @property
    def tours(self) -> Dict[str, Dict[str, Union[int, str]]]:
        """
        This method get raw tour data and added tour links to them
        :return: prepared data
        """
        if self._tours is None:
            self._tours = rd.tours
            for idx, tour in self.tours.items():
                tour['link'] = f'/tour/{idx}'

        return self._tours

    @property
    def departures(self) -> Dict[str, str]:
        """
        This method added link and text into departures info
        :return: prepared data
        """

        if self._departures is None:
            self._departures = rd.departures
            for departure_key in sorted(rd.departures):
                self._departures[departure_key] = {
                    'link': f'/departure/{departure_key}',
                    'text': rd.departures[departure_key]
                }

        return self._departures
