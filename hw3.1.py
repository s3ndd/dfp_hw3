"""
Homework 3 Team 7:

Name: Yuling Shi
Andrew ID: yulings
Email: yulings@andrew.cmu.edu

Name: Sheldon Shi
Andrew ID: lijuns
Email: lijuns@andrew.cmu.edu
"""


def main():
    raw_file = "expenses.txt"

    # execute part 1
    part1(raw_file)


def part1(raw_file: str) -> None:
    """
    implements the homework part 1
    :param raw_file: the expenses.txt filename
    :return: None
    """
    # a
    print_part_break(1, 'a')
    records = []
    with open(raw_file, 'r') as fd:
        for line in fd:
            records.append(remove_newline_break(line))
    for line in records:
        print(line)

    # b
    print_part_break(1, 'b')
    with open(raw_file, 'r') as fd:
        records2 = [remove_newline_break(line) for line in fd]
        print("\nrecords == records2:", records == records2, '\n')

    # c
    print_part_break(1, 'c')
    with open(raw_file, 'r') as fd:
        records3 = tuple(tuple(remove_newline_break(line).split(':')) for line in fd)
        for tup in records3:
            print(tup)
        # d
        cat_set = {element[1] for element in records3 if element[1] != 'Category'}
        date_set = {element[2] for element in records3 if element[2] != 'Date'}

        print('Categories:', cat_set, '\n')
        print('Dates:     ', date_set, '\n')

        # e
        rec_num_to_record = {i: element for i, element in enumerate(records3)}
        for rn in range(len(rec_num_to_record)):
            print('{:3d}:{}'.format(rn, rec_num_to_record[rn]))

        for i in rec_num_to_record.items():
            print('{:3d}: {}'.format(i[0], i[1]))

        for k, v in rec_num_to_record.items():
            print('{:3d}: {}'.format(k, v))


def remove_newline_break(line: str) -> str:
    """
    remove the newline break from the given string.
    :param line: a string to be removed the newline break
    :return: a new string
    """
    return line.strip('\n').strip('\r\n')


def print_part_break(part: int, sub: str) -> None:
    """
    a helper to print each part of the homework
    :param part:  question part
    :param sub: sub question index
    :return: None
    """
    print('*' * 80, f'Part {part}, {sub}', '*' * 80, sep='\n')


if __name__ == '__main__':
    main()
