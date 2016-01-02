__author__ = 'miholeus'

from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from flask.ext.mongoengine.wtf import model_form
from models import Post

posts = Blueprint('posts', __name__, template_folder='templates')


class ListView(MethodView):

    @staticmethod
    def get():
        items = Post.objects
        return render_template('posts/list.html', posts=items)


# Register the urls
posts.add_url_rule('/', view_func=ListView.as_view('list'))
posts.add_url_rule('/<slug>/', view_func=ListView.as_view('detail'))