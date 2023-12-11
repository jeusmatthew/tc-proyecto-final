import sys
import os
import re

# abre el archivo por medio de argumentos


def abrir_archivo():
    with open("src/factorial.mio", "r", encoding="UTF-8") as file:
        return file.read(), file.name


def analizar(codigo: str):
    """
    1. separa el codigo por lineas
    2. limpia todas las lineas 
    3. verifica la linea para saber que instruccion es
        1. si es un comentario iniciará con '#'
        2. si es un

    """
    lines = separar_lineas(codigo)
    lines = limpiar_lineas(lines)

    for index, line in enumerate(lines):
        if es_comentario(line):
            lines.pop(index)

        elif es_palabra_reservada(line):
            print(f"{line} es una palabra reservada")


def separar_lineas(raw_data: str):
    return raw_data.split("\n")


def limpiar_lineas(lines: list[str]):
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
    return lines


def es_comentario(line: str):
    return line[0] == "#"


def es_palabra_reservada(line: str):
    # PROGRAMA
    # FINPROG
    # SI
    # ENTONCES
    # SINO
    # FINSI
    # REPITE
    # VECES
    # FINREP
    # IMPRIME
    # LEE
    reserved_words = ["PROGRAMA", "FINPROG", "SI", "ENTONCES",
                      "SINO", "FINSI", "REPITE", "VECES", "FINREP", "IMPRIME", "LEE"]

    return line in reserved_words


def main():
    # variables
    read_data = ""
    word_list = []

    # abre el archivo
    read_data, filename = abrir_archivo()
    filename = os.path.splitext(filename)[0]
    fileOut = open(f"{filename}.lex", "w")

    analizar(read_data)


if __name__ == "__main__":
    main()
