from hypothesis import given, event
from hypothesis.strategies import lists, integers, composite, just
from src.bowling import calculate_bowling_score
from typing import TypeVar


@composite
def regular_frame(draw):
    first_try = draw(integers(0, 9))
    second_try = draw(integers(0, 9 - first_try))
    return [first_try, second_try]


#-------------------------

@given(tries=lists(regular_frame()))
def test_score_of_regular_frame(tries):
    flatten_tries = flatten(tries)
    event("tries length : %i" % len(flatten_tries))
    assert calculate_bowling_score(flatten_tries) == sum(flatten_tries)

#-----------------------

@composite
def spare_frame(draw):
    first_try = draw(integers(0, 9))
    second_try = draw(just(10 - first_try))
    return [first_try, second_try]


@composite
def strike_frame(draw):
    first_try = draw(just(10))
    return [first_try]


@given(tries=lists(regular_frame()), spare=spare_frame(), last_frame=regular_frame())
def test_score_of_spare_frame(tries, spare, last_frame):
    flatten_tries = flatten(tries + [spare, last_frame])
    assert calculate_bowling_score(flatten_tries) == sum(flatten_tries) + last_frame[0]


@given(tries=lists(regular_frame()), strike=strike_frame(), last_frame=regular_frame())
def test_score_of_strike_frame(tries, strike, last_frame):
    flatten_tries = flatten(tries + [strike, last_frame])
    assert calculate_bowling_score(flatten_tries) == sum(flatten_tries) + sum(last_frame)


T = TypeVar('T')


def flatten(l: [[T]]) -> [T] :
    return [x for y in l for x in y]
