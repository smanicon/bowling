from typing import TypeVar

T = TypeVar('T')


def flatten(l: [[T]]) -> [T] :
    return [x for y in l for x in y]
