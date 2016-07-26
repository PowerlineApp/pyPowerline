'''
    Basic event example
'''
import requests
import json
import datetime
from pprint import pprint

import sys
import os
sys.path.insert(0, "../")

from powerline.secure import Secure, Config

c = Config()
s = Secure( c.base_url )
token = s.login( c.username, c.password )


data = {
    "type"          : "event",
    "subject"       : "event subject",
    "title"         : "the event title for something cool",
    "started_at"    : now.isoformat(),
    "finished_at"   : (now + datetime.timedelta(days=1)).isoformat()
}

"""
url = base + "/groups/{0}/polls".format(gid)
r = requests.get(url, headers=headers).json()
for e in r['payload']:
    print e
"""
now = datetime.datetime.now()



url = base + "/groups/{0}/polls".format(gid)
print url
pprint(data)

r = requests.post(url, headers=headers, json=data)
print r.json()
#print r
#print r.text

