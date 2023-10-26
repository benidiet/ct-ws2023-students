import random

def throw():
    """
    Throws a dice.

    Parameters:
        None

    Returns:
        (int): A random number between 1 and 6 (including both).
    """
    return random.randint(1, 6)