import random

Probabilities = {
    'HIGH': 0.8,
    'MED': 0.5,
    'SMALL': 0.2
}

class Passenger:

    def __init__(self, probability):
        # only allowed one carry on
        self.hasBag = random.random() < Probabilities[probability];
        # initialize to all be off the plane
        self.seat_assignment = -1
        return 
