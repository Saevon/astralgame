def round(num, nearest = 1):
    """round(...) --> float
    Returns the rounded version of the number.
    The number rounds up if greater than half of nearest, otherwise rounds down.
    e.g. a num > 1.5, rounded to nearest 1 --> 2"""
    if num % nearest != 0:
        if (num % nearest) >= nearest / 2.0:
            num = num - (num % nearest) + nearest
        else:
            num = num - (num % nearest)
    return num
