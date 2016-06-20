#!/usr/bin/env python  

from twisted.internet import reactor, task  
from twisted.web.client import HTTPConnectionPool  
import treq  
import random  
from datetime import datetime
from twisted.internet.error import ConnectBindError

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

# TODO: Figure out how to hide the exceptions that are generated.
def request():  
    deferred = treq.get('http://127.0.0.1:8000')
    deferred.addErrback(error_handler)
    deferred.addCallback(request_done)
    return deferred

def requests_generator():  
    global req_generated
    while True:
        deferred = request()
        req_generated += 1
        # do not yield deferred here so cooperator won't pause until
        # response is received
        yield None

# TODO: This does not handle shit, fix it.
def error_handler(failure):
    failure.trap(ConnectBindError)

if __name__ == '__main__':  
    # make cooperator work on spawning requests
    cooperator.cooperate(requests_generator())

    # run the counter that will be reporting sending speed once a second
    reactor.callLater(1, counter)

    # run the reactor
    reactor.run()