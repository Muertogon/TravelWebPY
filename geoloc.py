import geocoder
def getLoc(city):
    g = geocoder.osm(city)
    eee = g.latlng
    return eee
