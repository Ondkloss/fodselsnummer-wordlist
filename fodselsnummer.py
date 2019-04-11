# Based on https://no.wikipedia.org/wiki/F%C3%B8dselsnummer


def create_fodselsnummer_wordlist(days, months, years):
    result = ''
    for day in days:
        for month in months:
            for year in years:
                for individual in range(0, 999):
                    fodselsnummer = create_fodselsnummer(day, month, year, individual)

                    if fodselsnummer is not None:
                        result += fodselsnummer + '\n'

    with open('fodselsnummer.txt', 'w') as file:
        file.write(result)


def create_fodselsnummer(day, month, year, individual):
    if day < 1 or day > 31:
        return None
    if month < 1 or month > 12:
        return None
    if year < 0 or year > 99:
        return None
    if individual < 0 or individual > 999:
        return None

    d1 = get_xth_digit(day, 2)
    d2 = get_xth_digit(day, 1)
    m1 = get_xth_digit(month, 2)
    m2 = get_xth_digit(month, 1)
    y1 = get_xth_digit(year, 2)
    y2 = get_xth_digit(year, 1)
    i1 = get_xth_digit(individual, 3)
    i2 = get_xth_digit(individual, 2)
    i3 = get_xth_digit(individual, 1)

    control_digit_1 = calculate_control_digit_1(d1, d2, m1, m2, y1, y2, i1, i2, i3)
    if control_digit_1 == 10:
        return None
    c1 = control_digit_1

    control_digit_2 = calculate_control_digit_2(d1, d2, m1, m2, y1, y2, i1, i2, i3, c1)
    if control_digit_2 == 10:
        return None
    c2 = control_digit_2

    return str(d1) + str(d2) + str(m1) + str(m2) + str(y1) + str(y2) + str(i1) + str(i2) + str(i3) + str(c1) + str(c2)


def calculate_control_digit_1(d1, d2, m1, m2, y1, y2, i1, i2, i3):
    result = 11 - (((3 * d1) + (7 * d2) + (6 * m1) + (1 * m2) + (8 * y1) + (9 * y2) + (4 * i1) + (5 * i2) + (2 * i3)) % 11)

    if result == 11:
        return 0
    return result


def calculate_control_digit_2(d1, d2, m1, m2, y1, y2, i1, i2, i3, c1):
    result = 11 - (((5 * d1) + (4 * d2) + (3 * m1) + (2 * m2) + (7 * y1) + (6 * y2) + (5 * i1) + (4 * i2) + (3 * i3) + (2 * c1)) % 11)

    if result == 11:
        return 0
    return result


def get_xth_digit(number, digit):
    if len(str(number)) < digit:
        return 0

    return int(str(number)[len(str(number)) - digit])


if __name__ == "__main__":
    create_fodselsnummer_wordlist(range(1, 32), range(1, 13), range(0, 100))
