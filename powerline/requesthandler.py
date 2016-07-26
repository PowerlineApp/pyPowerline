'''

    Request Handler
    ===============

    A base class for Powerline API HTTP requests

    Individual controllers should inherit this class
'''

import urllib, urllib2
import requests
import json

class RequestHandler(object):


    def __init__(self, token, base_url, use_v2=False):
        self.token      = token
        self.base_url   = base_url + "/api"
        if use_v2:
            self.base_url = self.base_url + "/v2"
        self.headers    = {
            "Content-Type"  : "application/json",
            "Token"         : self.token  }


    def post(self, route, h=None, **kwargs):
        """
        POST request
        """
        url     = self.base_url + route
        if h: self.headers.update(h)
        return requests.post(url, headers=self.headers, verify=False, **kwargs)


    def put(self, route, h=None, **kwargs):
        """
        PUT request
        """
        url = self.base_url + route
        if h: self.headers.update(h)
        return requests.put(url, headers=self.headers, verify=False, **kwargs)


    def get(self, route, h=None, params=None):
        """
        GET request
        """
        kwargs  = {}
        url     = self.base_url + route
        if h:
            headers.update(h)
        if params:
            kwargs['params'] = params
        return requests.get(url, headers=self.headers, verify=False, **kwargs)


    def delete(self, route, data=None, h=None):
        """
        DELETE request
        """
        kwargs  = {}
        url     = self.base_url + route
        if h:
            headers.update(h)
        if data:
            kwargs['data'] = data
        return requests.delete(url, headers=self.headers, verify=False, **kwargs)






    def get_social_activities(self):
        r = self.request("/social-activities/")
        r.add_header('Content-Type', 'application/json')
        r.add_header("Token", self.token)
        rsp = urllib2.urlopen(r)
        j = rsp.read()
        rsp.close()
        return json.loads(j)

    def get_activities(self):
        r = self.request("/activities/")
        r.add_header('Content-Type', 'application/json')
        r.add_header("Token", self.token)
        rsp = urllib2.urlopen(r)
        j = rsp.read()
        rsp.close()
        return json.loads(j)

    def get_page_activities(self, d):
        url = "/activities?offset={0}&limit={1}".format(d['offset'], d['limit'])
        r = self.request(url)
        r.add_header('Content-Type', 'application/json')
        r.add_header("Token", self.token)
        rsp = urllib2.urlopen(r)
        j = rsp.read()
        rsp.close()
        return json.loads(j)

    def follow(self, id):
        r = self.request("/activities/")
        r.add_header('Content-Type', 'application/json')
        r.add_header("Token", self.token)
        rsp = urllib2.urlopen(r)

