from events import EventManager

class TripAnalyzer(EventManager):
  def __init__(self, tripId):
    self.tripId = tripId
    self.stopId = None

  def update(self, predictions):
    newStopId = self.getShortestPrediction(predictions)

    if(newStopId):
      if(self.stopId != None):
        self.turnOff(self.stopId)

      self.turnOn(newStopId)
      self.stopId = newStopId

  def getShortestPrediction(self, trip):
    indexedOnPrediction = {}

    for stop_id in trip:
      indexedOnPrediction[trip[stop_id]] = stop_id

    times = indexedOnPrediction.keys()
    times.sort()

    shortestKey = times[0]
    shortestId  = indexedOnPrediction[shortest_key]
    
    return shortestId if shortestKey < 700 else None

    
  
  def destroy(self):
    self.turnOff(self.stopId)
