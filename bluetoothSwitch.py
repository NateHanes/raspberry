#!/usr/bin/python
import bluetooth
import time
import urllib2
import pywemo

print "In/Out Board"
print ("sleeping for 60")
#time.sleep(60)
address = "192.168.0.4"
port = pywemo.ouimeaux_device.probe_wemo(address)
url = 'http://%s:%i/setup.xml' % (address, port)
device = pywemo.discovery.device_from_description(url, None)
print(device)

state = device.get_state()
result = bluetooth.lookup_name('88:BD:45:B8:99:29', timeout=5)
manual = 0

while True:

        result = bluetooth.lookup_name('88:BD:45:B8:99:29', timeout=5)
        state = device.get_state()
        if (result == "Galaxy S9+" and state == 0 and manual == 0):
                device.on()

        result = bluetooth.lookup_name('88:BD:45:B8:99:29', timeout=5)
        state = device.get_state()
        if (result == "Galaxy S9+" and state == 0):
                manual = 1

        result = bluetooth.lookup_name('88:BD:45:B8:99:29', timeout=5)
        state = device.get_state()
        if (result == None):
                device.off()
                manual = 0