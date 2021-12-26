def part_1(list):
    i = 0
    k = len(list) - 1
    list.sort()
    while i < k:
        if list[i] + list[k] > 2020:
            k -= 1
        elif list[i] + list[k] < 2020:
            i += 1
        else:
            return list[i] * list[k]


def part_2(list):
    list.sort()
    curr = 0
    while curr < len(list) - 2:
        left = curr + 1
        right = len(list) - 1
        while left < right:
            if list[curr] + list[left] + list[right] > 2020:
                right -= 1
            elif list[curr] + list[left] + list[right] < 2020:
                left += 1
            else:
                return list[curr] * list[left] * list[right]
        curr += 1


# Accept a text file of numbers as input
with open("day1.txt") as _file:
    nums = [int(num) for num in _file]

    print(part_1(nums))
    print(part_2(nums))
