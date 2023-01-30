from src.bowling import calculate_bowling_score


def test_1_then_5_pins_knocked_down_give_6_points():
    pins_knocked_down = [1, 5]

    score = calculate_bowling_score(pins_knocked_down)

    assert score == 6


def test_3_then_5_pins_knocked_down_give_8_points():
    pins_knocked_down = [3, 5]

    score = calculate_bowling_score(pins_knocked_down)

    assert score == 8


def test_start_with_spare_then_third_throw_counts_double():
    pins_knocked_down = [5, 5, 3, 5]

    score = calculate_bowling_score(pins_knocked_down)

    assert score == 21


def test_start_with_strike_then_third_and_fourth_throws_count_double():
    tries_pins_knocked_down = [10, 5, 3]

    score = calculate_bowling_score(tries_pins_knocked_down)

    assert score == 26
