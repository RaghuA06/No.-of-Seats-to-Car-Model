# Raghu Alluri
# April 2020

from typing import TextIO, Dict, List

# A car-rental weekly-price file is a .txt file that contains information about
# the cost of renting a car for one week in Toronto.
#
# Information about each rental option is given on four consecutive lines in
# the file, in the order:
#     rental-category
#     car-model
#     number-of-seats
#     quoted-weekly-rental-price
#
# Data has be gathered from many car rental companies.
#
# There are no blank lines in a car-rental weekly-price file.  All
# number-of-seats values can be converted to type int and all
# quoted-weekly-rental-price values can be converted to type float.
#
# For an example rent file, see final_q1_car_rental.txt
#
# Note that more than one company could rent the same car-model and they could
# quote different prices for a weekly rental.


def build_seats_to_models(car_rental_file: TextIO) -> Dict[int, List[str]]:
    """Return a dictionary with data from car_rental_file in which each key
    is a number of seats and each value a list of all car models available
    with that number of seats.

    Note: All car models in the values list are to be unique and should appear
    in the same order as they first appear in car_rental_file.

    >>> f = open('final_q1_car_rental.txt')
    >>> result = build_seats_to_models(f)
    >>> result == {
    ... 4: ['Chevrolet Spark', 'Hyundai Accent'],
    ... 7: ['Dodge Grand Caravan'],
    ... 5: ['Ford Escape', 'Ford Edge', 'Kia Rio', 'Hyundai Tucson']}
    True
    >>> f.close()
    """
    seats_to_model = {}
    raw_data = []
    for line in car_rental_file:
        raw_data.append(line.strip())

    lst = []
    i = 1
    while i < len(raw_data):
        car = raw_data[i:i + 1][0]
        seats = raw_data[i + 1]
        block = [car, seats]
        lst.append(block)

        i = i + 4

    keys = []
    for block in lst:
        if block[1] not in keys:
            keys.append(block[1])

    for seats in keys:
        seats_to_model[int(seats)] = []

    for seats in keys:
        for block in lst:
            if block[1] == seats:
                if block[0] not in seats_to_model[int(seats)]:
                    seats_to_model[int(seats)].append(block[0])

    return seats_to_model
    


#f = open('car_rental_data.txt')
#print(build_seats_to_models(f))
#f.close()
