
from uuid import UUID

import uuid

class Patient:
  def __init__(
    self,
    id = uuid.uuid4(),
    healthValue = 3,
    serviceTime = 10,
    walkingTime = 10,
    name = "Clone"):
        self.id = id
        self.healthValue = healthValue
        self.serviceTime = serviceTime
        self.walkingTime = walkingTime
        self.name = name

