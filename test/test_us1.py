import pytest
import sys
#sys.path.append("../src")
from src import user_story_1
from src import data_creation

#non reproducable test, point is to try with many entries
def test_mass():
    correct=data_creation.create_entries_mass(5000,'../data/test_mass.txt')
    results=user_story_1.parse_scan('../data/test_mass.txt')
    for j in range(len(results)):
        assert results[0][j]==correct[0][j]

