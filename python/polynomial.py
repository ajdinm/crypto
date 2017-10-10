from test import test

def add_binary(a, b):
    return (a + b) % 2

def add_polynomials_binary(a, b):
    return map(lambda x, y: add_binary(x, y), a, b)


def fill_bits(x, n):
    to_add = n - len(x)
    if to_add <= 0:
        return x
    return x + ([0] * to_add)

def multiply_factor_polynomial(factor, polynomial):
    
    max_len = factor + len(polynomial) 
    polynomial = filter(lambda x: x[1] != 0, enumerate(polynomial))
    polynomial = map(lambda x: x[0], polynomial) # get index of non zero elements in poly
    one_inds = map(lambda x: x + factor, polynomial) # get inds of ones in result
    
    result = map(lambda i: 1 if i in one_inds else 0, range(max_len))

    return result

def multiply_polynomials(a, b):
    
    max_len = len(a) + len(b) - 1
    factors = filter(lambda x: x[1] != 0, enumerate(a))
    factors = map(lambda x: x[0], factors) 
    expanded = map(lambda x: fill_bits(multiply_factor_polynomial(x, b), max_len), factors)

    result = reduce(lambda x, y: add_polynomials_binary(x, y), expanded)

    return result

def test_multiply_polynomials():
    test_cases = [[[1, 1, 1], [1, 0, 1], [1, 1, 0, 1, 1]],
                  [[1, 0, 1], [1, 1, 1], [1, 1, 0, 1, 1]],
                  [[1, 0, 0], [1, 1, 0], [1, 1, 0, 0, 0]],
                  [[1, 0, 1], [1, 0, 1], [1, 0, 0, 0, 1]]
                  ]
    test(test_cases, multiply_polynomials, 'multiply_polynomials')

test_multiply_polynomials()
