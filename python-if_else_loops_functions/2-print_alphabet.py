#!/usr/bin/python3
print("".join("{:c}".format(i) for i in range(97, 123)), end="")

# "{:c}".format(i) convertit i en son caractère ASCII
# "".join(...) caractères générés et concatène en une chaîne.
# end="" empêche l'ajout d'un saut de ligne à la fin
