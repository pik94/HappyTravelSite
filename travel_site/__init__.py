from flask import Flask

from travel_site.views import Departure, Index, Tour

app = Flask(__name__, template_folder='templates')
app.url_map.strict_slashes = False

# index page
app.add_url_rule('/',
                 view_func=Index.as_view(
                     'index', template_name='index.html'))

# departure page
_departure_view = Departure.as_view(
    'departure', template_name='departure.html')
app.add_url_rule('/departure', view_func=_departure_view,
                 defaults={'departure': None})
app.add_url_rule('/departure/<string:departure>',
                 view_func=_departure_view)

# tour page
_tour_view = Tour.as_view('tour', template_name='tour.html')
app.add_url_rule('/tour', view_func=_tour_view,
                 defaults={'tour_number': None})
app.add_url_rule('/tour/<int:tour_number>', view_func=_tour_view)
