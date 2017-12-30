#!/usr/bin/env python
# encoding: utf-8

import requests
import json
import sys

def print_response(response):
    print "=" * 32
    print response.headers
    print "=" * 32
    print response.content
    print "=" * 32


def write(session, data):
    url= "http://127.0.0.1/proxy.php?h=127.0.0.1&p=8888"
    headers = {"C":"W"}
    cookies = {'PHPSESSID':'amrppakfpus87kgfpktpo1snb2','path':'/'}
    response = session.post(url, data = data, headers = headers, cookies=cookies)
    print_response(response)
    return handle_response(response)

def handle_response(response):
    result = json.loads(response.headers['S'])
    if result['status'] == "1":
        message = result['message']
        return (True, message)
    else:
        message = result['message']
        return (False, message)


def main():
    if len(sys.argv) != 3:
        print "python %s [COOKIE] [DATA]" % (sys.argv[0])
        exit(1)
    # cookie = sys.argv[1]
    data = sys.argv[2]
    session = requests.Session()
    write_result = write(session, data)
    if write_result[0]:
        print "[+] %s" % (write_result[1])
    else:
        print "[-] %s" % (write_result[1])

if __name__ == "__main__":
    main()

