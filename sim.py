from airplane import Airplane
from passenger import Passenger
import pprint

NUM_ROWS = 36
SEATS_PER_ROW = 6
PRETTY_FULL_MULT = 0.9
PRETTY_EMPTY_MULT = 0.7

## TODO research avg fullness of flight + avg flight capacity
# full flight passengers
NUM_PASSENGERS_FULL_FLIGHT = NUM_ROWS * SEATS_PER_ROW
# pretty full flight
NUM_PASSENGERS_ALMOST_FULL = NUM_PASSENGERS_FULL_FLIGHT * PRETTY_FULL_MULT
# pretty empty flight
NUM_PASSENGERS_PRETTY_EMPTY = NUM_PASSENGERS_FULL_FLIGHT * PRETTY_EMPTY_MULT

class Simulator:
    def __init__(self, rows, seats_per_row):
        self.plane = self.init_airplane(rows, seats_per_row)
        self.passengers = self.init_passengers()
        return

    def init_airplane(self, rows, seats_per_row):
        plane = Airplane(rows, seats_per_row)
        return plane

    def rear_frist(plane, passengers):
        # sort passengers by seat number

        #

        return

    def updateTick():
        # let people move into seats first
        # let people put bags up second
        # let people advance down aisle third
        return

    def init_passengers(self):
        passengers = map(lambda passenger: Passenger('HIGH'), [None] * NUM_PASSENGERS_FULL_FLIGHT)
        for i in range(0, len(passengers)):
            passengers[i].seat_assignment = i
        return passengers

# TODO ugh what is this again?
## TODO take args here
if __name__ == "__main__":
    sim = Simulator(NUM_ROWS, SEATS_PER_ROW)
