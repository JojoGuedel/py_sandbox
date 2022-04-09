from Diagnostics.DiagnosticBag import DiagnosticBag
from Syntax.Lexer import Lexer
from Syntax.Parser import Parser, SyntaxNode
from Syntax.Node.Token import Token

def print_parser_node(node: SyntaxNode or Token, indent = "", is_last = True):
    marker = "└──" if is_last else "├──"

    if isinstance(node, Token):
        print(indent + marker + str(node))
    
    else:
        print(indent + marker + str(node))

        indent += "    " if is_last else "│   "
        
        last_child = node.children()[-1]
        for child in node.children():
            print_parser_node(child, indent, child == last_child)

if __name__ == "__main__":
    # text = "g(x, a, b)) a b c = 1b 2"
    text = "=>"
    print(text, end="\n\n")

    diagnostics = DiagnosticBag(text)
    lexer = Lexer(text, diagnostics)
    lexer.lex()

    parser = Parser(lexer.tokens, diagnostics)
    parser.parse()

    if diagnostics.any():
        diagnostics.print()
    else:
        print_parser_node(parser.tree)

    # print_parser_node(parser.tree)

    # for i in lexer.tokens:
    #     print(i)