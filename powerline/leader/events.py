'''
    Events API
    ==================

    Create leader content - Event

'''

from ..requesthandler import RequestHandler

class LeaderEvents(RequestHandler):

    def __init__(self, token, base_url):
        super(LeaderEvents, self).__init__(token, base_url)
        self.base_url = self.base_url + "/v2"


    def create(self, gid, data):
        """
        Create an event
        """
        r = self.post("/groups/{gid:d}/polls".format(gid=gid), json=data)
        if r.status_code != 201:
            raise Exception( r.json() )
        return r
