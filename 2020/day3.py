with open("day3.txt", "r") as fd:
    lines = [line.rstrip() for line in fd]


def part_one():
    trees = 0
    right = 3
    for i in range(1, len(lines)):
        if lines[i][right % len(lines[i])] == "#":
            trees += 1
        right += 3
    return trees


print(part_one())
