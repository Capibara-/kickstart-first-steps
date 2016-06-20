#!/usr/bin/env python  
import treq
import sys
import random
from twisted.internet import reactor, task  
from twisted.web.client import HTTPConnectionPool  
from datetime import datetime
from twisted.internet.error import ConnectBindError, ConnectError, ConnectionLost, ConnectionDone

req_generated = 0  
req_made = 0  
req_done = 0

cooperator = task.Cooperator()

pool = HTTPConnectionPool(reactor)

def counter():  
    '''
    This function gets called once a second and prints the progress at one 
    second intervals. 
    '''
    print("[*] Requests: {} generated; {} made; {} done".format(
            req_generated, req_made, req_done))
    # reset the counters and reschedule ourselves
    req_generated = req_made = req_done = 0
    reactor.callLater(1, counter)

def body_received(body):  
    global req_done
    req_done += 1

def request_done(response):  
    global req_made
    deferred = treq.json_content(response)
    req_made += 1
    deferred.addCallback(body_received)
    return deferred

def request(url):  
    deferred = treq.get(url)
    deferred.addErrback(error_handler)
    return deferred

def requests_generator(url):  
    global req_generated
    while True:
        deferred = request(url)
        req_generated += 1
        # do not yield deferred here so cooperator won't pause until
        # response is received
        yield None

def error_handler(failure):
    failure.trap(Exception)

def main():
    if len(sys.argv) != 2:
        print "Usage: {} <URL>".format(sys.argv[0])
        return

    url = sys.argv[1]

    # make cooperator work on spawning requests
    cooperator.cooperate(requests_generator(url))

    # run the counter that will be reporting sending speed once a second
    reactor.callLater(1, counter)

    # run the reactor
    reactor.run()

if __name__ == '__main__':  
    main()