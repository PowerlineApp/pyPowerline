'''
    Basic Leader Petition example
'''

import sys
import datetime
from pprint import pprint
import os
sys.path.insert(0, "../")

import powerline

c = powerline.Config()
s = powerline.Secure( c.base_url )
token = s.login( c.username, c.password )

now = datetime.datetime.now()
gid = 308
petition = powerline.LeaderPetitions(token, c.base_url)

data = {
    "type"              : "petition",
    "subject"           : "Sign to elect pete",
    "petition_title"    : "eleted pete",
    "petition_body"     : "sign to elect pete because idk... why not!",
    "is_outsiders_sign" : True
}

try:
    petition.create(gid, data)
except Exception as e:
    print e
