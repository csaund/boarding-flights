
SeatTypes = {
    'window': (0, 5),
    'middle': (1, 4),
    'aisle': (2, 3)
}

# handy dandy enums
Side = {
    'left': 0,
    'right': 1
}

# type is window, middle, aisle
# side is left/right
# row is row in aircraft
class Seat:
    def __init__(self, seat_type, side, row_num):
        self.type = seat_type
        self.side = side
        self.row_num = row_num
        self.occupied = False
        return


class Airplane:

    def __init__(self, rows, seats_per_row):
        self.seats = [[None for x in range(seats_per_row)] for y in range(rows)]

        self.num_rows = rows
        self.num_seats_per_row = seats_per_row
        self.total_seats = self.num_rows * self.num_seats_per_row
        self.init_seats()
        return

    ## Tells if seats[i] is left, right, window, middle, aisle
    ## always assume rows % seats == 3
    def init_seats(self):
        ## figure out side and type if we assume
        ##   | 0 1 2 _ 3 4 5 |
        ##   | 6 7 8 _ 9 ... |
        for i in range(0, self.num_rows):
            for j in range(0, self.num_seats_per_row):
                # figure seat type
                # mod to find row
                row_num = i
                type_num = j % self.num_seats_per_row
                this_seat_type = ""
                this_side = ""
                for seat_type in SeatTypes:
                    if type_num in SeatTypes[seat_type]:
                        this_seat_type = seat_type
                this_side = j % 2
                self.seats[i][j] = Seat(this_seat_type, this_side, row_num)
