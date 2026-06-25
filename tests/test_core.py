import os
from traffic_analyzer import core

sample_file = "tests/data/sample/traffic_sample.csv"

def test_maximum_traffic():
    assert core.maximum_traffic(sample_file) >= 0

def test_longest_jam():
    assert isinstance(core.longest_jam(sample_file), int)

def test_nm_of_jams():
    assert core.nm_of_jams(sample_file) >= 0



