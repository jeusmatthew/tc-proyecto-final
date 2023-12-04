import re

def analizador_lexico(entrada):
    # Definir las expresiones regulares para cada tipo de token
    patrones = [
        (r'PROGRAMA', 'PROGRAMA'),
        (r'FINPROG', 'FINPROG'),
        (r'SI', 'SI'),
        (r'ENTONCES', 'ENTONCES'),
        (r'SINO', 'SINO'),
        (r'FINSI', 'FINSI'),
        (r'REPITE', 'REPITE'),
        (r'VECES', 'VECES'),
        (r'FINREP', 'FINREP'),
        (r'IMPRIME', 'IMPRIME'),
        (r'LEE', 'LEE'),
        (r'#.*', 'COMENTARIO'),
        (r'>', 'OP_REL_MAYOR'),
        (r'<', 'OP_REL_MENOR'),
        (r'==', 'OP_REL_IGUAL'),
        (r'=', 'ASIGNACION'),
        (r'\+', 'OP_ARIT_SUMA'),
        (r'-', 'OP_ARIT_RESTA'),
        (r'\*', 'OP_ARIT_MULTIPLICACION'),
        (r'/', 'OP_ARIT_DIVISION'),
        (r'0x[0-9A-Fa-f]+', 'LITERAL_NUMERICA'),
        (r'"[^"]*"', 'LITERAL_TEXTO'),
        (r'[a-zA-Z][a-zA-Z0-9]{0,15}', 'IDENTIFICADOR'),
        (r'\b\d+\b', 'LITERAL_NUMERICA_DECIMAL')
    ]

    # Inicializar la tabla de símbolos
    ids = {}
    txt = {}
    val = {}

    # Leer el archivo de entrada
    with open(entrada, 'r') as archivo:
        lineas = archivo.readlines()

    # Inicializar el contador de líneas
    num_linea = 0

    # Procesar cada línea del archivo
    for linea in lineas:
        num_linea += 1
        for patron, tipo_token in patrones:
            matches = re.finditer(patron, linea)
            for match in matches:
                valor = match.group(0)
                if tipo_token == 'IDENTIFICADOR':
                    if valor not in ids:
                        ids[valor] = f'ID{len(ids) + 1:02d}'
                elif tipo_token == 'LITERAL_TEXTO':
                    if valor not in txt:
                        txt[valor] = f'TX{len(txt) + 1:02d}'
                elif tipo_token == 'LITERAL_NUMERICA':
                    valor_decimal = int(valor, 16)
                    if valor not in val:
                        val[valor] = f'{valor_decimal}'
                elif tipo_token == 'COMENTARIO':
                    break  # No almacenar comentarios en la tabla de símbolos
                print(f'{tipo_token}\t{valor}\t{num_linea}')

    # Escribir las tablas de símbolos en archivos
    with open('programa.sim', 'w') as sim_file:
        # Escribir la tabla de identificadores
        for valor, clave in ids.items():
            sim_file.write(f'{valor}\t{clave}\n')

        # Escribir la tabla de literales de texto
        for valor, clave in txt.items():
            sim_file.write(f'{valor}\t{clave}\n')

        # Escribir la tabla de literales numéricas
        for valor, clave in val.items():
            sim_file.write(f'{valor}\t{clave}\n')

if __name__ == '__main__':
    analizador_lexico('factorial.mio')
