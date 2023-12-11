import re

from xml.sax.saxutils import prepare_input_source

# def open


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
    id_counter = 0
    txt_literals = []
    txt_counter = 0
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
                if token not in identifiers:
                    id_counter += 1
                    identifiers.append(f"{token}, ID{id_counter:02}")
            elif is_valid_text_literal(token):
                tokens.append("[txt]")
                if token not in txt_literals:
                    txt_literals.append(f"{token}, TXT{txt_counter:02}")
            elif is_valid_numeric_literal(token):
                tokens.append("[val]")
                if token not in numeric_literals:
                    numeric_literals.append(f"{token}, {int(token, 16)}")
            else:
                print(
                    f"Error en la línea {line_number}: Unidad léxica no válida '{token}'")
                return False
            # previous_token = token

    with open('./programa.lex', 'w', encoding='utf-8') as lex_file:
        for token in tokens:
            lex_file.write(f"{token}\n")

    with open('./programa.sim', 'w', encoding='utf-8') as sim_file:
        sim_file.write("IDS\n")
        sim_file.write('\n'.join(identifiers) + '\n\n')

        sim_file.write("TXT\n")
        sim_file.write('\n'.join(txt_literals) + '\n\n')

        sim_file.write("VAL\n")
        sim_file.write('\n'.join(numeric_literals) + '\n')


    return True


def main():
    # Ejemplo de uso
    input_code = u"""
    #* Programa que calcula el factorial de un número
    #DSJSÑADFKLJFMKASDLJ 
    PROGRAMA
    # VarX acumula los productos por iteración
    VarX = 0x1
    # VarY contiene el iterador del factor
    VarY = 0x0
    LEE Num
    #  Aplica Num! = 1 * 2 * 3 * ... * Num
    REPITE NumVECES
    VarY = VarY + 0x1
    VarX = VarX * VarY
    FINREP
    IMPRIME “Factorial de ”
    IMPRIME Num
    IMPRIME “ es “
    IMPRIME VarX
    FINPROG 
    """

    if lexical_analysis(input_code):
        print("Análisis sintáctico completado.")


if __name__ == '__main__':
    main()
