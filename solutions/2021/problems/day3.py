with open("../input/day3.txt") as f:
    input = [x for x in f.read().split("\n")[:-1]]


class Solution:
    def __init__(self, data):
        self.data = data

    def part_one(self, data):
        i = 0
        gamma = [0] * len(data[i])
        epsilon = [0] * len(data[i])

        while i < len(data):
            binary = data[i]

            for idx in range(len(binary)):
                if int(binary[idx]) == 1:
                    gamma[idx] += 1
                    epsilon[idx] -= 1
                else:
                    gamma[idx] -= 1
                    epsilon[idx] += 1
            i += 1

        gamma = self.convert_to_binary(gamma)
        epsilon = self.convert_to_binary(epsilon)

        return self.convert_to_decimal(gamma) * self.convert_to_decimal(epsilon)

    def part_two(self, data):
        return data

    def convert_to_binary(self, input):
        binary = ""

        for idx in range(len(input)):
            if input[idx] > 0:
                binary += "1"
            else:
                binary += "0"

        return binary

    def convert_to_decimal(self, input):
        num = input
        decimal_value = 0
        base = 1

        for i in range(len(num) - 1, -1, -1):
            if num[i] == "1":
                decimal_value += base
            base = base * 2

        return decimal_value

    def print_output(self):
        print(self.part_one(self.data))


solution = Solution(input)
solution.print_output()
