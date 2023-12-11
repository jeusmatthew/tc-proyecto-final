import re


def is_valid_identifier(token):
    # Verifica si el token es un identificador válido
    return re.match(r'^[a-zA-Z][a-zA-Z0-9]{0,15}$', token)


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
    keywords = set(['PROGRAMA', 'FINPROG', 'SI', 'ENTONCES', 'SINO',
                   'FINSI', 'REPITE', 'VECES', 'FINREP', 'IMPRIME', 'LEE'])
    relational_operators = set(['>', '<', '=='])
    arithmetic_operators = set(['+', '-', '*', '/'])

    lines = input_code.split('\n')
    tokens = []

    for line_number, line in enumerate(lines, start=1):
        # Eliminar comentarios
        line = re.sub(r'#.*$', '', line)

        # Tokenizar la línea
        # Expresión regular para tokenizar
        for token in re.findall(r'[A-Za-z0-9]+|\"[^\"]+\"|==|>|<|=|[-+*/]', line):
            if token in keywords:   
                tokens.append(token) # (tipo, token, línea) va añadiendo cada linea a la lista
            elif token in relational_operators:
                tokens.append(token)
            elif token in arithmetic_operators:
                tokens.append(token)
            elif token == '=':
                tokens.append(token)
            elif is_valid_identifier(token):
                tokens.append("[id]")
            elif is_valid_text_literal(token):
                tokens.append("[txt]")
            elif is_valid_numeric_literal(token):
                tokens.append("[val]")
            else:
                print(
                    f"Error en la línea {line_number}: Unidad léxica no válida '{token}'")
                return False

    with open('./programa.lex', 'w', encoding='utf-8') as lex_file:
        for token in tokens:
            lex_file.write(f"{token}\n")

    return True


def main():
    # Ejemplo de uso
    input_code = u"""
    * Programa que calcula el factorial de un número
    DSJSÑADFKLJFMKASDLJ 
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
