'''
    Petition API
    ==================

    Create leader content - Petition

'''

from ..requesthandler import RequestHandler

class LeaderPetitions(RequestHandler):

    def __init__(self, token, base_url):
        super(LeaderPetitions, self).__init__(token, base_url)
        self.base_url = self.base_url + "/v2"


    def create(self, gid, data):
        """
        Create an Petition
        """
        r = self.post("/groups/{gid:d}/polls".format(gid=gid), json=data)
        if r.status_code != 201:
            raise Exception( r.json() )
        return r

    def list(self, gid):
        """
        list petitions for the leader
        """
        r = self.get("/groups/{gid:d}/polls".format(gid=gid))
        if r.status_code != 200:
            raise Exception( r.json() )
