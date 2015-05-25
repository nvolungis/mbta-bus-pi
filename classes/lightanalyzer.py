from events import EventManager
from tripanalyzer import TripAnalyzer 

class LightAnalyzer(EventManager):
  def __init__(self):
    self.tripAnalyzers = {}

  def analyze(self, predictions):
    touched = []

    for trip_id in predictions:
      if(not(trip_id in self.tripAnalyzers)):
        self.tripAnalyzers[trip_id] = TripAnalyzer(trip_id)
        self.tripAnalyzers[trip_id].addEvent( turnOn = [self.onTurnOn] )
        self.tripAnalyzers[trip_id].addEvent( turnOff = [self.onTurnOff] )

      self.tripAnalyzers[trip_id].update(predictions[trip_id])

    for trip_id in self.tripAnalyzers:
      if(not(trip_id in touched)):
        self.tripAnalyzers[trip_id].destroy()
        self.tripAnalyzers.pop(trip_id, None)

  def onTurnOn(self, stop_id):
    this.turnOn(stop_id)

  def onTurnOff(self, stop_id):
    this.turnOff(stop_id)
  


