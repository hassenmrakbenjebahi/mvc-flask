from flask import Flask
from routes.userRoute import user_bp
from config import Config
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config.from_object(Config)

mongo = PyMongo(app)

app.register_blueprint(user_bp, url_prefix='/users')

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello my friend!'


if __name__ == '__main__':
    app.debug = True
    app.run()
 