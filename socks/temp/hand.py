#!/usr/bin/env python
# encoding: utf-8

def connect(host, port):
    data = "POST /proxy.php?h=%s&p=%d HTTP/1.1\r\n" % (host, port)
    data += "Host: 127.0.0.1\r\n"
    data += "Accept-Encoding: identity\r\n"
    data += "Connection: keep-alive\r\n"
    data += "C: N\r\n"
    data += "Content-Length: 0\r\n"
    data += "\r\n\r\n\r\n"
    return data

