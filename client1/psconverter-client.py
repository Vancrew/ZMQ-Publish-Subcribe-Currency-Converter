#
# Weather update client
# Connects SUB socket to tcp://localhost:5556
# Collects weather updates and finds avg temp in zipcode
#

import sys
import zmq

# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

print("Collecting updates from currency server 'IDR to USD'")
socket.connect("tcp://localhost:5556")


socket.setsockopt(zmq.SUBSCRIBE, '')
# Process updates
#total_temp = 0
#for update_nbr in range(5):
while True:
	string = socket.recv_string()
	#zipcode, temperature, relhumidity = string.split()
	#total_temp += int(temperature)
	print("Hasil Konversi 1 IDR ke USD: %s" %string)

#print("Average temperature for zipcode was %dF" % (
#	total_temp / update_nbr)
#)



# Subscribe to zipcode, default is NYC, 10001
#zip_filter = sys.argv[1] if len(sys.argv) > 1 else "10001"

# Python 2 - ascii bytes to unicode str
#if isinstance(zip_filter, bytes):
#	zip_filter = zip_filter.decode('ascii')
#socket.setsockopt_string(zmq.SUBSCRIBE, zip_filter)
