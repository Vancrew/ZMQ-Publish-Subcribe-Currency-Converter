#
# Weather update server
# Binds PUB socket to tcp://*:5556
# Publishes random weather updates
#

import zmq
from random import randrange
import time
import requests

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5556")

while True:
        response = requests.get(
                'http://jsonrates.com/get/?'+
                'from=IDR'+
                '&to=USD'
                '&apiKey=jr-8749a8da225f0508da2bd6a1c137f339'
        )
        json = response.json()
        rate = float(json['rate'])
        #mi = str(rate)

        # Send reply back to client

        socket.send_string("%f" % (rate))

        # Do some 'work'
        time.sleep(10)

