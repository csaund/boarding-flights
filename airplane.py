
SeatTypes = {
    'window': 3,
    'middle': 2,
    'aisle': 1
}

# handy dandy enums
SIDE = {
    'left': 0
    'right': 1
}

class Seat:
    def __init__(self, type):
        self.type = ""
        self.row = -1
        self.side = ""


class Airplane:

    def __init__(self, rows, seats_per_row):
        self.num_rows = rows
        self.num_seats_per_row = seats_per_row
        self.total_seats = self.num_rows * self.num_seats_per_row
        return

    ## Tells if seats[i] is left, right, window, middle, aisle
    ## always assume rows % seats == 3
    def initSeats(self):
        ## for now, just assume 3 seats on each side
        self.seats = [None] * self.num_rows * self.num_seats
