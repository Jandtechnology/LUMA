from lark import Lark, Transformer, UnexpectedInput
from statistics import mean, median, mode, variance, stdev
import math

# ─── Memoria simbólica ─────────────────────────────────────
memoria = {}
funciones = {}

# ─── Evaluador LUMA Extendida ──────────────────────────────
class EvaluadorLUMA(Transformer):
    def asignacion(self, items):
        nombre = str(items[0])
        valor = self._resolver(items[1])
        memoria[nombre] = valor
        print(f"🧠 {nombre} = {valor}")

    def imprimir(self, items):
        print("🗣️", self._resolver(items[0]))

    def suma(self, items):
        return self._resolver(items[0]) + self._resolver(items[1])

    def resta(self, items):
        return self._resolver(items[0]) - self._resolver(items[1])

    def multiplicacion(self, items):
        return self._resolver(items[0]) * self._resolver(items[1])

    def division(self, items):
        return self._resolver(items[0]) / self._resolver(items[1])

    def potencia(self, items):
        return self._resolver(items[0]) ** self._resolver(items[1])

    def raiz(self, items):
        return math.sqrt(self._resolver(items[0]))

    def media(self, items):
        return mean([self._resolver(x) for x in items])

    def mediana(self, items):
        return median([self._resolver(x) for x in items])

    def moda(self, items):
        return mode([self._resolver(x) for x in items])

    def varianza(self, items):
        return variance([self._resolver(x) for x in items])

    def desviacion(self, items):
        return stdev([self._resolver(x) for x in items])

    def numero(self, items):
        return float(items[0])

    def variable(self, items):
        nombre = str(items[0])
        return memoria.get(nombre, f"⚠️ {nombre} no definido")

    def _resolver(self, valor):
        return valor if not hasattr(valor, 'children') else self.transform(valor)

# ─── Intérprete principal ─────────────────────────────────
def interpretar_codigo(codigo):
    with open("luma/luma.lark") as archivo_gramatica:
        parser = Lark(archivo_gramatica, start="inicio", parser="lalr")
    try:
        arbol = parser.parse(codigo)
        EvaluadorLUMA().transform(arbol)
    except UnexpectedInput as e:
        print("❌ Error de sintaxis:", e)
