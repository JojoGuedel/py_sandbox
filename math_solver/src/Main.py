from Diagnostics.DiagnosticBag import DiagnosticBag
from Evaluation.Node.AddExpression import AddExpression
from Evaluation.Node.Expression import Expression
from Evaluation.Node.MultExpression import MultExpression
from Evaluation.Node.NumberExpression import NumberExpression
from Evaluation.Node.VariableExpression import VariableExpression
from Evaluation.Simplifier import Simplifier
from Syntax.Lexer import Lexer
from Syntax.Parser import Parser, SyntaxNode
from Syntax.Node.Token import Token

def print_parser_node(node: SyntaxNode, indent = "", is_last = True):
    marker = "└──" if is_last else "├──"

    print(indent + marker + str(node))

    if not isinstance(node, Token):
        print(indent + marker + str(node))

        indent += "    " if is_last else "│   "
        
        last_child = node.children()[-1]
        for child in node.children():
            print_parser_node(child, indent, child == last_child)

def print_ir_node(node: Expression, indent = "", is_last = True):
    marker = "└──" if is_last else "├──"

    print(indent + marker + str(node))

    if not isinstance(node, (NumberExpression, VariableExpression)) > 0:
        indent += "    " if is_last else "│   "
        
        last_child = node.children()[-1]
        for child in node.children():
            print_ir_node(child, indent, child == last_child)

if __name__ == "__main__" and False:
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

if __name__ == "__main__":
    expr = MultExpression(VariableExpression("a"), AddExpression(NumberExpression(5), AddExpression(VariableExpression("b"), VariableExpression("c"))))
    simplifier = Simplifier(expr)
    flattened_expr = simplifier.flatten()
    print_ir_node(flattened_expr)