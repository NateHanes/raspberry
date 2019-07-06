#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import httplib, urllib

import sys
from Adafruit_IO import MQTTClient
ADAFRUIT_IO_KEY = '21eaab7bca7245a6b7000b1eaeb2bb29'
ADAFRUIT_IO_USERNAME = 'NateHanes'
FEED_ID = 'doorpi'

nate = 0
cliff = 0
dennis = 0
rachel = 0
denice = 0

# Pushover API setup
PUSH_TOKEN = "aZtsTRSxEn22Gb1j9jj8f6RH6q4vx1" # API Token/Key
PUSH_USER = "u67mm7kbqKTUB4GYVAwf7SEFAL7gqS" # Your User Key
PUSH_MSG = "Door Opened!" # Push Message you want sent
# number of seconds to delay between alarms
DELAY = 45
# This function sends the push message using Pushover.
# Pass in the message that you want sent

def sendPush( msg ):
	conn = httplib.HTTPSConnection("api.pushover.net:443")
	conn.request("POST", "/1/messages.json",
		urllib.urlencode({
			"token": PUSH_TOKEN,
			"user": PUSH_USER,
			"message": msg,
		}), { "Content-type": "application/x-www-form-urlencoded" })

	conn.getresponse()
	return

def connected(client):
    """Connected function will be called when the client is connected to
    Adafruit IO.This is a good place to subscribe to feed changes.  The client
    parameter passed to this function is the Adafruit IO MQTT client so you
    can make calls against it easily.
    """
    # Subscribe to changes on a feed named Counter.
    print('Subscribing to Feed {0}'.format(FEED_ID))
    client.subscribe(FEED_ID)
    print('Waiting for feed data...')

def disconnected(client):
    """Disconnected function will be called when the client disconnects."""
    sys.exit(1)

def message(client, feed_id, payload):
    """Message function will be called when a subscribed feed has a new value.
    The feed_id parameter identifies the feed, and the payload parameter has
    the new value.
    """
    print('Feed {0} received new value: {1}'.format(feed_id, payload))
    global nate
    global cliff
    global dennis
    global rachel
    global denice

    if(payload == "Nate on"):
        nate = 1
        print("Nate Activated")

    if(payload == "Nate off"):
	nate = 0
	print("Nate Deactivated")

    if(payload == "cliff on"):
	cliff = 1
	print("Cliff Activated")

    if(payload == "cliff off"):
	cliff = 0
	print("Cliff Deactivated")

    if(payload == "Dennis on"):
        dennis = 1
        print("Dennis Activated")

    if(payload == "Dennis off"):
        dennis = 0
        print("Dennis Deactivated")


    if(payload == "Rachel on"):
        rachel = 1
        print("Rachel Activated")

    if(payload == "Rachel off"):
        rachel = 0
        print("Rachel Deactivated")


    if(payload == "Denise on"):
        denice = 1
        print("Denice Activated")

    if(payload == "Denise off"):
        denice = 0
        print("Denice Deactivated")

client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.connect()
client.loop_background()


GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

msg = "Door Opened!"


while True:
    input_state = GPIO.input(18)
    if input_state == False:
	print(PUSH_MSG)
	print("Nate: ")
	print(nate)
	print("Cliff: ")
	print(cliff)
	print("Dennis: ")
	print(dennis)
        print("Rachel: ")
	print(rachel)
	print("Denice: ")
	print(denice)

	if(nate == 1):
	    conn = httplib.HTTPSConnection("api.pushover.net:443")
            conn.request("POST", "/1/messages.json",
                    urllib.urlencode({
                            "token": PUSH_TOKEN,
                            "user": "gm2oqmqgm4znbeq862j4mjtb2warqf",
                            "message": msg,
                    }), { "Content-type": "application/x-www-form-urlencoded" })

            conn.getresponse()

	if(cliff == 1):
            conn = httplib.HTTPSConnection("api.pushover.net:443")
            conn.request("POST", "/1/messages.json",
                    urllib.urlencode({
                            "token": PUSH_TOKEN,
                            "user": "gfrs9sqco4mwxdma7b581sz6xdrx8p",
                            "message": msg,
                    }), { "Content-type": "application/x-www-form-urlencoded" })

            conn.getresponse()

	if(dennis == 1):
            conn = httplib.HTTPSConnection("api.pushover.net:443")
            conn.request("POST", "/1/messages.json",
                    urllib.urlencode({
                            "token": PUSH_TOKEN,
                            "user": "gsbsw6f99wcnnpfhwqmwdcatvigusz",
                            "message": msg,
                    }), { "Content-type": "application/x-www-form-urlencoded" })

            conn.getresponse()

        if(rachel == 1):
            conn = httplib.HTTPSConnection("api.pushover.net:443")
            conn.request("POST", "/1/messages.json",
                    urllib.urlencode({
                            "token": PUSH_TOKEN,
                            "user": "gtb17tcng9xzf6utrajtouhcqgzp8k",
                            "message": msg,
                    }), { "Content-type": "application/x-www-form-urlencoded" })

            conn.getresponse()


        if(denice == 1):
            conn = httplib.HTTPSConnection("api.pushover.net:443")
            conn.request("POST", "/1/messages.json",
                    urllib.urlencode({
                            "token": PUSH_TOKEN,
                            "user": "g8rzmr4ngqwfo3apm42fink39ipjna",
                            "message": msg,
                    }), { "Content-type": "application/x-www-form-urlencoded" })

            conn.getresponse()



	while True:
	    input_state = GPIO.input(18)
	    if input_state == True:
		print("Door Closed.")
		break
#cleanup GPIOs when program exits
GPIO.cleanup()
