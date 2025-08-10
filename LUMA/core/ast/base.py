from dataclasses import dataclass
from typing import Union, List, Dict, Optional, Any
from pathlib import Path

# ───────────── Ubicación ─────────────
@dataclass
class SourceLocation:
    file: Optional[Path] = None
    line: int = 1
    column: int = 0

    def __str__(self):
        if self.file:
            return f"{self.file}:{self.line}:{self.column}"
        return f"line {self.line}, column {self.column}"

    def to_dict(self):
        return {
            "file": str(self.file) if self.file else None,
            "line": self.line,
            "column": self.column
        }

# ───────────── Nodo base ─────────────
@dataclass
class Node:
    location: SourceLocation
    meta: Optional[Dict[str, Any]] = None

    def __post_init__(self):
        if self.meta is None:
            self.meta = {}

    def to_dict(self):
        raise NotImplementedError("Subclases deben implementar to_dict()")

# ───────────── Expresiones ─────────────
@dataclass
class Expression(Node):
    pass

@dataclass
class Literal(Expression):
    value: Union[str, int, float, bool]

    def to_dict(self):
        return {
            "type": "Literal",
            "value": self.value,
            "location": self.location.to_dict()
        }

@dataclass
class Symbol(Expression):
    name: str

    def to_dict(self):
        return {
            "type": "Symbol",
            "name": self.name,
            "location": self.location.to_dict()
        }

@dataclass
class ListExpr(Expression):
    elements: List[Expression]

    def to_dict(self):
        return {
            "type": "ListExpr",
            "elements": [e.to_dict() for e in self.elements],
            "location": self.location.to_dict()
        }

# ───────────── Programa ─────────────
@dataclass
class Program(Node):
    statements: List[Node]

    def to_dict(self):
        return {
            "type": "Program",
            "statements": [stmt.to_dict() for stmt in self.statements],
            "location": self.location.to_dict()
        }
