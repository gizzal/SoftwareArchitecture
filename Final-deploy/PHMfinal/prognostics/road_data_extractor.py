import requests
from xml.etree import ElementTree


def get_route_coordinates(flat, flon, tlat, tlon):
    link1 = 'http://www.yournavigation.org/api/1.0/gosmore.php?format=kml&flat={}&flon={}&tlat={}&tlon={}&v=motorcar&fast=1&layer=mapnik'.format(
        flat, flon, tlat, tlon)

    response = requests.get(link1)

    tree = ElementTree.fromstring(response.content)

    distance = tree[0].find('{http://earth.google.com/kml/2.0}distance')
    print(distance.text)

    folder = tree[0].find('{http://earth.google.com/kml/2.0}Folder')
    placemark = folder.find('{http://earth.google.com/kml/2.0}Placemark')
    line_string = placemark.find('{http://earth.google.com/kml/2.0}LineString')
    coordinates = line_string.find('{http://earth.google.com/kml/2.0}coordinates')
    print(coordinates.text)
    return {'distance': distance, 'coordinates': coordinates}


if __name__ == '__main__':
    flat, flon, tlat, tlon = 55.751008, 48.743636, 55.849819, 48.895440
    get_route_coordinates(flat, flon, tlat, tlon)
