__author__ = 'miholeus'

from flask import Blueprint, request, render_template, jsonify
from flask.views import MethodView
from models import Vote

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
        values = {}
        vote_value = request.form['vote']
        vote = Vote()
        for item in request.form.getlist('value[]'):
            if vote.get_vote_title(item) is not None:
                values[item] = vote.get_vote_title(item)
            elif int(item) == Vote.CUSTOM_VOTE_ID and vote_value:
                values[item] = vote_value
        if values:
            # add vote
            vote.ip = request.remote_addr
            vote.votes = values
            vote.save()
            return jsonify({'status': 'ok'})
        else:
            return jsonify({'status': 'error', 'message': 'Choose any option to vote'})


# Register the urls
bp.add_url_rule('/', view_func=ListView.as_view('list'))
bp.add_url_rule('/about/', view_func=AboutView.as_view('about'))
bp.add_url_rule('/vote/', view_func=VoteView.as_view('vote'))
