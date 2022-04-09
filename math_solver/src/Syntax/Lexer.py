from Syntax.Node.Token import Token
from Syntax.TokenKind import TokenKind


class Lexer:
    text: str
    pos: int
    tokens: list[Token]

    def __init__(self, text: str):
        self._text = text
        self._pos = 0
        self.tokens = []

    def _current_char(self) -> str:
        if self._pos >= 0 and self._pos < len(self._text):
            return self._text[self._pos]

        else:
            return "\0"

    def _lex_num(self):
        start = self._pos
        float = False

        while True:
            if str.isdigit(self._current_char()):
                self._pos += 1

            elif self._current_char() == ".":
                if float > True:
                    break

                float = True
                self._pos += 1

            else:
                break

        self.tokens.append(Token(TokenKind.Number, start, self._pos - start))

    def _lex_literal(self):
        start = self._pos

        while True:
            if str.isalpha(self._current_char()) or self._current_char() == '_' or str.isdigit(self._current_char()):
                self._pos += 1

            elif self._current_char() == '(':
                self.tokens.append(Token(TokenKind.FunctionName, start, self._pos - start))
                return

            else:
                break

        self.tokens.append(Token(TokenKind.Literal, start, self._pos - start))

    def _lex_space(self):
        start = self._pos

        while str.isspace(self._current_char()):
            self._pos += 1

        # self.tokens.append(Token(TokenKind.Space, start, self._pos - start));

    def lex(self):
        self.tokens.clear()

        while True:
            if self._current_char() == "\0":
                self.tokens.append(Token(TokenKind.End, self._pos, 1))
                break

            elif self._current_char() == "+":
                self.tokens.append(Token(TokenKind.Plus, self._pos, 1))
                self._pos += 1

            elif self._current_char() == '-':
                self.tokens.append(Token(TokenKind.Minus, self._pos, 1))
                self._pos += 1

            elif self._current_char() == "*":
                self.tokens.append(Token(TokenKind.Star, self._pos, 1))
                self._pos += 1

            elif self._current_char() == "/":
                self.tokens.append(Token(TokenKind.Slash, self._pos, 1))
                self._pos += 1

            elif self._current_char() == "=":
                self.tokens.append(Token(TokenKind.Equal, self._pos, 1))
                self._pos += 1

            elif self._current_char() == "^":
                self.tokens.append(Token(TokenKind.Pow, self._pos, 1))
                self._pos += 1

            elif self._current_char() == "(":
                self.tokens.append(Token(TokenKind.LParen, self._pos, 1))
                self._pos += 1

            elif self._current_char() == ")":
                self.tokens.append(Token(TokenKind.RParen, self._pos, 1))
                self._pos += 1

            elif self._current_char() == ",":
                self.tokens.append(Token(TokenKind.Comma, self._pos, 1))
                self._pos += 1

            elif str.isdigit(self._current_char()):
                # if self.tokens.last().kind == TokenKind.Number or self.tokens.last().kind == TokenKind.Literal:
                #     kind = TokenKind.Star
                self._lex_num()

            elif str.isalpha(self._current_char()):
                self._lex_literal()

            elif str.isspace(self._current_char()):
                self._lex_space()

            else:
                self.tokens.append(Token(TokenKind.Invalid, self._pos, 1))
                self._pos += 1



