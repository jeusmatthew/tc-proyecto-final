def __split_lines(raw_data: str):
    return raw_data.split("\n")


def __clean_lines(lines: list[str]):
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
    return lines


def __is_comment(line: str):
    return line[0] == "#"


def __is_reserved_word(line: str):
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


def analizar(codigo: str):
    """
    1. separa el codigo por lineas
    2. limpia todas las lineas 
    3. verifica la linea para saber que instruccion es
        1. si es un comentario iniciará con '#'
        2. si es un

    """
    lines = __split_lines(codigo)
    lines = __clean_lines(lines)

    for index, line in enumerate(lines):
        if __is_comment(line):
            lines.pop(index)
        
        elif __is_reserved_word(line):
            print(f"{line} es una palabra reservada")
