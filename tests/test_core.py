from traffic_analyzer import core


SAMPLE_FILE = "tests/data/sample/traffic_sample.csv"


def test_maximum_traffic_returns_integer():
    assert isinstance(core.maximum_traffic(SAMPLE_FILE), int)


def test_maximum_traffic_is_not_negative():
    assert core.maximum_traffic(SAMPLE_FILE) >= 0


def test_longest_jam_returns_integer():
    assert isinstance(core.longest_jam(SAMPLE_FILE), int)


def test_longest_jam_is_not_negative():
    assert core.longest_jam(SAMPLE_FILE) >= 0


def test_number_of_jams_is_not_negative():
    assert core.nm_of_jams(SAMPLE_FILE) >= 0


def test_empty_measurement_ratio_is_between_zero_and_one():
    result = core.nm_of_empty_measurements(SAMPLE_FILE)
    assert 0 <= result <= 1


def test_average_cars_per_hour_is_not_negative():
    result = core.average_cars_per_hour(SAMPLE_FILE, 8)
    assert result >= 0


