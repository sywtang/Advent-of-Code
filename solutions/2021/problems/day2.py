with open("../input/day2.txt") as f:
    input = [x for x in f.read().split("\n")[:-1]]


class Solution:
    def __init__(self, data):
        self.data = data

    def part_one(self, data):
        horizontal = 0
        depth = 0

        for direction in data:
            if direction[0] == "f":
                horizontal += int(direction[-1])
            elif direction[0] == "u":
                depth -= int(direction[-1])
            else:
                depth += int(direction[-1])

        return horizontal * depth

    def part_two(self, data):
        horizontal = 0
        depth = 0
        aim = 0

        for direction in data:
            if direction[0] == "f":
                horizontal += int(direction[-1])
                depth += aim * int(direction[-1])
            elif direction[0] == "u":
                aim -= int(direction[-1])
            else:
                aim += int(direction[-1])

        return horizontal * depth

    def print_output(self):
        print(self.part_one(self.data))
        print(self.part_two(self.data))


solution = Solution(input)
solution.print_output()
