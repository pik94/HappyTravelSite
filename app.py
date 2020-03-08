from flask import Flask, render_template


class TravelSiteApp:
    def __init__(self):
        self._app = Flask(__name__, template_folder='templates')

    def set_pages(self) -> None:
        self._app.add_url_rule('/', 'index', self._get_index)
        self._app.add_url_rule('/departure/', 'departure', self._get_departure)
        self._app.add_url_rule('/tour/', 'tour', self._get_tour)

    def _get_index(self) -> str:
        return render_template('index.html')

    def _get_departure(self) -> str:
        return render_template('departure.html')

    def _get_tour(self) -> str:
        return render_template('tour.html')

    def run(self):
        self.set_pages()

        self._app.run(debug=True)


def main():
    app = TravelSiteApp()
    app.run()


if __name__ == '__main__':
    main()
