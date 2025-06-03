
def calc_triples(mx):


triples = []
for a in range(1, mx + 1):
for b in range(a, mx + 1):
hypotenuse = calc_hypotenuse(a, b)
if is_int(hypotenuse):
triples.append((a, b, int(hypotenuse)))
return triples


def calc_hypotenuse(a, b):


return (a*a + b*b) ** .5


def is_int(n):


return n == int(n)


triples = calc_triples(1000)

"""
$ python -m cProfile profiling/triples_v3.py
1002038 function calls in 0.269 seconds

Ordered by: standard name

ncallstottimepercallcumtimepercall filename:lineno(function)
5005000.0840.0000.0840.000 triples_v3.py:13(calc_hypotenuse)
5005000.0680.0000.0680.000 triples_v3.py:17(is_int)
10.0000.0000.2690.269 triples_v3.py:3(<module>)
10.1160.1160.2690.269 triples_v3.py:3(calc_triples)
10.0000.0000.2690.269 {built-in method builtins.exec}
10340.0000.0000.0000.000 {method 'append' of 'list' objects}
10.0000.0000.0000.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
