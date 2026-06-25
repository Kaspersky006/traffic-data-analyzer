from pathlib import Path


def read_lines(filepath: str) -> list[str]:
    """Read traffic data from a file and return all lines."""
    return Path(filepath).read_text().splitlines()


def average_cars_per_hour(filepath: str, hour: int) -> float:
    """Calculate the average number of cars for a selected hour."""
    lines = read_lines(filepath)
    selected_hour = str(hour).zfill(2)

    hourly_lines = [line for line in lines if line.startswith(selected_hour)]

    if not hourly_lines:
        return 0.0

    total_cars = sum(line.count(">") for line in hourly_lines)
    return total_cars / len(hourly_lines)


def nm_of_empty_measurements(filepath: str) -> float:
    """Calculate the ratio of measurements without any cars."""
    lines = read_lines(filepath)

    if not lines:
        return 0.0

    empty_lines = sum(1 for line in lines if ">" not in line)
    return empty_lines / len(lines)


def maximum_traffic(filepath: str) -> int:
    """Find the maximum number of cars in a single measurement."""
    lines = read_lines(filepath)

    if not lines:
        return 0

    return max(line.count(">") for line in lines)


def nm_of_jams(filepath: str) -> int:
    """Count traffic jams, where a jam is three or more cars in a row."""
    lines = read_lines(filepath)
    return sum(line.count(">>>") for line in lines)


def longest_jam(filepath: str) -> int:
    """Find the longest continuous traffic jam."""
    lines = read_lines(filepath)

    longest_streak = 0

    for line in lines:
        current_streak = 0

        for char in line:
            if char == ">":
                current_streak += 1
                longest_streak = max(longest_streak, current_streak)
            else:
                current_streak = 0

    return longest_streak
