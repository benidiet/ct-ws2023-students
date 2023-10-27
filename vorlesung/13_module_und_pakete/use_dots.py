#################################################
# Aufgabe                                       #
#################################################
# Importieren sie die Funktionen aus dots.py in 
# dieser Datei in den Namensbereich dots.
#
# Verwenden Sie dann die Funktionen um folgendes
# zu berechnen:
#          3 + 4 * 2
import dots as dots

result = dots.add(dots.to_dots(3), dots.mul(dots.to_dots(4), dots.to_dots(2)))
print(result)