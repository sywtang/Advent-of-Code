with open("day5.txt", "r") as fd:
    lines = [line.rstrip() for line in fd]

SEAT = "FBFBBFFRLR"
SEAT_2 = "FB"


# think of how to solve recursively
# binary space partitioning

# F: lower half = (upper - lower) // 2 = lower + result = new upper value
# ex: (127 - 0) // 2 = 63 -> 0 + 63 = 63, 0

# B: upper half, subtract difference from upper to get new lower value
# ex: (63 - 0) // 2 = 31 -> 63 - 31 = 32 => 63, 32


# Return highest seat ID
def part_one(data):
    highest_seat = 0

    for i in range(len(data)):
        seat = partition_seats(data[i])
        if seat > highest_seat:
            highest_seat = seat
    return highest_seat


def partition_seats(data):
    row_lower = 0
    row_upper = 127

    col_lower = 0
    col_upper = 7

    row = 0
    col = 0
    for i in range(len(data)):
        if data[i] == "F":
            new_half = (row_upper - row_lower) // 2
            row_upper = row_lower + new_half
        elif data[i] == "B":
            new_half = (row_upper - row_lower) // 2
            row_lower = row_upper - new_half
        if i == 6:
            row = (
                min(row_lower, row_upper)
                if data[i] == "F"
                else max(row_lower, row_upper)
            )
        if data[i] == "R":
            new_half = (col_upper - col_lower) // 2
            col_lower = col_upper - new_half
        elif data[i] == "L":
            new_half = (col_upper - col_lower) // 2
            col_upper = col_lower + new_half
        if i == 9:
            col = (
                min(col_lower, col_upper)
                if data[i] == "L"
                else max(col_lower, col_upper)
            )

    seat = row * 8 + col
    return seat


print(part_one(lines))
