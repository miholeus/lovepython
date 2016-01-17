# coding: utf-8
__author__ = 'miholeus'

from flask import Blueprint, request, render_template, jsonify
from flask.views import MethodView
from models import Vote
import datetime

bp = Blueprint('votes', __name__, template_folder='templates')


def total_voted_last_month():
    """
    Get total number of people voted for last 31 days
    :return: int
    """
    return len(Vote.objects(created_at__gte=(datetime.datetime.now() - datetime.timedelta(days=31))))


class ListView(MethodView):
    @staticmethod
    def get():
        return render_template('index/index.html', active_link='/', total=total_voted_last_month())


class AboutView(MethodView):
    @staticmethod
    def get():
        return render_template('index/about.html', active_link='/about/', total=total_voted_last_month())


class VoteView(MethodView):
    @staticmethod
    def ordinal(n):
        if 10 <= n % 100 < 20:
            return str(n) + 'th'
        else:
            return str(n) + {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, "th")
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
            try:
                vote_current = Vote.objects(ip=request.remote_addr,
                                            created_at__gte=(datetime.datetime.now() - datetime.timedelta(minutes=15)))
                if vote_current:
                    raise ValueError("You've already voted!")
                vote.save()
                suffix = VoteView.ordinal(len(Vote.objects))

                return jsonify({'status': 'ok',
                                'message': 'Thank your for voting! You are the %s fan of python' % suffix})
            except ValueError as e:
                return jsonify({'status': 'error', 'message': e.message})
            except Exception:
                return jsonify({'status': 'error', 'message': 'Error while saving vote. Sorry :('})
        else:
            return jsonify({'status': 'error', 'message': 'Choose any option to vote'})


# Register the urls
bp.add_url_rule('/', view_func=ListView.as_view('list'))
bp.add_url_rule('/about/', view_func=AboutView.as_view('about'))
bp.add_url_rule('/vote/', view_func=VoteView.as_view('vote'))
