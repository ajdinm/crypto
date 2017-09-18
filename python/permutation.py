from functools import partial
from test import test

def permutation(perm_array, msg):
    if len(perm_array) != len(msg):
        raise ValueError('lengths missmatch')

    cipher = map(lambda i: msg[perm_array.index(i)], range(len(msg)))
    return ''.join(cipher)

def encrypt(msg, key):
    msg = msg.lower()
    sigma = partial(permutation, key)
    remainder = len(msg) % len(key)
    if remainder != 0:
        to_add = len(key) - remainder
        msg = msg + ''.join(['0'for x in range(to_add)])
    n = len(key)
    blocks = [msg[i:i+n] for i in range(0, len(msg), n)]
    cipher = map(lambda block: ''.join(sigma(block)), blocks)
    return ''.join(cipher)

def decrypt(cipher, key):
    key = map(lambda i: key.index(i), range(len(key)))
    return encrypt(cipher, key)

def test_encrypt():
    test_cases = [ ('onceuponatimetherewasalittlegirlcalledsnowwhiteahb', [1, 3, 0, 2, 4], 
                    'coenunpaoteitmheewralsiatetglicralldlsenwohwiatheb'),
                    ('abcdefghijklmnopqrstuvwxy', [1, 3, 0, 2, 4], 'cadbehfigjmknlorpsqtwuxvy')]
    test(test_cases, encrypt, 'encrypt')

def test_decrypt():
    test_cases = [ ('onceuponatimetherewasalittlegirlcalledsnowwhiteahb', [1, 3, 0, 2, 4], 
                    'coenunpaoteitmheewralsiatetglicralldlsenwohwiatheb'),
                    ('abcdefghijklmnopqrstuvwxy', [1, 3, 0, 2, 4], 'cadbehfigjmknlorpsqtwuxvy')]
    test_cases = map(lambda test_case: (test_case[2], test_case[1], test_case[0]), test_cases)
    test(test_cases, decrypt, 'decrypt')

def test_permutation():
    test_cases = [([1, 3, 0, 2, 4], 'onceu', 'coenu')]
    test(test_cases, permutation, 'permutation')


test_permutation()
test_encrypt()
test_decrypt()
