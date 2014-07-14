import flask
 
application = flask.Flask(__name__)

#Set application.debug=true to enable tracebacks on Beanstalk log output. 
#Make sure to remove this line before deploying to production.
application.debug=True
 
@application.route('/')
def hello_world():
    return "Hello world!"
 
if __name__ == '__main__':
    application.run(host='0.0.0.0', debug=True)

"""
import os
import flask, flask.views
from flask import Markup
from flask import jsonify
import evaluate

app = flask.Flask(__name__)

class Main(flask.views.MethodView):
    def get(self):
        return flask.render_template('index.html')
   
class About(flask.views.MethodView):
    def get(self):
        return flask.render_template('about.html')
    
class Contact(flask.views.MethodView):
    def get(self):
        return flask.render_template('contact.html')   


app.add_url_rule('/',view_func=Main.as_view('main'), methods=["GET"])
app.add_url_rule('/about/',view_func=About.as_view('about'), methods=["GET"])
app.add_url_rule('/contact/',view_func=Contact.as_view('contact'), methods=["GET"])


@app.route('/_compute')
def compute():
    sentence = flask.request.args.get('sentence')
    percentage = evaluate.tweetscore(sentence)
    return jsonify(result=percentage)

"""