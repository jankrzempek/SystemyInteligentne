# from Doctor import Doctor
class Queue:

  def __init__(self, queue, limit = 1000): 
        self.queue = queue 
        self.limit = limit
  
  def addToQueue(self, patient):
    self.queue.append(patient)
  
  def takeFirstToDoctor(self, doctor, timeAmount) -> str:
    name = self.queue[0]
    self.queue.pop(0)
    doctor.defineAsBusy(timeAmount)
    return name