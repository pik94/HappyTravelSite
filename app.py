from flask import Flask, abort, render_template, redirect, request

from source.data import departures, description, subtitle, title, tours


class TravelSiteApp:
    def __init__(self):
        self._app = Flask(__name__, template_folder='templates')
        self._app.url_map.strict_slashes = False

        self.departures = {}
        for departure_key in sorted(departures):
            self.departures[departure_key] = {
                'link': f'/departure/{departure_key}',
                'text': departures[departure_key]
            }

        self.tours = tours
        for idx, tour in self.tours.items():
            tour['link'] = f'/tour/{idx}'

    def set_pages(self) -> None:
        # index page
        self._app.add_url_rule('/', 'index', self._get_index)

        # departure page
        self._app.add_url_rule('/departure',
                               'departure', self._get_departure,
                               defaults={'departure': None})
        self._app.add_url_rule('/departure/<string:departure>',
                               'departure', self._get_departure)

        # tour page
        self._app.add_url_rule('/tour', 'tour', self._get_tour,
                               defaults={'tour_number': None})
        self._app.add_url_rule('/tour/<int:tour_number>', 'tour',
                               self._get_tour)

    def _render_template(self, html_file: str, **params):
        return render_template(html_file,
                               title=title,
                               departures=self.departures,
                               request=request,
                               **params)

    def _get_index(self) -> str:
        tours = sorted([tour for tour in self.tours.values()],
                       key=lambda item: item['stars'])[:6]
        return self._render_template('index.html',
                                     tours=tours,
                                     subtitle=subtitle,
                                     description=description)

    def _get_departure(self, departure: str) -> str:
        if departure not in self.departures:
            if departure is not None:
                abort(404)
            else:
                return redirect(self.departures['msk']['link'], code=301)

        tours = [tour
                 for tour in self.tours.values()
                 if tour['departure'] == departure]

        return self._render_template('departure.html',
                                     selected_departure=departure,
                                     tours=tours)

    def _get_tour(self, tour_number: int) -> str:
        if tour_number not in self.tours:
            if tour_number is not None:
                abort(404)
            else:
                return redirect(self.tours[1]['link'], code=301)

        return self._render_template('tour.html', tour=self.tours[tour_number])

    def run(self):
        self.set_pages()

        self._app.run(debug=True, host='0.0.0.0', port=8080)


def main():
    app = TravelSiteApp()
    app.run()


if __name__ == '__main__':
    main()
