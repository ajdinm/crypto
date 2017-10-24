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
    print 'SUB KEY: ', a, key, history
    if(len(a) == 0):
        return a
    factor = a[key]
    desired_dict = history[key]
    for temp in desired_dict.keys():
        desired_dict[temp] = factor * desired_dict[temp]
    del a[key]
    #print 'dzeko', a, desired_dict
    result = add_dicts(a, desired_dict)
    #print 'dzekson', result
    return result

def join_dicts(a, b, history, initial_keys): 
    a_sub_keys = list(set(a.keys()) - set(initial_keys))
    b_sub_keys = list(set(b.keys()) - set(initial_keys))
    print 'no', a, b

    for key in a_sub_keys:
        a = substitute_key(a, key, history)
    for key in b_sub_keys:
        b = substitute_key(b, key, history)

    print 'idk', a, b

    return add_dicts(a, b)

def gcd(a, b, initial_keys = [], r = dict(), history = dict()):
    if len(initial_keys) == 0:
        initial_keys = [a, b]
    max_v = max(a, b)
    min_v = min(a, b)
    
    division_f = division()
    d = division_f(max_v, min_v)
    s, remainder = d[0], d[1]
    if remainder == 0:
        return [min_v, r]

    r_temp = dict()
    r_temp[max_v] = 1
    r_temp[min_v] = -1 * s
    
    r = join_dicts(r, r_temp, history, initial_keys)
    history[remainder] = r
    print max_v, min_v, s, remainder, r
    return gcd(min_v, remainder, initial_keys, r, history)

result = gcd(888, 54)
print 'result', result
result = gcd(1312, 78)
print 'result', result
#print 'q', result[0]
#print 'r', result[1]
#print 's', result[2]

#a = {888:1, 54:-16}
#b = {54:1, 24:-2}
#print join_dicts(a, b)
