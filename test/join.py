'''
    Basic group example

    some groups have official_title, others have official_name
    however, takes official_name and response with official_title
'''

import sys
import requests
from pprint import pprint
import os
sys.path.insert(0, "../")

import powerline

c = powerline.Config()
s = powerline.Secure( c.base_url )
token = s.login( c.username, c.password )
groups = powerline.Groups(token, c.base_url)
gid=308
msg = groups.join(gid)
print "Join {}: {}".format(gid, msg['status'])
