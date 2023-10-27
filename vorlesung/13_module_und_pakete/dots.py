"""
Dieses Modul implementiert das Dots Zahlensystem.
"""

def add(a, b):
    """Addiert Zahl a und b"""
    return a+b

def sub(a, b):
    """Subtrahiert a von b"""
    return a[0:max(0, len(a)-len(b))]

def div(a, b):
    """Dividiert a durch b"""
    return to_dots(int(len(a) / len(b)))

def mul(a, b):
    """Multipliziert a und b"""
    return a * len(b)

def to_dots(number):
    """Wandelt die Zahl number in dots um"""
    return '.'*number

def to_number(dots):
    """Wandelt dots in eine Zahl um"""
    return len(dots)
