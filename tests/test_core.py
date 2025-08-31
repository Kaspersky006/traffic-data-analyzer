import os
from traffic_analyzer import core

sample_file = os.path.join(os.path.dirname(__file__), "data/sample/traffic_sample.txt")

def test_maximum_traffic():
    assert core.maximum_traffic(sample_file) >= 0

def test_longest_jam():
    assert isinstance(core.longest_jam(sample_file), int)

def test_nm_of_jams():
    assert core.nm_of_jams(sample_file) >= 0



