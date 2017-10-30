from test import test

def add_binary(a, b):
    return (a + b) % 2

def add_polynomials_binary(a, b):
    if len(a) == 0:
        return b
    if len(b) == 0:
        return a
    max_len = max(len(a), len(b))
    a = fill_bits(a, max_len)
    b = fill_bits(b, max_len)
    return map(lambda x, y: add_binary(x, y), a, b)

def max_polynomial(a, b):
    if len(a) == 0 and len(b) == 0:
        return a
    if len(b) == 0:
        return a
    if len(a) == 0:
        return b

    a_deg = sorted(get_polynomial_degree(a), reverse=True)
    b_deg = sorted(get_polynomial_degree(b), reverse=True) # desc

    smaller_array = a_deg
    greater_array = b_deg
    original_small = a
    original_great = b

    if len(b_deg) < len(smaller_array):
        smaller_array = b_deg
        greater_array = a_deg
        original_small = b
        original_great = a

    for i in range(len(smaller_array)):
        if smaller_array[i] > greater_array[i]:
            return original_small
        if smaller_array[i] < greater_array[i]:
            return original_great
    return original_great

def min_polynomial(a, b):

    mmax = max_polynomial(a, b)
    if mmax == a:
        return b
    return a

    
def fill_bits(x, n):
    to_add = n - len(x)
    if to_add <= 0:
        return x
    return x + ([0] * to_add)


def get_polynomial_degree(polynomial):
    polynomial = filter(lambda x: x[1] != 0, enumerate(polynomial))
    polynomial = map(lambda x: x[0], polynomial) # get index of non zero elements in poly

    return polynomial

def multiply_degree_polynomial(degree, polynomial):
    
    max_len = degree + len(polynomial) 
    polynomial = get_polynomial_degree(polynomial)
    one_inds = map(lambda x: x + degree, polynomial) # get inds of ones in result
    
    result = map(lambda i: 1 if i in one_inds else 0, range(max_len))
    return result

def multiply_polynomials(a, b):
    
    max_len = len(a) + len(b) - 1
    degrees = filter(lambda x: x[1] != 0, enumerate(a))
    degrees = map(lambda x: x[0], degrees) 
    expanded = map(lambda x: fill_bits(multiply_degree_polynomial(x, b), max_len), degrees)

    result = reduce(lambda x, y: add_polynomials_binary(x, y), expanded)

    return result

def get_polynomial_from_degree(degree):
    return map(lambda i: 1 if i == degree else 0, range(degree + 1))

def divide_polynomials(a, b): # returns (c, d) touple where c = a/b, and d is reminder in form (numerator, denominator)
    
    a_deg = get_polynomial_degree(a)
    b_deg = get_polynomial_degree(b)
    if b_deg[-1] > a_deg[-1]:
        return ([], (a, b))
    temp = a_deg[-1] - b_deg[-1]
    to_sub = multiply_degree_polynomial(temp, b)
    c = add_polynomials_binary(a, fill_bits(to_sub, len(a)))
    new_result = divide_polynomials(c, b)
    return (add_polynomials_binary(get_polynomial_from_degree(temp), new_result[0]), new_result[1])


def test_multiply_polynomials():
    test_cases = [[[1, 1, 1], [1, 0, 1], [1, 1, 0, 1, 1]],
                  [[1, 0, 1], [1, 1, 1], [1, 1, 0, 1, 1]],
                  [[1, 0, 0], [1, 1, 0], [1, 1, 0, 0, 0]],
                  [[1, 0, 1], [1, 0, 1], [1, 0, 0, 0, 1]]
                  ]
    test(test_cases, multiply_polynomials, 'multiply_polynomials')

def test_max_polynomial():
    test_cases = [[[1, 1, 1], [1, 0, 1], [1, 1, 1]],
                  [[1, 0, 1], [1, 1, 1], [1, 1, 1]],
                  [[1, 0, 0], [1, 0, 0], [1, 0, 0]],
                  [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                  ]
    test(test_cases, max_polynomial, 'max_polynomial')

def test_min_polynomial():
    test_cases = [[[1, 1, 1], [1, 0, 1], [1, 0, 1]],
                  [[1, 0, 1], [1, 1, 1], [1, 0, 1]],
                  [[1, 0, 0], [1, 0, 0], [1, 0, 0]],
                  [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                  ]
    test(test_cases, min_polynomial, 'min_polynomial')

test_multiply_polynomials()
test_max_polynomial()
test_min_polynomial()
