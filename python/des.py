import numpy as np
from constants import *
from test import test
from functools import partial

initial_permutation_array = map(lambda x: x-1, get_initital_permutation_array())


def permutation(key, msg):
    if len(key) != len(msg):
        print len(key)
        print len(msg)
        raise ValueError()

    result = ''.join(map(lambda i: msg[key[i]], range(len(msg))))
    return result

def test_permutation():
    test_cases = [ ([1, 0], 'ab', 'ba')]
    test(test_cases, permutation, 'permutation')

def expand_right(r):
    to_add = 48 - len(r)
    return '0' * to_add + r

def fill_bits(target, msg):
    to_add = target - len(msg)
    if to_add < 0:
        raise ValueError()
    return '0' * to_add + msg

def get_round_keys(key, r = 16):
    r = r+1
    C, D = range(r), range(r)
    C[0] = permutation(get_pc_1_permutation(), key)
    C[0], D[0] = C[0][:28], C[0][28:]
    round_keys = [None] * r
    for i in range(1, r):
        p_i = 2
        if i in [1, 2, 9, 16]:
            p_i = 1
        C[i] = left_cyclic_shift(C[i-1], p_i)
        D[i] = left_cyclic_shift(D[i-1], p_i)
        round_keys[i] = C[i] + D[i]
        round_keys[i] = permutation(get_pc_2_permutation(), round_keys[i])

    return rounds[1:]

def s_box(key, msg):
    row = int(msg[0], msg[5], 2)
    col = int(msg[1:5], 2)
    return fill_bits(4, key[row][col])

def left_cyclic_shift(x, n):
    return map(lambda i: x[(i+n)%len(x)], x)

def des_seq(msg, key): 
    if len(msg) != 64:
        raise ValueError('only working with 64bit plaintext')
    msg = permutation(initial_permutation_array, msg)
    expansion_array = map(lambda x: x-1, get_expansion_permutation_array())
    l, r = msg[:32], msg[32:]
    rounds = 16
    L, R = range(rounds), range(rounds)
    L[0], R[0] = l, r
    round_keys = get_round_keys(key, rounds)
    s_boxes = get_s_box_keys()
    s_boxes = map(lambda box: partial(s_box, box), s_boxes)
    for i in range(1, rounds):
        R[i] = expand_right(R[i])
        R[i] = permutation(expansion_array, R[i])
        R[i] = np.bitwise_xor(int(R[i], 2), int(round_keys[i-1], 2))
        number_of_bits_in_lot = 6
        split = [R[i][j*number_of_bits_in_lot:j*number_of_bits_in_lot+number_of_bits_in_lot]
                    for j in ranke(len(R[i])/float(number_of_bits_in_lot))]

        split = map(lambda msg_part, box: box(msg_part), split, s_boxes)
        split = ''.join(split)

test_permutation()
des_seq('1' * 64, 1)
