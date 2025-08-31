def average_cars_per_hour(filepath, hour):
    count = 0
    line_counter = 0
    with open(filepath, "r") as file:
        for line in file:
            if line[:2] == str(hour).zfill(2):
                line_counter += 1
                count += line.count(">")
    return count / line_counter if line_counter else 0


def nm_of_empty_measurements(filepath):
    nm_of_empty_lines = 0
    nm_of_lines = 0
    with open(filepath, "r") as file:
        for line in file:
            nm_of_lines += 1
            if ">" not in line:
                nm_of_empty_lines += 1
    return nm_of_empty_lines / nm_of_lines if nm_of_lines else 0


def maximum_traffic(filepath):
    maximum_nm_of_cars = 0
    with open(filepath, "r") as file:
        for line in file:
            num_of_cars = line.count(">")
            if num_of_cars > maximum_nm_of_cars:
                maximum_nm_of_cars = num_of_cars
    return maximum_nm_of_cars


def nm_of_jams(filepath):
    jam_number = 0
    with open(filepath, "r") as file:
        for line in file:
            jam_number += line.count(">>>")
    return jam_number


def longest_jam(filepath):
    long_jam = 0
    with open(filepath, "r") as file:
        for line in file:
            current_streak = 0
            for char in line:
                if char == ">":
                    current_streak += 1
                    long_jam = max(long_jam, current_streak)
                else:
                    current_streak = 0
    return long_jam


