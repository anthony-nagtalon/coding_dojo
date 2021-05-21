import random
def randInt(min=0, max=100):
    # Handles if min is greater than max
    if min > max:
        return False

    # As long as min is less than max, this should work
    # even with negative integers
    num = round((random.random() * (max - min)) + min)
    return num