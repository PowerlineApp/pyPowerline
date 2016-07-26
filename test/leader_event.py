'''
    Basic leader  example
'''

import sys
import datetime
import os
sys.path.insert(0, "../")

import powerline

c = powerline.Config()
s = powerline.Secure( c.base_url )
token = s.login( c.username, c.password )

now = datetime.datetime.now()
gid = 308
event = powerline.Events(token, c.base_url)

data = {
    "type"          : "event",
    "subject"       : "event subject 2",
    "title"         : "the event title for something cool 2",
    "started_at"    : now.isoformat(),
    "finished_at"   : (now + datetime.timedelta(days=1)).isoformat()
}

try:
    event.create(gid, data)
except Exception as e:
    print e
