
import flask
     
application = flask.Flask(__name__)
     
@application.route('/')
def hello_world():
    return "Hello world! !!!!"
     
if __name__ == '__main__':
    # Switch this to false when deployed
    application.debug=True
    application.run(host='0.0.0.0')

"""
import os
import flask, flask.views
from flask import Markup
from flask import jsonify
import evaluate

application = flask.Flask(__name__)

class Main(flask.views.MethodView):
    def get(self):
        return flask.render_template('index.html')
    
 
class About(flask.views.MethodView):
    def get(self):
        return flask.render_template('about.html')
    
class Contact(flask.views.MethodView):
    def get(self):
        return flask.render_template('contact.html')   

application.add_url_rule('/',view_func=Main.as_view('main'), methods=["GET"])
application.add_url_rule('/about/',view_func=About.as_view('about'), methods=["GET"])
application.add_url_rule('/contact/',view_func=Contact.as_view('contact'), methods=["GET"])


@application.route('/_compute')
def compute():
    sentence = flask.request.args.get('sentence')
    percentage = evaluate.tweetscore(sentence)
    return jsonify(result=percentage)
    
"""
