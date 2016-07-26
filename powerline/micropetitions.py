'''
    Micro-Petitions API
    ==================

    Micro-petition access for standard user

'''

from powerline.requesthandler import RequestHandler

class Micropetitions(RequestHandler):

    def __init__(self, token, base_url):
        super(Micropetitions, self).__init__(token, base_url)


    def create(self, gid, data):
        """"
        Create a micro-petition

        Data Fields:
            petition_body       ::=  Body
            title               ::=  Title
            link                ::=
            is_outsiders_sign   ::=  allow non-group members to sign
            type                ::=  [ quorum | long-petition ]

        Description:
            quorum        ::=  A user post with up/down option
            long-petition ::=  A user petition with sign option

        """
        r = self.post("/groups/{gid:d}/micro-petitions".format(gid=gid),
            json=data )
        return r.json()

    def delete(self, id):
        """
        Delete a micro-petition
        """
        r = self.delete("/mciro-petitions/{id:d}".format(id=id) )
        return r.json()

    def get(self, id):
        """
        Get micropetition
        """
        r = self.get("/micro-petitions/{id:d}".format(id=id) )
        return r.json()

    def list(self):
        """
        Get all micropetitions
        """
        r = self.get("/micro-petitions")
        return r.json()

    def update(self, id):
        """
        Update a micro-petition
        """
        pass

    def delete_answer(self, id):
        """
        Delete a micro-petitions answer
        """
        pass

    def create_answer(self, id):
        """
        Answer a micro-petition
        """
        pass
