# gps
East Asia Map Viewer through web server and GPS device

Installation
------------
1.) You have to install Python Bottle web server module.
```shell
sudo apt-get install python-setuptools
sudo easy_install pip
sudo pip install bottle
```
2.) If you want to get gps location, install gps related packages for debian linux.
```shell
sudo apt-get install gpsd gpsd-clients python-gps
```
Set the gps server with connected gps module. ex)
```shell
sudo gpsd /dev/ttyS0 -F /var/run/gpsd.lock
```
3.) Clone this repo onto your linux.
```shell
git clone https://github.com/swkim01/gps.git
cd gps
```
3.) Set ip address within the webserver file(mapserver.py) and execute.
```shell
python mapserver.py
```
4.) Browse web with URL.
```
http://<IP address>:8008/
```

Supported Maps
--------------
#### Global Maps
 * OpenStreet Map: WGS84 Coordinate (EPSG:900913) with base (-180, 90) and (+Lon, -Lat) tile indices
 * Google Map: WGS84 Coordinate (EPSG:900913) with base (-180, 90) and (+Lon, -Lat) tile indices

#### Korean Maps
 * Daum Map: Korea 2000/Central Belt (GRS80) Coordinate (EPSG:5181) with offset (-30000, -60000) and (+Lon, +Lat) tile indices
 * Naver Map: UTM-K (GRS80) Coordinate (EPSG:5179) with offset (+90112, +1192896) and (+Lon, +Lat) tile indices
 * VWorld Map: WGS84 Coordinate (EPSG:900913) with base (-180, 90) and  (+Lon, -Lat) tile indices

#### China Maps
 * GoogleMap China: GCJ-02 Coordinate with base (-180, 90) and (+Lon, -Lat) tile indices
 * Baidu Map: GCJ-02 -> BD-09 Coordinate with base (0, 0) and (+Lon, +Lat) tile indices
 * Sogou Map: BD-09 Coordinate -> 256/250 Scale Transform with base (0, 0) and (+Lon, +Lat) tile indices
 * Autonavi Map: GCJ-02 Coordinate with base (-180, 90) and (+Lon, -Lat) tile indices

#### Japan Maps
 * Japan Vector Map: WGS84 Coordinate (EPSG:900913) with base (-180, 90) and (+Lon, -Lat) tile indices
 * Yahoo Japan Map: WGS84 Coordinate (EPSG:900913) with base (0, 0) and (+Lon, +Lat) tile indices

## Acknowledgement

Thanks [@tschaub](https://github.com/tschaub/projzh) for china map coordinates.
