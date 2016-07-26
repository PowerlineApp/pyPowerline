'''
    Basic micropetition example
'''
import requests
import json

import sys
import os
sys.path.insert(0, "../")

from powerline.secure import Secure, Config

headers = {
    "Content-Type"  : "application/json",
    "Token"         : None  }
base = 'https://api-dev.powerli.ne/api/v2'

c = Config()                # read a powerline.cfg file
s = Secure( c.base_url )
token = s.login( c.username, c.password )
headers['Token'] = token

gid = 59

"""
url = base + "/user/groups"
r = requests.get(url, headers=headers)
data = r.json()

for k, v in data.iteritems():
    if k == 'payload':
        for e in v:
            print e['id'], e['official_title']
"""
"""
# list micropetitions
url = base + "/user/micro-petitions"
r = requests.get(url, headers=headers)
print r.json()
"""



# create quorum micropetition
data = {
    "petition_body" : "testing the body here",
    "title"         : "austin's title",
    "is_outsiders_sign" : True,
    "type"          : "quorum" }

url = base + "/groups/{id}/micro-petitions".format(id=gid)
r = requests.post(url, json=data, headers=headers)
print r.json()

"""
url = base + "/user/micro-petitions"
r = requests.get(url, headers=headers)
print r.json()
"""

