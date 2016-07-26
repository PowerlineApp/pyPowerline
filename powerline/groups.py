'''

    Groups API
    =========

    Group access for standard user

'''

from requesthandler import RequestHandler

class Groups(RequestHandler):


    def __init__(self, token, base_url):
        super(Groups, self).__init__(token, base_url, use_v2=True)


    def create(self, data):
        """
        Create a group
        """
        # TODO:
        #   Validate group data is complete

        validate = {
            'required' : {},
            'optional' : {}
        }

        r = self.post("/user/groups", json=data )
        return r


    def join(self, gid, group_fields=None):
        """
        Join a group

        Group fields may be necessary to join. See def required_fields

        Return {
            "status"    : True | False
            "message"   : Error message of False
        }
        """
        kwargs = {}
        if group_fields:
            kwargs['data'] = group_fields
        r = self.put("/user/groups/{gid:d}".format(gid=gid), **kwargs )
        if r.status_code == 204:
            return { "status" : True, "message" : ""}
        return { "status" : False, "message" : r.json() }


    def unjoin(self, gid):
        """
        Unjoin a group
        """
        r = self.delete("/groups/join/{gid:d}".format(gid=gid))
        return r.json()


    def info(self, gid):
        """
        Get group info
        """
        if not gid:
            raise Exception("Group id must be given")
        r = self.get("/groups/{gid:d}".format(gid=gid))
        return r.json()


    def users(self, gid):
        """
        A group's users
        """
        r = self.get("/groups/{g:d}/users".format(g=gid))
        return r.json()

    def invite_approvals(self, status, gid):
        """
        group invite status
        """
        statuses = ["reject", "approve" ]
        if status not in statuses:
            raise Exception("Unknown status request for invites")
        r = self.post("/groups/invites/{s:s}/{g:d}".format(s=status, g=gid))
        print r

    def required_fields(self, gid):
        """
        A group's required fields
        """
        r = self.get("/groups/{g:d}/fields".format(g=gid))
        return r.json()

    def invites(self, gid):
        """
        A group's invites
        """
        r = self.get("/groups/invites")
        return r.json()

    def user_groups(self):
        """
        Get user's groups
        """
        r = self.get("/user/groups")
        return r.json()

    def list(self):
        """
        List all groups
        """
        r = self.get("/groups/")
        return r.json()

    def popular(self):
        """ Return popular groups """
        r = self.get("/groups/popular")
        return r.json()

    def new(self):
        """ Return new groups """
        r = self.get("/groups/new")
        return r.json()

    def is_membership(self, gid, membership):
        """
        Return if user is a manager, member or owner
        """
        if membership not in [ 'member', 'manager', 'owner']:
            raise Exception("Membership request is unexpect as: {m}. Only member, owner or manager inquery allowed.".format(m=membership))
        url = "{b}/group/is-{m}/{gid}".format(b=self.base_url, m=membership, gid=gid)
        r = self.get(url)
        print r

