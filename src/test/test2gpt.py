import re

# Definir patrones regulares para identificar las unidades léxicas
patron_programa = re.compile(r'\bPROGRAMA\b')
patron_finprog = re.compile(r'\bFINPROG\b')
# Agrega otros patrones para las palabras reservadas, operadores, identificadores, literales, etc.

# Inicializar listas para almacenar tokens
tokens = []
errores = []

# Contadores para las claves alfanuméricas consecutivas
id_contador = 1
txt_contador = 1

# Leer el archivo de entrada
with open('src/factorial.lex', encoding="UTF-8") as archivo:
    for numero_linea, linea in enumerate(archivo, 1):
        # Eliminar comentarios y dividir la línea en palabras
        palabras = re.split(r'\s', linea.split('#')[0].strip())
        
        for palabra in palabras:
            # Verificar si la palabra coincide con algún patrón
            if patron_programa.match(palabra):
                tokens.append(('PROGRAMA', None))
            elif patron_finprog.match(palabra):
                tokens.append(('FINPROG', None))
            # Agrega más condiciones para otros patrones

            # Si no coincide con ningún patrón, es un error
            else:
                errores.append(f"Error en la línea {numero_linea}: '{palabra}' no es válido.")

# Escribir tokens en archivo de salida
with open('programa.lex', 'w') as archivo_lex:
    for token in tokens:
        archivo_lex.write(f"{token[0]}\n")

# Escribir tabla de símbolos en archivo de salida
with open('programa.sim', 'w') as archivo_sim:
    # Agrega secciones para IDS, TXT, VAL
    # IDS
    for token in tokens:
        if token[0] == 'IDS':
            archivo_sim.write(f"{token[1]}\tID{id_contador}\n")
            id_contador += 1
    # TXT
    for token in tokens:
        if token[0] == 'TXT':
            archivo_sim.write(f"{token[1]}\tTX{txt_contador}\n")
            txt_contador += 1
    # VAL
    # Agrega código para la sección VAL

# Imprimir errores
for error in errores:
    print(error)
