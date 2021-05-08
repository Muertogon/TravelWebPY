import geocoder
def getLoc(city):
    g = geocoder.google(city)
    eee = g.latlng
    return eee