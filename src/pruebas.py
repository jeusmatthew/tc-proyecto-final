
if __name__ == "__main__":
    # lectura de archivo
    
    read_data = ""
    word_list = []

    with open("in/factorial.mio") as file:
        read_data = file.read()
    

    # separacion de palabras
    word_list = read_data.split(" \n")

    

    file.close()