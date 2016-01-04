__author__ = 'miholeus'

from flask import Blueprint, request, redirect, render_template, url_for, jsonify
from flask.views import MethodView
# from flask.ext.mongoengine.wtf import model_form
from models import Post

bp = Blueprint('votes', __name__, template_folder='templates')


class ListView(MethodView):
    @staticmethod
    def get():
        return render_template('index/index.html', active_link='/')


class AboutView(MethodView):
    @staticmethod
    def get():
        return render_template('index/about.html', active_link='/about/')


class VoteView(MethodView):
    @staticmethod
    def post():
        # print request
        print request.get_data()
        return jsonify({'status': 'ok'})


# Register the urls
bp.add_url_rule('/', view_func=ListView.as_view('list'))
bp.add_url_rule('/about/', view_func=AboutView.as_view('about'))
bp.add_url_rule('/vote/', view_func=VoteView.as_view('vote'))