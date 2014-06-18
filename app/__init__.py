import flask, flask.views
from flask import Markup
from flask import jsonify

app = flask.Flask(__name__)

app.secret_key = 'bacon'


class Main(flask.views.MethodView):
    def get(self):
        return flask.render_template('index.html')

    
@app.route('/_compute')
def compute():
    a = flask.request.args.get('a')
    return jsonify(result='Score = '+str(5)+a+' %')
    
class About(flask.views.MethodView):
    def get(self):
        return flask.render_template('about.html')
    
class Contact(flask.views.MethodView):
    def get(self):
        return flask.render_template('contact.html')
    


app.add_url_rule('/',view_func=Main.as_view('main'), methods=["GET"])
app.add_url_rule('/about/',view_func=About.as_view('about'), methods=["GET"])
app.add_url_rule('/contact/',view_func=Contact.as_view('contact'), methods=["GET"])

app.debug = True
app.run()