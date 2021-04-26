passports = open("day4.txt").read().split("\n\n")


def part_one(data):
    valid_passport_count = 0
    required_fields = ["pid", "ecl", "hcl", "hgt", "eyr", "iyr", "byr"]

    # increment counter if every field in passport is in required_fields
    for passport in data:
        valid_passport_count += all(field in passport for field in required_fields)

    return valid_passport_count


print(part_one(passports))
