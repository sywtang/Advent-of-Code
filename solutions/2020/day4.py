import re

data = open("day4.txt").read().strip().split("\n\n")


def passport_validator_part_one(data):
    valid_passport_count = 0
    required_fields = ["pid", "ecl", "hcl", "hgt", "eyr", "iyr", "byr"]

    # increment counter if every field in passport is in required_fields
    for passport in data:
        valid_passport_count += all(field in passport for field in required_fields)

    return valid_passport_count


# Alternatively: Create a dict checking your passport validations

lines = [line.replace("\n", " ") for line in open("day4.txt").read().split("\n\n")]
passports = [dict(tuple(x.split(":")) for x in line.split()) for line in lines]

fields = {
    "byr": lambda x: len(x) == 4 and 2002 >= int(x) >= 1920,
    "iyr": lambda x: len(x) == 4 and 2020 >= int(x) >= 2010,
    "eyr": lambda x: len(x) == 4 and 2030 >= int(x) >= 2020,
    "hgt": lambda x: (x.endswith("cm") and 193 >= int(x[:-2]) >= 150)
    or (x.endswith("in") and 76 >= int(x[:-2]) >= 59),
    "hcl": lambda x: re.match(r"^#[a-f\d]{6}$", x) != None,
    "ecl": lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda x: len(x) == 9 and x.isdigit(),
}


def part_one(passports):
    return all(key in passports for key in fields)


def part_two(passports):
    return all(key in passports and fields[key](passports[key]) for key in fields)


print(passport_validator_part_one(data))

print(sum(part_one(p) for p in passports))
print(sum(part_two(p) for p in passports))
