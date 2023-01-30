from hypothesis import given
from hypothesis.strategies import lists, integers, just, composite

from src.bowling import calculate_bowling_score
from test.bowling_regular_frame_composite import regular_frame
from test.utils import flatten


@composite
def spare_frame(draw):
    first_try = draw(integers(0, 9))
    second_try = draw(just(10 - first_try))
    return [first_try, second_try]


@given(tries=lists(regular_frame()), spare=spare_frame(), last_frame=regular_frame())
def test_score_of_spare_frame(tries, spare, last_frame):
    flatten_tries = flatten(tries + [spare, last_frame])
    assert calculate_bowling_score(flatten_tries) == sum(flatten_tries) + last_frame[0]
