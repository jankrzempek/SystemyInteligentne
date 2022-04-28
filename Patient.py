
from uuid import UUID

import uuid

class Patient:
  def __init__(self, id = uuid.uuid4(), healthValue = 3, name = "Clone"):
        self.id = id
        self.healthValue = healthValue
        self.name = name

