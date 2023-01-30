def calculate_bowling_score(tries: [int]) -> int:
    if tries == []:
        return 0
    if (sum(tries[0:1]) == 10):
        return sum(tries[0:3]) + calculate_bowling_score(tries[1:])
    if (sum(tries[:2]) == 10):
        return sum(tries[0:3]) + calculate_bowling_score(tries[2:])
    return sum(tries[0:2]) + calculate_bowling_score(tries[2:])
