from DestinationPrediction import DestiPred
from EnergyPrediction import EnergyPred

iroute = None
route = None
lowSoc = 0.2
minSoc = 0.05
def init(i):
    iroute = i
    DestiPred.init(homeGPS=..., probThreshold=..., homeRadius=...)
    DestiPred.load()
    EnergyPred.init(homeGPS=...)
    EnergyPred.load()


def getRoute():
    # read from files[index]
    # store data in route
    # return a version for autonomie to simulate
    pass

# isim is the index of the GPS point the simulation is currently on
def engineOnOff(isim, soc):
    if soc < minSoc:
        return True
    if soc > lowSoc:
        return False
    lats = route["lats"][:isim]
    lngs = route["lngs"][:isim]
    toHome = DestiPred.predict(lats, lngs)
    if not toHome:
        return True
    socEsti = EnergyPred.predict(lats[-1], lngs[-1])
    if socEsti < minSoc:
        return True
    else:
        return False

