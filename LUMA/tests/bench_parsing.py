# tests/bench_parsing.py
import timeit
from core.parsing import dual

parser = dual.DualParser()
time = timeit.timeit(
    lambda: parser.parse("(define x 42)"),
    number=10_000
)
print(f"10,000 parses in {time:.2f}s")