__author__ = 'miholeus'

import datetime
from flask import url_for
from src import db


class Vote(db.Document):
    CUSTOM_VOTE_ID = 6
    voteFields = {1: 'Easy to read', 2: 'Easy to use', 3: 'Internet of things opportunities',
                  4: 'Asynchronous coding benefits', 5: 'Multiparadigm approach bests Java'}

    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    ip = db.StringField(max_length=15, required=True)
    votes = db.DictField(required=True)

    def get_absolute_url(self):
        return url_for('post', kwargs={"slug": self.slug})

    def __unicode__(self):
        return self.title

    def get_vote_title(self, vote_id):
        """
        Get title by identifier
        :type vote_id: int
        """
        vote_id = int(vote_id)
        return self.voteFields[vote_id] if vote_id in self.voteFields.keys() else None

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at', 'ip'],
        'ordering': ['-created_at']
    }
