import re

string = "este es una prueba\nhola               \tdef main"
tokens = []

tokens = re.split(r"[\n\t ]+", string)
print(tokens)