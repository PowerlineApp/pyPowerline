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


# -------------- show groups joined

users_groups = groups.user_groups()
for group in users_groups['payload']:
    #print group['id'], group['official_title']
    pprint(group)

# ----------- create group
'''
new_group = {
    'username'          : 'austin1',
    'official_type'     : 'Business',
    'official_name'     : 'another cool busines group'
    }
x = groups.create(new_group)
print x
print x.text
'''

# ---------- get group info
'''
x = groups.info(308)
print x
'''
