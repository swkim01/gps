#!/usr/bin/python
from bottle import route,run,get,response,static_file,request
import threading
import gpsreceiver

gpsr = gpsreceiver.GpsReceiver()
gpsr.daemon = True
gpsr.start()

#gLocation={"lat":35.180, "lon":129.076, "alt":0.0, "speed":0.0}

#respone json for gps location
@get('/getLocation')
def get_location():
    #return gLocation
    return gpsr.getLocation()

@route('/')
def do_route():
    return static_file("osm.html", root=".")

@route('/<filename>')
def do_map(filename):
    return static_file(filename, root=".")

@route('/geolocation_marker.png')
def do_marker():
    return static_file("geolocation_marker.png", root=".")

@route('/javascript/<filename>')
def do_js(filename):
    return static_file(filename, root="./javascript")

run(host='<host IP>', port=8008)
