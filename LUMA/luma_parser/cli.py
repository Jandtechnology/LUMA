import argparse
from pathlib import Path
from .parsing.dual import DualParser

def main():
    parser = argparse.ArgumentParser(description='Parser LUMA')
    parser.add_argument('file', help='Archivo .luma a parsear')
    parser.add_argument('--ast', action='store_true', help='Mostrar AST')
    args = parser.parse_args()

    try:
        luma_parser = DualParser()
        ast = luma_parser.parse_file(args.file)
        
        if args.ast:
            print("AST generado correctamente:")
            print(ast)
        else:
            print(f"Archivo {args.file} parseado con éxito!")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()