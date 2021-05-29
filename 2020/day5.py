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


def part_one(data):
    return data
