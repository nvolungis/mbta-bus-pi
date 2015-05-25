from events import EventManager
from predictionmanager import PredictionManager
import json

class StopManager(EventManager):
  def __init__(self):
    self.stops = self.getStops()
    self.predictionManager = PredictionManager(self.stops)
    self.predictionManager.addEvent( turnOn = [self.onTurnOn] )
    self.predictionManager.addEvent( turnOf = [self.onTurnOff] )

  def start(self):
    self.predictionManager.start()
    self.turnOn('arg')

  def onTurnOn(self, stop_id):
    self.turnOn(stop_id)

  def onTurnOff(self, stop_id):
    self.turnOff(stop_id)

  def getStops(self):
    return ["12645", "12648", "12649", "12650", "12651", "12652", "12653", "12654", "2637", "2575", "2576", "2577", "2578", "2579", "2580", "2581", "2582", "2583", "2584", "2586", "2587", "2588", "2589", "2590", "2591", "2593", "2594", "14150", "2606", "2605", "2607", "2609", "12610", "2612", "26131", "12615", "12616"]
    






  
