class ParseError(Exception):
    """Excepción para errores de parsing."""
    
    def __init__(self, message: str, filename: str = None, line: int = None, column: int = None):
        self.filename = filename
        self.line = line
        self.column = column
        super().__init__(f"{filename+': ' if filename else ''}{message}")