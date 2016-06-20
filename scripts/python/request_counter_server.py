#!/usr/bin/env python
# Reflects the requests from HTTP methods GET, POST, PUT, and DELETE
# Written by Nathan Hamiel (2010)

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from optparse import OptionParser
import time

request_count = 0

class RequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
    
        request_path = self.path
        global request_count
        request_count += 1
        print('[{}] Got request number {}'.format(time.ctime(), request_count))
        
        self.send_response(200)

    do_POST = do_GET
    do_PUT = do_GET
    do_DELETE = do_GET
        
def main():
    port = 8000
    print('Listening on localhost:%s' % port)
    server = HTTPServer(('', port), RequestHandler)
    server.serve_forever()

        
if __name__ == "__main__":
    parser = OptionParser()
    parser.usage = ("Creates an http-server that will echo out any GET or POST parameters\n"
                    "Run:\n\n"
                    "   reflect")
    (options, args) = parser.parse_args()
    
    main()
