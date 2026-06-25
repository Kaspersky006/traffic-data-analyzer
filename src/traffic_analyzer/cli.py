import argparse

from traffic_analyzer.core import (
    average_cars_per_hour,
    nm_of_empty_measurements,
    maximum_traffic,
    nm_of_jams,
    longest_jam,
)


def main():
    parser = argparse.ArgumentParser(
        description="Traffic Data Analyzer"
    )

    parser.add_argument(
        "filepath",
        help="Path to the traffic data file"
    )

    parser.add_argument(
        "--hour",
        type=int,
        default=8,
        help="Hour to calculate average traffic"
    )

    args = parser.parse_args()

    print("\n========== Traffic Analysis ==========\n")

    print(f"Average cars at {args.hour}:00 : "
          f"{average_cars_per_hour(args.filepath, args.hour):.2f}")

    print(f"Empty measurements      : "
          f"{nm_of_empty_measurements(args.filepath):.2%}")

    print(f"Maximum traffic         : "
          f"{maximum_traffic(args.filepath)}")

    print(f"Number of traffic jams  : "
          f"{nm_of_jams(args.filepath)}")

    print(f"Longest traffic jam     : "
          f"{longest_jam(args.filepath)} cars")


if __name__ == "__main__":
    main()

