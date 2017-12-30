#!/usr/bin/env python
# encoding: utf-8

import requests
import json
import sys

class Socket():
    def __init__(self, url, host, port):
        self.url= url + "?h=%s&p=%d" % (host, port)
        self.session = requests.Session()
        self.session.headers = {"Connection":"keep-alive"}

    def print_response(self, response):
        print "=" * 32
        print response.headers
        print "=" * 32
        print response.content
        print "=" * 32

    def connect(self):
        headers = {"C":"N"}
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

    def get_session(self, url):
        response = self.session.get(url)
        print response.headers
        print response.content


def main():
    if len(sys.argv) != 4:
        print "python %s [URL] [HOST] [PORT]" % (sys.argv[0])
        exit(1)
    url = sys.argv[1]
    host = sys.argv[2]
    port = int(sys.argv[3])
    socket = Socket(url, host, port)
    socket.get_session(url)
    connect_result = socket.connect()
    if connect_result[0]:
        print "[+] %s" % (connect_result[1])
    else:
        print "[-] %s" % (connect_result[1])

if __name__ == "__main__":
    main()

