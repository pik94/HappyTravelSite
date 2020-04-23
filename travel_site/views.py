from flask import abort, redirect, render_template, request, url_for
from flask.views import View

from travel_site.data import data_storage


class Index(View):
    def __init__(self, template_name: str):
        self._template_name = template_name

    def dispatch_request(self) -> str:
        tours = sorted(data_storage.tours.items(),
                       key=lambda item: item[1]['stars'],
                       reverse=True)[:6]
        return _render_template(self._template_name,
                                tours=dict(tours),
                                subtitle=data_storage.subtitle,
                                description=data_storage.description)


class Departure(View):
    def __init__(self, template_name: str):
        self._template_name = template_name

    def dispatch_request(self, departure: str) -> str:
        if departure not in data_storage.departures:
            if departure is not None:
                abort(404)
            else:
                return redirect(url_for('departure', departure='msk'),
                                code=301)

        tours = {tour_id: tour
                 for tour_id, tour in data_storage.tours.items()
                 if tour['departure'] == departure}

        return _render_template(self._template_name,
                                departure=departure,
                                tours=tours)


class Tour(View):
    def __init__(self, template_name: str):
        self._template_name = template_name

    def dispatch_request(self, tour_number: int) -> str:
        if tour_number not in data_storage.tours:
            if tour_number is not None:
                abort(404)
            else:
                return redirect(url_for('tour', tour_number=1),
                                code=301)

        return _render_template(self._template_name,
                                tour=data_storage.tours[tour_number])


def _render_template(html_file: str, **params) -> str:
    return render_template(html_file,
                           title=data_storage.title,
                           departures=data_storage.departures,
                           request=request,
                           **params)
