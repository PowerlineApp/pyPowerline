    def user_info(self, uid):
        """ Get the user info """
        r = self.get("/profile/info/{uid:d}".format(uid=uid))
        return r.json()
