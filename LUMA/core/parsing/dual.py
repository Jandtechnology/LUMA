from __future__ import annotations
from typing import Optional, Union
from pathlib import Path
from functools import lru_cache

from .natural import NaturalParser
from .sexpr import SexprParser
from ..ast.base import Program
from ..exceptions import ParseError, ParserError
from ..utils import benchmark


class DualParser:
    __slots__ = ('_natural', '_sexp', '_stats')
    
    def __init__(self):
        self._natural: Optional[NaturalParser] = None
        self._sexp: Optional[SexprParser] = None
        self._stats: dict[str, Union[int, float]] = {
            'parse_time': 0.0,
            'parse_count': 0
        }

    @property
    def natural(self) -> NaturalParser:
        if self._natural is None:
            self._natural = NaturalParser()
        return self._natural

    @property
    def sexp(self) -> SexprParser:
        if self._sexp is None:
            self._sexp = SexprParser()
        return self._sexp

    @benchmark
    def parse(self, source: str, filename: Optional[Union[str, Path]] = None) -> Program:
        """
        Parse source code from a string or a file path.

        Args:
            source (str): Source code or path to a file.
            filename (str | Path, optional): Optional filename for error reporting.

        Returns:
            Program: Parsed AST.

        Raises:
            FileNotFoundError: If a given file path does not exist.
            ParserError: If an unexpected error occurs.
            ParseError: If a syntax-specific error occurs.
        """
        try:
            filepath = Path(filename) if filename else None
            if Path(source).exists():
                filepath = Path(source)
                source = filepath.read_text(encoding='utf-8')

            if self._is_sexpression(source):
                return self.sexp.parse(source, filepath)
            return self.natural.parse(source, filepath)

        except FileNotFoundError as e:
            raise FileNotFoundError(f"Source file not found: {e.filename}") from e
        except ParseError:
            raise
        except Exception as e:
            raise ParserError(f"Failed to parse: {e}") from e

    @staticmethod
    @lru_cache(maxsize=128)
    def _is_sexpression(source: str) -> bool:
        return source.lstrip().startswith('(')

    def parse_file(self, filepath: Union[str, Path]) -> Program:
        """
        Shortcut to parse source directly from a file.

        Args:
            filepath (str | Path): Path to the source file.

        Returns:
            Program: Parsed AST.
        """
        path = Path(filepath)
        return self.parse(path.read_text(encoding='utf-8'), str(path))

    @property
    def stats(self) -> dict:
        """
        Returns parsing statistics.

        Returns:
            dict: Copy of stats dictionary.
        """
        return self._stats.copy()
