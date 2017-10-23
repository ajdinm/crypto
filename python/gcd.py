from polynomial import *

def division():
    return lambda x, y: [x/y, x%y]

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

    for key in a.keys():
        b[key] = b[key] + a[key]

    return b

def join_dicts(a, b): # a is such that there exists key K in b such K = eval(a)
    key_to_be_replaced = filter(lambda x: x not in a.keys(), b.keys())[0] # assume only one
    factor = b[key_to_be_replaced]
    for key in a.keys():
        a[key] = factor * a[key] 
    print a
    del b[key_to_be_replaced]
    return add_dicts(a, b)

def gcd(a, b, r = []):
    max_v = max(a, b)
    min_v = min(a, b)
    
    division_f = division()
    d = division_f(max_v, min_v)
    s, r = d[0], d[1]

    r_temp = dict()
    r_temp[max_v] = 1
    r_temp[min_v] = -1 * s
    
    r = add_dicts(r_temp, r)

#result = gcd(888, 54)
#print 'q', result[0]
#print 'r', result[1]
#print 's', result[2]

a = {888:1, 54:-16}
b = {54:1, 24:-2}
print join_dicts(a, b)
