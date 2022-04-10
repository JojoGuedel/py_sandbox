from cgitb import text
from Analyzer import Analyzer
from Diagnostics.DiagnosticBag import DiagnosticBag
from Evaluation.Node.AddExpression import AddExpression
from Evaluation.Node.Expression import Expression
from Evaluation.Node.MultExpression import MultExpression
from Evaluation.Node.NumberExpression import NumberExpression
from Evaluation.Node.VariableExpression import VariableExpression
from Evaluation.Simplifier import Simplifier
from Syntax.Lexer import Lexer
from Syntax.Parser import Parser, SyntaxNode
from Syntax.Node.SyntaxToken import SyntaxToken

def print_parser_node(node: SyntaxNode, indent = "", is_last = True):
    marker = "└──" if is_last else "├──"

    print(indent + marker + str(node))

    if not isinstance(node, SyntaxToken):
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

if __name__ == "__main__":
    text = "(a + b) (a + b)"
    analyzer = Analyzer(text)
    
    bound_tree = analyzer.analyze()
    # print_parser_node(analyzer.parser_tree)

    if analyzer.diagnostics.any():
        analyzer.diagnostics.print()
    else:
        print(text)
        print_ir_node(bound_tree)

if __name__ == "__main__" and False:
    text = "g(x, a, b) a b c = 1b 2"
    print(text)

    diagnostics = DiagnosticBag(text)
    lexer = Lexer(text, diagnostics)
    lexer.lex()

    parser = Parser(lexer.tokens, diagnostics)
    parser.parse()

    if diagnostics.any():
        diagnostics.print()
    else:
        print_parser_node(parser.tree)

if __name__ == "__main__" and False:
    expr = MultExpression(VariableExpression("a"), AddExpression(NumberExpression(5), AddExpression(VariableExpression("b"), VariableExpression("c"))))
    simplifier = Simplifier(expr)
    flattened_expr = simplifier.flatten()
    print_ir_node(flattened_expr)