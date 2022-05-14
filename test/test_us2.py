import pytest
from src import user_story_2
from src import user_story_1


def test_validation_second_option():
    assert user_story_2.validate('num',str(123456789))[1]== True
    assert user_story_2.validate('num',str(111111111))[1]== False
    assert user_story_2.validate('num',f"1?1111111")[1]== 'ILL'
    assert user_story_2.validate('num',f"1?1?11?11")[1]== 'ILL'
