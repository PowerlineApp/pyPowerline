'''
    Basic login example
'''

import sys
import os
sys.path.insert(0, "../")
import powerline

c = powerline.Config()                # read a powerline.cfg file
s = powerline.Secure( c.base_url )

token = s.login( c.username, c.password )
print token
