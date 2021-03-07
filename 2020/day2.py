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
