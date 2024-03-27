#!/usr/bin/python
from bottle import route,run,get,response,static_file,request
try:
    import gps
except ImportError:
    has_gps_module = False

if has_gps_module:
    import gpsreceiver

    gpsr = gpsreceiver.GpsReceiver()
    gpsr.daemon = True
    gpsr.start()

else:
    gLocation={"lat":35.180, "lon":129.076, "alt":0.0, "speed":0.0}

#respone json for gps location
@get('/getLocation')
def get_location():
    if has_gps_module:
        return gpsr.getLocation()
    else:
        global gLocation
        return gLocation

@route('/')
def do_route():
    return static_file("index.html", root=".")

@route('/<filename>')
def do_file(filename):
    return static_file(filename, root=".")

@route('/geolocation_marker.png')
def do_marker():
    return static_file("geolocation_marker.png", root="./static")

@route('/javascript/<filename>')
def do_js(filename):
    return static_file(filename, root="./static/javascript")

run(host='<host IP>', port=8008)
#run(host='localhost', port=8008)
