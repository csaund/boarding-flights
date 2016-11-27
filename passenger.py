import random

Probabilities = {
    'HIGH': 0.8,
    'MED': 0.5,
    'SMALL': 0.2
}

class Passenger:
    def __repr__(self):
        return str(self)

    def __str__(self):
        return "has bag: %s, seat_assignment: %s" % (self.hasBag, self.seat_assignment)

    def __init__(self, probability):
        # only allowed one carry on
        self.hasBag = random.random() < Probabilities[probability];
        # initialize to all be off the plane
        self.seat_assignment = {}
        self.in_seat = False
        return
