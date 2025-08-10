import sys
import os

# Añadir la ruta raíz al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.db.luma_db import guardar_programa, obtener_todos_programas

programa_de_prueba = {
    "type": "Program",
    "location": {"file": "demo.luma", "line": 1, "column": 0},
    "statements": [
        {
            "type": "ListExpr",
            "location": {"line": 1, "column": 0},
            "elements": [
                {"type": "Symbol", "name": "print"},
                {"type": "Literal", "value": "Hola desde LUMA"}
            ]
        }
    ]
}

if __name__ == "__main__":
    guardar_programa(programa_de_prueba)
    print("📦 Programas en DB:")
    for prog in obtener_todos_programas():
        print(prog)
