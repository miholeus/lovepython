__author__ = 'miholeus'

from flask import Flask
from flask.ext.mongoengine import MongoEngine


def register_blueprints(app):
    # Prevents circular imports
    from src.views import posts
    app.register_blueprint(posts)

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {"DB" : "python"}
app.config['SECRET_KEY'] = 'MY_S3CR3T_KEY'

db = MongoEngine(app)

register_blueprints(app)

if __name__ == '__main__':
    app.run()
