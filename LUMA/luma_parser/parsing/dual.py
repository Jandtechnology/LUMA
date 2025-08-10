from pathlib import Path
from typing import Optional, Union
from ..ast.base import Node
from .sexp import SexpParser
from .natural import NaturalParser
from ..exceptions import ParseError
from ..ast.base import Program  # Asegúrate que este import sea correcto

class DualParser:
    """
    Parser dual para LUMA que maneja tanto sintaxis natural como S-expressions.
    """

    __slots__ = ('_sexp', '_natural')

    def __init__(self):
        self._sexp: Optional[SexpParser] = None
        self._natural: Optional[NaturalParser] = None

    @property
    def sexp(self) -> SexpParser:
        if self._sexp is None:
            self._sexp = SexpParser()
        return self._sexp

    @property
    def natural(self) -> NaturalParser:
        if self._natural is None:
            self._natural = NaturalParser()
        return self._natural

    def parse_file(self, filepath: Union[str, Path]) -> Node:
        path = Path(filepath)
        try:
            source = path.read_text(encoding='utf-8')
            return self.parse(source, str(path))
        except FileNotFoundError as e:
            raise FileNotFoundError(f"No se encontró el archivo: {filepath}") from e
        except Exception as e:
            raise ParseError(f"Error al parsear archivo {filepath}: {str(e)}") from e

    def parse(self, source: str, filename: Optional[str] = None) -> Node:
        from core.db.luma_db import guardar_programa  # Import interno para evitar circularidad

        source = source.strip()
        if not source:
            raise ParseError("El código fuente está vacío", filename=filename)

        try:
            if self._is_sexpression(source):
                parsed = self.sexp.parse(source, filename)
            else:
                parsed = self.natural.parse(source, filename)

            if isinstance(parsed, Program):
                guardar_programa(parsed.to_dict())  # Guardar automáticamente

            return parsed
        except Exception as e:
            raise ParseError(f"Error de parsing: {str(e)}", filename=filename) from e

    @staticmethod
    def _is_sexpression(source: str) -> bool:
        return bool(source.lstrip()) and source.lstrip()[0] == '('
