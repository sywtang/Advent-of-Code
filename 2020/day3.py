with open("day3.txt", "r") as fd:
    lines = [line.rstrip() for line in fd]


def part_one(slope, jump=1):
    trees = 0
    right = slope
    for i in range(jump, len(lines)):
        if lines[i][right % len(lines[i])] == "#":
            trees += 1
        right += slope
    return trees


# take in list of arguments where n elements represents slopes
def part_two():
    slope_one = part_one(1)
    slope_two = part_one(3)
    slope_three = part_one(5)
    slope_four = part_one(7)
    slope_five = part_one(1, 2)

    return slope_one * slope_two * slope_three * slope_four * slope_five


print(part_one(3))
print(part_two())
