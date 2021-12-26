with open("../input/day1.txt") as f:
    input = [int(x) for x in f.read().split("\n")[:-1]]


class Solution:
    def __init__(self, data):
        self.data = data

    def part_one(self, data):
        num_increases = 0

        for idx in range(1, len(data)):
            current_depth = data[idx - 1]
            depth = data[idx]

            if current_depth < depth:
                num_increases += 1

        return num_increases

    def part_two(self, data):
        num_increases = 0
        previous_sum = 0
        idx = 0

        while idx < len(data) - 2:
            sums = data[idx] + data[idx + 1] + data[idx + 2]

            # no previous sum
            if previous_sum == 0:
                previous_sum = sums
                continue

            if sums > previous_sum:
                num_increases += 1

            previous_sum = sums
            idx += 1

        return num_increases

    def print_output(self):
        print(self.part_one(self.data))
        print(self.part_two(self.data))


result = Solution(input)
result.print_output()
