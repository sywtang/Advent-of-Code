from utils.parser import data_parser

lines = data_parser("day5.txt")

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


def part_two(data):
    # what is your seat ID?
    # very front and back seats are not yours
    seat_range = find_seat_range(data)
    start = seat_range[0]
    end = seat_range[1]

    # compile of a list of all of the seat IDs and find the gap in the middle
    seat_ids = []
    current_sum_in_list = 0
    total_sum = float("-inf")

    for i in range(len(data)):
        seat = partition_seats(data[i])
        seat_ids.append(seat)

    seat_ids.sort()

    # current sum of all seat IDs in list
    for id in seat_ids:
        current_sum_in_list = max(id, id + current_sum_in_list)

        if current_sum_in_list > total_sum:
            total_sum = current_sum_in_list

    current_sum = 0
    max_sum = float("-inf")

    # max possible sum from start to end in list
    for id in range(int(start), int(end + 1)):
        current_sum = max(id, id + current_sum)

        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum - total_sum


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


def find_seat_range(data):
    lowest_seat = float("inf")
    highest_seat = float("-inf")

    for i in range(len(data)):
        seat = partition_seats(data[i])
        if seat < lowest_seat:
            lowest_seat = seat

    for i in range(len(data)):
        seat = partition_seats(data[i])
        if seat > highest_seat:
            highest_seat = seat

    return [lowest_seat, highest_seat]


print(part_one(lines))
print(part_two(lines))
