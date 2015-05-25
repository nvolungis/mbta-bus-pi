from events import EventManager
from lightanalyzer import LightAnalyzer

import urllib2 as http
import time
from xml.dom import minidom


class PredictionManager(EventManager):
  def __init__(self, stops):
    self.stops = stops
    self.endpoint = self.getEndpoint("http://webservices.nextbus.com/service/publicXMLFeed?command=predictionsForMultiStops&a=mbta")
    self.lightAnalyzer = LightAnalyzer()
    self.lightAnalyzer.addEvent( turnOn = [self.onTurnOn] )
    self.lightAnalyzer.addEvent( turnOff = [self.onTurnOff] )

  def getEndpoint(self, base):
    endpoint = base
    for stop in self.stops:
      endpoint += "&stops=87|" + stop

    return endpoint


  def start(self):
    while True:
      self.fetch() 
      time.sleep(5)

  def onTurnOn(self, stop_id):
    self.turnOn(stop_id)

  def onTurnOff(self, stop_id):
    self.turnOff(stop_id)

  def fetch(self):
    new_predictions = {}
    response = minidom.parseString(http.urlopen(self.endpoint).read())
    stops = response.getElementsByTagName("predictions")

    for stop in stops:
      stop_id = stop.attributes["stopTag"].value
      predictions = stop.getElementsByTagName("prediction")

      if(len(predictions) != 0):
        prediction = predictions[0]
        trip_id = prediction.attributes["tripTag"].value
        seconds = prediction.attributes["seconds"].value

        if(not(trip_id in new_predictions)):
          new_predictions[trip_id] = {}

        new_predictions[trip_id][stop_id] = seconds

    self.analyzePredictions(new_predictions)

  def analyzePredictions(self, predictions):
    print predictions


      

