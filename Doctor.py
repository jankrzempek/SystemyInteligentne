import threading


class Doctor:
  isAvailable = True
  patientCount = 0

  def __init__(self, serviceTime, walkingTime, isAvailable = True, patientCount = 0):  
        self.serviceTime = serviceTime * 60 # The reason is to have minutes here
        self.walkingTime = walkingTime * 60 # The reason is to have minutes here
        self.isAvailable = isAvailable
        self.patientCount = patientCount

  def isFreeToTakeNewPatient(self) -> bool:
    if self.isAvailable:
      return True
    else:
      return False

  def defineAsBusy(self):
    self.isAvailable = False
    self.patientCount += 1
    x = threading.Timer(self.__getBlockingTime(), self.__free)
    x.start()

  # Private methods
  def __free(self):
    self.isAvailable = True

  def __getBlockingTime(self) -> float:
    return (self.serviceTime + self.walkingTime) / 100