__author__ = 'miholeus'

from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from flask.ext.mongoengine.wtf import model_form
from models import Post

posts = Blueprint('posts', __name__, template_folder='templates')


class ListView(MethodView):

    @staticmethod
    def get():
        return render_template('index/index.html', active_link='/')


class AboutView(MethodView):

    @staticmethod
    def get():
        return render_template('index/about.html', active_link='/about/')

# Register the urls
posts.add_url_rule('/', view_func=ListView.as_view('list'))
posts.add_url_rule('/about/', view_func=AboutView.as_view('about'))