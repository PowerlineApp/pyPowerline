'''

    Poll API
    =========

    Poll access for leaders

    Entities:
        [ Polls | Events | Fundraisers | Discussions | Petitions ]

    Note:
        Given the evolution of the product, Poll actually encapsulates not only
        itself but all entities listed above. We will eventually break this up
        into individual endpoints. For now, how the data object is presented
        to Polls endpoint will determine how the API considers the data a
        poll, event, etc.

    Entity Definitions:

        Polls:
        Events:
        Fundraisers:
        Discussions:
        Petitions:

'''
from powerline.requesthandler import RequestHandler

class Polls(RequestHandler):

    def __init__(self, token, base_url):
        super(Polls, self).__init__(token, base_url)


    def list(self, gid):
        """
        List all Polls and sub classes for the group

        Note:
            This will include all types including events, peitions, etc

        """
        r = self.get("/groups/{gid:d}/polls")
        return r.json()

    def create(self, data):
        """
        Create a poll
        """


