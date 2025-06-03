# lambda.explained.py
"""
myfunc = lambda [parameter_list]: expression

def myfunc([parameter_list]):
    return expression
"""

# example 1: adder


def adder(a, b):
    return a + b


# is equivalent to:
def adder_lambda(a, b): return a + b

# example 2: to uppercase


def to_upper(s):
    return s.upper()


# is equivalent to:
def to_upper_lambda(s): return s.upper()


if __name__ == "__main__":

    print(adder(3, 4))
    print(adder_lambda(3, 4))

    print(to_upper("Hello"))
    print(to_upper_lambda("Hello"))
