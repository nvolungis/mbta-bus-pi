from events import EventManager
from stopManager import StopManager


def onready():
  print "hi"


class LightBoard(EventManager):
  def __init__(self):
    self.stopManager = StopManager()
    self.stopManager.addEvent( turnOn = [self.onTurnOn])
    self.stopManager.addEvent( turnOff = [self.onTurnOff])
    self.stopManager.start()

  def onTurnOn(self, light):
    print "turn on " + light

  def onTurnOff(self, light):
    print "turn off " + light
