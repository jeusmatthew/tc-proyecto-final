class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.token_index = 0

    def consume_token(self):
        if self.token_index < len(self.tokens):
            self.current_token = self.tokens[self.token_index]
            self.token_index += 1
        else:
            self.current_token = None

    def match(self, expected_token):
        if self.current_token == expected_token:
            self.consume_token()
        else:
            print(
                f"Error de sintaxis: Se esperaba '{expected_token}' pero se encontró '{self.current_token}'")
            exit()

    def parse_PROG(self):
        self.match("PROGRAMA")
        self.match("[id]")
        self.parse_SENTS()
        self.match("FINPROG")

    def parse_SENTS(self):
        self.parse_SENT()
        while self.current_token in ["[id]", "SI", "REPITE", "IMPRIME", "LEE", "#"]:
            self.parse_SENT()

    def parse_SENT(self):
        if self.current_token == "[id]":
            self.match("[id]")
            self.match("=")
            self.parse_ELEM()
            if self.current_token in ["[op_ar]"]:
                self.match("[op_ar]")
                self.parse_ELEM()
        elif self.current_token == "SI":
            self.match("SI")
            self.parse_COMPARA()
            self.match("ENTONCES")
            self.parse_SENTS()
            if self.current_token == "SINO":
                self.match("SINO")
                self.parse_SENTS()
            self.match("FINSI")
        elif self.current_token == "REPITE":
            self.match("REPITE")
            self.parse_ELEM()
            self.match("VECES")
            self.parse_SENTS()
            self.match("FINREP")
        elif self.current_token == "IMPRIME":
            self.match("IMPRIME")
            if self.current_token == "[txt]":
                self.match("[txt]")
            else:
                self.parse_ELEM()
        elif self.current_token == "LEE":
            self.match("LEE")
            self.match("[id]")
        elif self.current_token == "#":
            self.match("#")

    def parse_ELEM(self):
        if self.current_token == "[id]":
            self.match("[id]")
        elif self.current_token == "[val]":
            self.match("[val]")

    def parse_COMPARA(self):
        self.match("[id]")
        self.match("[op_rel]")
        self.parse_ELEM()


def syntax_analysis(tokens):
    parser = Parser(tokens)
    parser.consume_token()  # Inicia el análisis sintáctico consumiendo el primer token
    parser.parse_PROG()
    print("Análisis sintáctico completado.")


if __name__ == '__main__':
    with open('./programa.lex', 'r', encoding='utf-8') as lex_file:
        tokens = [line.strip() for line in lex_file.readlines()]
        syntax_analysis(tokens)
