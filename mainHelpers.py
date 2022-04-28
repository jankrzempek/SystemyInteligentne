# HELPERS
from Queue import Queue
import time

class Helpers:
    def isAnyoneInQueue(self, queue) -> bool:
        if len(queue) != 0: return True
        else: return False
    
    def isAnyoneInAnyQueue(self, queueColection) -> bool:
        for q in queueColection:
            if len(q.queue) != 0: return True
        return False
    
    def getQueueWithPeople(self, queueColection) -> Queue:
        # For now we are selecting the first one - the light one
        for q in queueColection:
            if len(q.queue) != 0: return q
    
    def defineWorkingHours(self) -> time:
        # Starting the whole process
        return time.time() + (60 * 60 * 2) / 100
        # use: + 60 * 60 * 2 when testing
        # use: + 60 * 60 * 8  on production