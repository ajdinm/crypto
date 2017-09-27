import random
from test import test
from des import *
from constants import *
from termcolor import colored

def get_random_bitstring(n):
    return ''.join(map(lambda _: '1' if random.random() >= 0.5 else '0', range(n)))

def test_permutation():
    test_cases = [([1, 0], 'ab', 'ba'),
                   ([0, 1], 'ab', 'ab'),
                   ([2, 0, 1], '103', '310'),
                   ([1, 0], '103', '01')]
    test(test_cases, permutation, 'permutation')

def test_expand():
    test_cases = [('1', '0'*47 + '1'),
                  ('1'*48, '1'*48),
                  ('0' * 48, '0' * 48)]
    test(test_cases, expand, 'expand')

def test_left_cyclic_shift():
    test_cases = [('101', 1, '011'),
                  ('000', 2, '000'),
                  ('1100', 2, '0011'),
                  ('1100', 4, '1100'),
                  ('1100', 5, '1001')]
    test(test_cases, left_cyclic_shift, 'left_cyclic_shift')

def test_get_round_keys():
    key = '1011011011000100000110000111011100111001101111101101100000011111'
    after_permutation = permutation(get_pc_1_permutation_array(), key)
    c1, d1 = left_cyclic_shift(after_permutation[:28], 1), left_cyclic_shift(after_permutation[28:], 1)
    first_key = permutation(get_pc_2_permutation(), c1 + d1)
    c2, d2 = left_cyclic_shift(c1, 1), left_cyclic_shift(d1, 1)
    second_key = permutation(get_pc_2_permutation(), c2 + d2)
    c2, d2 = left_cyclic_shift(c2, 2), left_cyclic_shift(d2, 2)
    third_key = permutation(get_pc_2_permutation(), c2+d2)
    keys = get_round_keys(key)

    color = 'red' 
    to_print = 'NOK: expected: ' + str(first_key) + ' got: ' + str(keys[0])
    if first_key == keys[0]:
        color = 'green'
        to_print = 'OK'
    print colored(to_print, color) 
    color = 'red' 
    to_print = 'NOK: expected: ' + str(second_key) + ' got: ' + str(keys[1])
    if second_key == keys[1]:
        color = 'green'
        to_print = 'OK'
    print colored(to_print, color) 
    color = 'red' 
    to_print = 'NOK: expected: ' + str(third_key) + ' got: ' + str(keys[2])
    if third_key == keys[2]:
        color = 'green'
        to_print = 'OK'
    print colored(to_print, color) 



test_permutation()
test_expand()
test_left_cyclic_shift()
test_get_round_keys()
