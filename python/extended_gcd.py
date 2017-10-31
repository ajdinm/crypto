from polynomial import *
from copy import deepcopy
from test import test

def division(x, y):
    return divide_polynomials(x, y)
    return lambda x, y: [x/y, x%y]

def get_number_from_bitlist(bitlist):
    bitstring = ''.join(map(lambda x: str(x), bitlist))
    return int(bitstring, 2)

def get_help_arrays(a, b, q = [], r=[], s=[]):
    max_v = max(a, b)
    min_v = min(a, b)
    
    division_f = division()
    division_result = division_f(max_v, min_v)
    s_temp, r_temp = division_result[0], division_result[1]

    if r_temp == 0:
        return [q, r, s]

    if len(q) == 0:
        q = [max_v, min_v]
    else:
        q = q + [min_v]

    s = s + [s_temp]
    r = r  + [r_temp]

    a = min_v
    b = r_temp
    return get_help_arrays(a, b, q, r, s)

def pad_keys(d, keys):
    new_keys = filter(lambda x: x not in d.keys(), keys) # keys not in d
    for key in new_keys:
        d[key] = 0

    return d

def add_dicts(a, b):
    a = pad_keys(a, b.keys())
    b = pad_keys(b, a.keys())

    for key in a.keys(): #TODO map
        b[key] = b[key] + a[key]

    return b

def _join_dicts(a, b, history, initial_keys): 
    if(len(a) == 0):
        return b
    if(len(b) == 0):
        return a
    key_to_be_replaced = filter(lambda x: x not in a.keys(), b.keys())[0] # assume only one
    factor = b[key_to_be_replaced]
    for key in a.keys():
        a[key] = factor * a[key] 
    del b[key_to_be_replaced]
    return add_dicts(a, b)

def substitute_key(a, key, history):
    if(len(a) == 0):
        return a
    factor = a[key]
    desired_dict = dict(history[key])
    for temp in desired_dict.keys():
        desired_dict[temp] = factor * desired_dict[temp]
    del a[key]
    result = add_dicts(dict(a), dict(desired_dict))
    #print 'sub: ', a, key, history, result
    return result

def update_dict(a,history, initial_keys): 
    #print '--- UPDATE DICT ---', a, history
    a_original = dict(a)
    a_sub_keys = list(set(a.keys()) - set(initial_keys))
    #print '\t a_sub_keys: ', a_sub_keys
    for key in a_sub_keys:
        a = substitute_key(a, key, history)
        #print '\t\t iter_i: ', a
    return a

def extended_gcd(a, b):
    return ext_gcd_help(a, b, [], dict())

def ext_gcd_help(a, b, initial_keys = [], history = dict()):
    if a == 0 or b == 0:
        raise ValueError('Parameters has to be non-zero')
    if len(initial_keys) == 0:
        initial_keys = [a, b]

    # change these funs if want to use gcd for numbers
    
    max_f = max_polynomial
    min_f = min_polynomial
    division_f = division
    get_key_f = get_number_from_bitlist # for (real) numbers, identity function

    max_v = max_f(a, b)
    min_v = min_f(a, b)

    d = division_f(max_v, min_v)
    s, remainder = d[0], d[1]
    remainder = remainder[0] + remainder[1] # since polynomial remainder is in form  x/y
    if s == []:
        s = 0

    if sum(remainder) == 0:
        if min_v in history.keys():
            return [min_v, history[get_key_f(min_v)]]
        #print 'a, b, rem', a, b, remainder
        return [min_v, {get_key_f(max_v): 0, get_key_f(min_v): 1}] # handle case when a mod b == 0 on the first call
    r_temp = dict()
    r_temp[get_key_f(max_v)] = 1
    r_temp[get_key_f(min_v)] = s # adding and substracting binary polynomials is the same
    print 'hist, sent', history, r_temp
    r_temp = update_dict(dict(r_temp), history, initial_keys)
    #print 'hist, received', history, r_temp

    #print 'hist before', history
    history[get_key_f(remainder)] = dict(r_temp)
    #print 'hist after', history
    #print 'UPDATING: ', remainder, r_temp , ' HIST:', history
    return ext_gcd_help(min_v, remainder, initial_keys, history)

def test_gcd():
    test_cases = [  [888, 54, [6, {888:-2, 54:33}]],
                    [1312, 78, [2, {1312:11, 78:-185}]],
                    [13, 5, [1, {13:2, 5:-5}]],
                    [6, 3, [3, {6:0, 3:1}]]
                 ]

    test(test_cases, extended_gcd, 'extended_gcd')

a = [1, 0, 1, 0, 1]
b = [0, 1]
print extended_gcd(a, b)
