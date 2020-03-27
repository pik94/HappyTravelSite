from flask import Flask

from travel_site.views import Departure, Index, Tour

app = Flask(__name__, template_folder='templates')
app.url_map.strict_slashes = False

# index page
app.add_url_rule('/',
                 view_func=Index.as_view(
                     'index', template_name='index.html'))

# departure page
# app.add_url_rule('/departure',
#                  view_func=Departure.as_view(
#                      'departure', template_name='departure.html'),
#                  defaults={'departure': None})
app.add_url_rule('/departure/<string:departure>',
                 view_func=Departure.as_view(
                     'departure', template_name='departure.html'))

# tour page
# app.add_url_rule('/tour',
#                  view_func=Tour.as_view(
#                      'tour', template_name='tour.html'),
#                  defaults={'tour_number': None})
app.add_url_rule('/tour/<int:tour_number>', 'tour',
                 view_func=Tour.as_view('tour', template_name='tour.html'))
