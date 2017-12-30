#!/usr/bin/env python
# encoding: utf-8

import requests
import json

    def connect(self):
        headers = {"C":"N"}
        response = self.session.post(self.url, headers = headers)
        self.print_response(response)
        return self.handle_response(response)

    def read(self):
        headers = {"C":"R"}
        response = self.session.post(self.url, headers = headers)
        self.print_response(response)
        result = json.loads(response.headers['S'])
        if result['status'] == "1":
            message = result['message']
            content = response.content
            return (True, message, content)
        else:
            message = result['message']
            return (False, message)

    def write(self, data):
        headers = {"C":"W"}
        response = self.session.post(self.url, data = data, headers = headers)
        self.print_response(response)
        return self.handle_response(response)

    def close(self):
        headers = {"C":"C"}
        response = self.session.post(self.url, headers = headers)
        self.print_response(response)
        return self.handle_response(response)

    def handle_response(self, response):
        result = json.loads(response.headers['S'])
        if result['status'] == "1":
            message = result['message']
            return (True, message)
        else:
            message = result['message']
            return (False, message)

class HTTP():
    def __init__(self, url, host, port)
        self.url= url + "?h=%s&p=%d" % (host, port)
        self.session = requests.Session()
        self.session.headers = {"Connection":"keep-alive"}

    def print_response(self, response):
        print "=" * 32
        print response.headers
        print "=" * 32
        print response.content
        print "=" * 32

    def get(self, url):
        self



def main():
    url = "http://127.0.0.1/server.php"
    remote_host = "127.0.0.1"
    remote_port = int("8888")
    local_port = int("9999")
    # start listening

if __name__ == "__main__":
    main()
