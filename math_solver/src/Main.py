from Syntax.Lexer import Lexer
from Syntax.Parser import Parser, ParserNode
from Syntax.Token import Token

def print_parser_node(node: ParserNode or Token, indent = "", is_last = True):
    marker = "└──" if is_last else "├──"

    if isinstance(node, Token):
        print(indent + marker + str(node.kind) + f"({node.pos}:{node.len})")
    
    else:
        print(indent + marker + node.__class__.__name__)

        indent += "    " if is_last else "│   "
        
        last_child = node.get_childrens()[-1]
        for child in node.get_childrens():
            print_parser_node(child, indent, child == last_child)

if __name__ == "__main__":
    text = "g(x, a, b) = a x + b = -20"
    #text = "1.1 + a"
    lexer = Lexer(text)
    lexer.lex()

    parser = Parser(lexer.tokens)
    parser.parse()

    print(text)
    print_parser_node(parser.tree)

    # for i in lexer.tokens:
    #     print(i)