import sys
import os

# abre el archivo por medio de argumentos
def open_file():
    try:
        # file = open(sys.argv[1], encoding="utf-8") # para ejecutar desde consola
        file = open("src/factorial.mio", encoding="utf-8")
        return file
    except:
        print("Error opening the file!!!")
        sys.exit()

def main():
    # variables
    read_data = ""
    word_list = []

    # abre el archivo
    fileIn = open_file()
    filename = os.path.splitext(fileIn.name)[0]
    fileOut = open(f"{filename}.lex", "w")
    read_data = fileIn.read()

    # separacion de palabras
    word_list = read_data.split("\n")
    print(word_list)    
    fileIn.close()

    # analisis lexico
    


if __name__ == "__main__":
    main()
