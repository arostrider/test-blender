from random import random


def roundf(value: float, n: int = 4) -> float:
    return round(value, n)


def randec() -> float:
    return roundf(random())
