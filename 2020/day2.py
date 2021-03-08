import re


def part_one(freq, letter, arr):
    pw_count = 0
    for i in range(len(arr)):
        letter_count = arr[i].count(letter[i])
        min = int(freq[i][0])
        max = int(freq[i][1])
        if min <= letter_count <= max:
            pw_count += 1
    return pw_count


def part_two(freq, letter, arr):
    pw_count = 0
    for i in range(len(arr)):
        pos_one = int(freq[i][0]) - 1
        pos_two = int(freq[i][1]) - 1
        if letter[i] == arr[i][pos_one] and letter[i] == arr[i][pos_two]:
            continue
        elif letter[i] == arr[i][pos_one] or letter[i] == arr[i][pos_two]:
            pw_count += 1
    return pw_count


with open("day2.txt") as _file:
    line = [line.split() for line in _file]
    freq = []
    letter = []
    arr = []
    for i in line:
        freq.append((re.findall(r"\d+", i[0])))
        letter.append(i[1].replace(":", ""))
        arr.append(i[2])
    print(part_one(freq, letter, arr))
    print(part_two(freq, letter, arr))
