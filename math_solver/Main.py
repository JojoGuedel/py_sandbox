from Syntax.Lexer import Lexer

if __name__ == "__main__":
    lexer = Lexer("g(x) = ax + b + atan2(1, 2)")
    lexer.lex()

    for i in lexer.tokens:
        print(i)