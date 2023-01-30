from hypothesis import given
from hypothesis.strategies import lists

from src.bowling import calculate_bowling_score
from test.bowling_regular_frame_composite import regular_frame
from test.utils import flatten


@given(tries=lists(regular_frame()))
def test_score_of_regular_frame(tries):
    flatten_tries = flatten(tries)

    assert calculate_bowling_score(flatten_tries) == sum(flatten_tries)
