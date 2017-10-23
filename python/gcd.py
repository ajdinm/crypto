from polynomial import *

def division():
    return lambda x, y: [x/y, x%y]

def gcd(a, b, q = [], r=[], s=[]):
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

#    print 'q', q
#    print 'r', r
#    print 's', s
    #a = min_v
    b = r_temp
    return gcd(a, b, q, r, s)

result = gcd(888, 54)
print 'q', result[0]
print 'r', result[1]
print 's', result[2]

