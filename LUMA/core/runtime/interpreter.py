from ast.base import *

class Interpreter:
    def __init__(self):
        self.environment = {
            'true': True,
            'false': False,
            'nil': None
        }
    
    def evaluate(self, node: Node):
        if isinstance(node, NumberLiteral):
            return node.value
        elif isinstance(node, Symbol):
            return self.environment.get(node.name)
        elif isinstance(node, ListExpr):
            if not node.elements:
                return None
            head = self.evaluate(node.elements[0])
            if callable(head):
                return head(*[self.evaluate(x) for x in node.elements[1:]])
            return [self.evaluate(x) for x in node.elements]
        elif isinstance(node, CognitiveDefinition):
            self.environment[node.name] = node
            return node
        raise RuntimeError(f"Unknown node type: {type(node)}")