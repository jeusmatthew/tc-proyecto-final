import sys
import os
import re
import AnalizadorLexico as al

# abre el archivo por medio de argumentos
def open_file():
    with open("src/factorial.mio", "r", encoding="UTF-8") as file:
        return file.read(), file.name

def main():
    # variables
    read_data = ""
    word_list = []

    # abre el archivo
    read_data, filename = open_file()
    filename = os.path.splitext(filename)[0]
    fileOut = open(f"{filename}.lex", "w")

    al.analizar(read_data)


if __name__ == "__main__":
    main()
