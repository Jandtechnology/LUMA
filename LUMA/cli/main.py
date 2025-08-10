"""
import sys
from luma.luma_core import interpretar_codigo

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python main.py archivo.luma")
    else:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            codigo = f.read()
            interpretar_codigo(codigo)

"""

import sys
from luma.luma_core import interpretar_codigo

if __name__ == "__main__":
    archivo = "demo.luma"  # Cambia aquí el nombre de tu archivo
    with open(archivo, "r", encoding="utf-8") as f:
        codigo = f.read()
        interpretar_codigo(codigo)
