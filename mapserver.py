#!/usr/bin/python3
from flask import Flask, render_template
import json

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
        return json.dumps(gpsr.getLocation())
    else:
        global gLocation
        return json.dumps(gLocation)

@app.route('/')
def do_route():
    return render_template("index.html")

@app.route('/<filename>')
def do_file(filename):
    return render_template(filename)

@app.route('/javascript/<filename>')
def do_js(filename):
    return render_template("./javascript/"+filename)

if __name__ == '__main__':
    app.run(host='<host IP>', port=8008)
    #app.run(host='localhost', port=8008)
