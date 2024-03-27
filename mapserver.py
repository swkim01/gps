#!/usr/bin/python3
from flask import Flask, render_template, jsonify, send_from_directory
#import json

app = Flask(__name__, template_folder=".", static_url_path='')

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
@app.route('/getLocation')
def get_location():
    if has_gps_module:
        response = jsonify(gpsr.getLocation())
    else:
        global gLocation
        response = jsonify(gLocation)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/')
def do_route():
    return render_template("index.html")

@app.route('/<filename>.html')
def do_file(filename):
    return render_template(filename+'.html')

@app.route('/javascript/<filename>')
def do_js(filename):
    return send_from_directory("javascript", filename)

if __name__ == '__main__':
    #app.run(host='<host IP>', port=8008)
    app.run(host='localhost', port=8008)
