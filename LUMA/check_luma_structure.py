#!/usr/bin/env python3
import os
import sys
from pathlib import Path
import argparse

# Configuración esperada
EXPECTED_STRUCTURE = {
    'luma_parser': {
        '__init__.py': None,
        'cli.py': None,
        'ast': {
            '__init__.py': None,
            'base.py': None,
            'cognitive.py': None,
            'emotional.py': None,
        },
        'parsing': {
            '__init__.py': None,
            'dual.py': None,
            'natural.py': None,
            'sexp.py': None,
        },
        'exceptions.py': None,
        'utils.py': None,
    },
    'setup.py': None,
    'pyproject.toml': None,
}

SAMPLE_LUMA_CODE = """
; Ejemplo LUMA válido (S-expression)
(define-concept Emoción
  (propiedad intensidad (rango 0.0 1.0))
  (propiedad valencia (enum "positiva" "neutral" "negativa"))
  (método describir ()
    (si (> .intensidad 0.7)
      "Emoción intensa"
      "Emoción leve")))
"""

def check_structure(base_path='.'):
    """Verifica la estructura del proyecto"""
    errors = []
    warnings = []
    base_path = Path(base_path)
    
    def check_dir(expected, current):
        nonlocal errors, warnings
        for item, subtree in expected.items():
            item_path = current / item
            if not item_path.exists():
                errors.append(f"Falta: {item_path.relative_to(base_path)}")
            elif subtree is not None and not item_path.is_dir():
                errors.append(f"Se esperaba directorio: {item_path.relative_to(base_path)}")
            elif subtree is None and not item_path.is_file():
                errors.append(f"Se esperaba archivo: {item_path.relative_to(base_path)}")
            elif subtree:
                check_dir(subtree, item_path)
    
    check_dir(EXPECTED_STRUCTURE, base_path)
    
    # Verificaciones adicionales
    if not (base_path / 'luma_parser').is_dir():
        errors.append("Directorio principal 'luma_parser' no encontrado")
    
    return errors, warnings

def test_parser():
    """Prueba básica del parser"""
    try:
        sys.path.insert(0, str(Path.cwd()))
        from luma_parser.parsing.dual import DualParser
        
        parser = DualParser()
        result = parser.parse(SAMPLE_LUMA_CODE)
        
        return True, f"Parser funcionó. Resultado: {type(result)}"
    except Exception as e:
        return False, f"Error en parser: {str(e)}"

def main():
    parser = argparse.ArgumentParser(description='Verificador de estructura LUMA-lang')
    parser.add_argument('--fix', action='store_true', help='Crear estructura faltante')
    parser.add_argument('--test', action='store_true', help='Probar parser con ejemplo')
    args = parser.parse_args()
    
    print("=== Verificación de estructura LUMA-lang ===")
    errors, warnings = check_structure()
    
    if errors:
        print("\n❌ Errores encontrados:")
        for error in errors:
            print(f"- {error}")
    else:
        print("\n✅ Estructura correcta")
    
    if warnings:
        print("\n⚠️ Advertencias:")
        for warning in warnings:
            print(f"- {warning}")
    
    if args.test:
        print("\n=== Probando parser ===")
        success, message = test_parser()
        if success:
            print(f"✅ {message}")
        else:
            print(f"❌ {message}")
    
    if args.fix and errors:
        print("\n=== Creando estructura faltante ===")
        create_missing_structure()
        print("Estructura creada. Vuelve a ejecutar para verificar.")

def create_missing_structure():
    """Crea la estructura faltante"""
    base_path = Path('.')
    for item, subtree in EXPECTED_STRUCTURE.items():
        item_path = base_path / item
        if subtree is None and not item_path.exists():
            if item.endswith('.py'):
                item_path.touch()
                print(f"Creado: {item_path}")
            else:
                item_path.mkdir(exist_ok=True)
                print(f"Creado directorio: {item_path}")
        elif subtree:
            for subitem in subtree:
                subitem_path = item_path / subitem
                if not subitem_path.exists():
                    if subitem.endswith('.py'):
                        subitem_path.touch()
                        print(f"Creado: {subitem_path}")