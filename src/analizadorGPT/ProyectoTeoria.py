import re
import os

def open_file():
    with open("factorial.mio", "r", encoding="UTF-8") as file:
        return file.read(), file.name


def is_valid_identifier(token):
    # Verifica si el token es un identificador válido
    return re.match(r'^[a-zA-Z]\w{0,15}$', token)


def is_valid_text_literal(token):
    # Verifica si el token es un literal de texto válido
    return re.match(r'^"[^"]*"$', token)


def is_valid_numeric_literal(token):
    # Verifica si el token es un literal numérico válido
    return re.match(r'^(0x[0-9A-Fa-f]+|\d+)$', token)


"""
@:param input_code: Código fuente del programa a analizar
"""


def lexical_analysis(input_code: str):
    # Palabras reservadas y operadores
    keywords = set(['PROGRAMA', 'SI', 'ENTONCES', 'SINO',
                   'REPITE', 'VECES', 'IMPRIME', 'LEE', 'FINPROG', 'FINSI', 'FINREP'])

    relational_operators = set(['>', '<', '=='])
    arithmetic_operators = set(['+', '-', '*', '/'])

    # Separar el código fuente en líneas
    lines = input_code.split('\n')

    tokens = []
    identifiers = []
    txt_literals = []
    numeric_literals = []

    # previous_token = None
    for line_number, line in enumerate(lines, start=1):
        # Eliminar comentarios
        line = re.sub(r'#.*$', '', line)
        # Tokenizar la línea
        # Expresión regular para tokenizar
        for token in re.findall(r'\w+|".*"|==|>|<|=|[-+*/]', line):
            # print(f"{previous_token} -> {token}")
            if token in keywords:
                tokens.append(token)
            elif token in relational_operators:
                tokens.append("[op_rel]")
            elif token in arithmetic_operators:
                tokens.append("[op_ar]")
            elif token == '=':
                tokens.append(token)
            elif is_valid_identifier(token):
                tokens.append("[id]")
                if token not in identifiers:  # Check if identifier already exists
                    identifiers.append(token)
            elif is_valid_text_literal(token):
                tokens.append("[txt]")
                if token not in txt_literals:
                    txt_literals.append(token)
            elif is_valid_numeric_literal(token):
                tokens.append("[val]")
                if token not in numeric_literals:
                    numeric_literals.append(token)
            else:
                print(
                    f"Error en la línea {line_number}: Unidad léxica no válida '{token}'")
                return False
            # previous_token = token

    with open('./programa.lex', 'w', encoding='utf-8') as lex_file:
        for token in tokens:
            lex_file.write(f"{token}\n")

    with open('./programa.sim', 'w', encoding='utf-8') as sim_file:
        id_counter = 1
        txt_counter = 1

        sim_file.write("IDS\n")
        # sim_file.write('\n'.join(identifiers) + '\n\n')
        for index, identifier in enumerate(identifiers):
            sim_file.write(f"{identifier}, ID{index+1:02}\n")

        sim_file.write("\nTXT\n")
        for index, txt_literal in enumerate(txt_literals):
            sim_file.write(f"{txt_literal}, TX{index+1:02}\n")

        sim_file.write("\nVAL\n")
        for numeric_literal in numeric_literals:
            sim_file.write(f"{numeric_literal}, {int(numeric_literal, 16)}\n")

    return True


def main():
    input_code, filename = open_file()
    filename = os.path.splitext(filename)[0]

    if lexical_analysis(input_code):
        print("Análisis sintáctico completado.")


if __name__ == '__main__':
    main()
