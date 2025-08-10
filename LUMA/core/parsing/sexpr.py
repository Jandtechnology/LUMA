from sexpdata import loads, Symbol
from core.ast.base import Program, Node

class SexprParser:
    def parse(self, source, filename=None) -> Program:
        def transform(sexp):
            if isinstance(sexp, list) and len(sexp) > 0:
                head = sexp[0]
                if head == Symbol('define-concept'):
                    return Node(kind='concept', name=str(sexp[1]))
            return Node(kind='unknown', name='')

        parsed = loads(source)
        nodes = [transform(expr) for expr in parsed]
        return Program(body=nodes)
