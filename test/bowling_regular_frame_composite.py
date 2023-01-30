from hypothesis.strategies import integers, composite


@composite
def regular_frame(draw):
    first_try = draw(integers(0, 9))
    second_try = draw(integers(0, 9 - first_try))
    return [first_try, second_try]