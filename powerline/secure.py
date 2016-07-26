#

import ConfigParser
import os
import urllib, urllib2
import requests
import json

CONFIG_FILE_NAME    = "powerline.cfg"
CWD                 = os.getcwd()

# Config sections
USER_SEC            = "user"
MYSQL_SEC           = "mysql"
MAILGUN_SEC         = "mailgun"

class Config(object):

    def __init__(self,
            config_file     = os.path.join(CWD, CONFIG_FILE_NAME),
            user_sec        = USER_SEC,
            mysql_sec       = MYSQL_SEC,
            mailgun_sec     = MAILGUN_SEC ):

        self.user_sec       = user_sec
        self.mysql_sec      = mysql_sec
        self.mailgun_sec    = mailgun_sec
        self.config_file    = config_file
        # login creds
        self.username = None
        self.password = None
        self.base_url = None
        # mysql creds only useful if attempting to directly work
        # with the mysql backend. Otherwise not needed here.
        self.myuser   = None
        self.mypass   = None
        self.mydbname = None
        self.myhost   = None
        # mailgun creds only useful if attmepting to directly work
        # with the mailgun api. Otherwise not needed here.
        self.mg_key   = None

        self.load_config()


    def load_config(self):

        if not os.path.isfile(self.config_file):
            raise Exception("could not load a config file")

        config = ConfigParser.ConfigParser()
        config.read(self.config_file)

        self.username = config.get(self.user_sec, 'username')
        self.password = config.get(self.user_sec, 'password')
        self.base_url = config.get(self.user_sec, 'url')

        if config.has_section(self.mysql_sec):
            self.myuser      = config.get(self.mysql_sec, 'user')
            self.mypass      = config.get(self.mysql_sec, 'password')
            self.mydbname    = config.get(self.mysql_sec, 'dbname')
            self.myhost      = config.get(self.mysql_sec, 'host')

        if config.has_section(self.mailgun_sec):
            self.mg_key = config.get(self.mailgun_sec, 'private')
            #mailgun = mailgun.MailGunApi(mg_key)


# -------------------------------
#   Token class
# -------------------------------
#
#   returns a token from login action
#
class Secure(object):

    def __init__(self, base_url):

        self.base_url       = base_url
        self.login_url      = self.base_url + "/api/secure/login"
        self.fb_login_url   = self.base_url + "/api/secure/facebook/login"
        self.headers        = {"Content-Type": "application/x-www-form-urlencoded"}


    def login(self, username, password):
        """
        Primary login
        """
        auth = urllib.urlencode({
            "username"  : username,
            "password"  : password})
        req = requests.post(
            self.login_url,
            headers=self.headers,
            data=auth)
        req_json = req.json()
        if 'token' not in req_json:
            raise Exception("Could not parse response correctly from login")
        return req_json['token']


    def fb_login(self):
        """ facebook login

            NEEDS UPDATE """

        auth = { 'facebook_token': self.fb_token, 'facebook_id' : self.fb_id }
        req = self.request("/secure/facebook/login", urllib.urlencode(auth))
        req.add_header('Content-Type','application/x-www-form-urlencoded')
        rsp = urllib2.urlopen(req)
        d = rsp.read()
        self.token = json.loads(d)['token']
        rsp.close()
        return d

    def register(self, json):
        """
        Register a new user
        """

        validation = {
            'required' : {
                'username',
                'first_name',
                'last_name',
                'password',
                'confirm',
                'address1',
                'city',
                'state',
                'country',
                'zip',
                'email',
                'phone' },
            'optional' : {}
            }

        r = self.request("/secure/registration", urllib.urlencode(d))
        r.add_header('Content-Type','application/x-www-form-urlencoded')
        rsp = urllib2.urlopen(r)
        d = rsp.read()
        self.token = json.loads(d)['token']
        rsp.close()
        return d
