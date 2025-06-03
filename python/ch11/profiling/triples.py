
def calc_triples(mx):


triples = []
for a in range(1, mx + 1):
for b in range(a, mx + 1):
hypotenuse = calc_hypotenuse(a, b)
if is_int(hypotenuse):
triples.append((a, b, int(hypotenuse)))
return triples


def calc_hypotenuse(a, b):


return (a**2 + b**2) ** .5


def is_int(n):  # n is expected to be a float


return n.is_integer()


triples = calc_triples(1000)

"""
$ python -m cProfile profiling/triples.py
1502538 function calls in 0.489 seconds

Ordered by: standard name

ncallstottimepercallcumtimepercall filename:lineno(function)
5005000.2820.0000.2820.000 triples.py:13(calc_hypotenuse)
5005000.0650.0000.0860.000 triples.py:17(is_int)
10.0000.0000.4890.489 triples.py:3(<module>)
10.1210.1210.4890.489 triples.py:3(calc_triples)
10.0000.0000.4890.489 {built-in method builtins.exec}
10340.0000.0000.0000.000 {method 'append' of 'list' objects}
10.0000.0000.0000.000 {method 'disable' of '_lsprof.Profiler' objects}
5005000.0210.0000.0210.000 {method 'is_integer' of 'float' objects}
"""
