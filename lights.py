
#!/usr/bin/python

#####################
#DEFAULT WHITE LIGHT#
#Hue: 8731          #
#Brightness: 254    #
#Saturation: 106    #
#####################

import time as t
from phue import Bridge
from datetime import *
from astral import Astral

#establish location for sunset and sunrise times
city_name = 'Buffalo'
a = Astral()
a.solar_depression = 'civil'
city = a[city_name]
print('Information for %s/%s\n' % (city_name, city.region))


timezone = city.timezone
print('Timezone: %s' % timezone)

print('Latitude: %.02f; Longitude: %.02f\n' % \
(city.latitude, city.longitude))

sun = city.sun(date = datetime.now() ,local = True)
print('Dawn:    %s' % str(sun['dawn']))
print('Sunrise: %s' % str(sun['sunrise']))
print('Noon:    %s' % str(sun['noon']))
print('Sunset:  %s' % str(sun['sunset']))
print('Dusk:    %s' % str(sun['dusk']))

#establish connection to bridge
b=Bridge('10.10.22.213')
b.connect()

#create array of light objects
lights = b.lights

def startColorLoop():
    """This function begins the color loop on all lights"""
    b.set_group(1, 'on', True)
    b.set_group(1, 'bri', 254)
    b.set_group(1, 'hue', 255)
    b.set_group(1, 'sat', 255)
    b.set_group(1, 'effect', 'colorloop')

def stopColorLoop():
    """This function stops the color loop on all lights and returns the lights to white"""
    b.set_group(1, 'effect', 'none')
    b.set_group(1, 'bri', 254)
    b.set_group(1, 'hue', 8731)
    b.set_group(1, 'sat', 106)

def setDayScene():
    """This Function determines the day of the week and sets the appropriate scene depending on the day"""
    day = datetime.today().weekday()
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    today = week[day]
    b.run_scene('Outdoor', today, transition_time=1)


#startColorLoop()
#t.sleep(30)
#stopColorLoop()
#setDayScene()

now = datetime.now()

sunset = sun['sunset']
dusk = sun['dusk']

sunrise = sun['sunrise']

while True:
    now = datetime.now()

    if (now.hour == sunset.hour and now.minute == (sunset.minute - 15)):
        startColorLoop()
        time.sleep(60)

    if (now.hour == dusk.hour and now.minute == (dusk.minute - 15)):
        stopColorLoop()
        setDayScene()

    if (now.hour == 0 and now.minute == 1):
        setDayScene()

    if (now.hour == sunrise.hour and now.minute == (sunrise.minute + 15)):
        b.set_group(1, 'on', False)
