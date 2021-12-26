def data_parser(file):
    with open(file, "r") as fd:
        lines = [line.rstrip() for line in fd]

    return lines
