import pytest
from src import user_story_2
from src import main
from src import user_story_4

@pytest.fixture
def results():
    results=[['123456789',True],['123456780', 'AMB'],['000000000',True],['711111111',True],['222222222', 'ERR'],['333393333',True],['444444444', 'ERR'],['555555555', 'AMB'],
             ['666666666', 'AMB'],['777777177',True],['888888888', 'AMB'],['999999999', 'AMB'],['ABEDEF000',True],['A?CD?F?00', 'AMB']]
    return results


def test_something(results):
    assert main.main('../data/test.txt','results.txt') == results


