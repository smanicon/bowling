from hypothesis import given
from hypothesis.strategies import lists, composite, just

from src.bowling import calculate_bowling_score
from test.bowling_regular_frame_composite import regular_frame
from test.utils import flatten


@composite
def strike_frame(draw):
    first_try = draw(just(10))
    return [first_try]


@given(tries=lists(regular_frame()), strike=strike_frame(), last_frame=regular_frame())
def test_score_of_strike_frame(tries, strike, last_frame):
    flatten_tries = flatten(tries + [strike, last_frame])
    assert calculate_bowling_score(flatten_tries) == sum(flatten_tries) + sum(last_frame)
