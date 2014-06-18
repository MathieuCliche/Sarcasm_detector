#from app import app

import flask

app = flask.Flask(__name__)



class Main(flask.views.MethodView):
    def get(self):
        return "Hello world"

app.add_url_rule('/',view_func=Main.as_view('main'), methods=["GET"])

app.debug = False
app.run()