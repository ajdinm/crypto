from test import test

def add_letters(p, q):
    p = p.upper()
    q = q.upper()
    offset = ord('A')
    new_letter = ((ord(p) + ord(q)) % 26) + offset
    return chr(new_letter)

def substract_letters(p, q):
    p = p.upper()
    q = q.upper()
    new_letter = ord(p) - ord(q)
    start = ord('A')
    if new_letter < 0:
        start = ord('Z') + 1
    new_letter = start + new_letter
    return chr(new_letter)

def _test(test_cases, f):
    for test_case in test_cases:
        print 'OK' if test_case[-1] == f(test_case[0], test_case[1]) else 'NOK'

def test_add_letters():
    test_cases = [('T', 'S', 'L'),
                  ('T', 'E', 'X'),
                  ('T', 'E', 'H'), # expected to fail
                  ('S', 'A', 'S')]
    test(test_cases, add_letters, 'add_letters')

def test_substract_letters():
    test_cases = [('L', 'S', 'T'),
                  ('X', 'E', 'T'),
                  ('S', 'A', 'S')]
    test(test_cases, substract_letters, 'substract_letters')

def add_padding(msg, key):
    remainder = len(msg) % len(key)
    if remainder != 0:
        msg = msg + ''.join(map(lambda _: '0', range(len(key) - remainder)))
    key = ''.join(map(lambda _: key, range(len(msg) / len(key))))
    return msg, key

def encrypt(msg, key):
    msg, key = add_padding(msg, key)
    cipher_text = ''.join(map(lambda i: add_letters(msg[i], key[i]), range(len(msg))))
    return cipher_text

def decrypt(cipher_text, key):
    cipher_text, key = add_padding(cipher_text, key)
    msg = ''.join(map(lambda i: substract_letters(cipher_text[i], key[i]), range(len(cipher_text))))
    return msg


def test_encrypt():
    test_cases = [['THISISATESTMESSAGE', 'SESAME', 'LLASUWSXWSFQWWKASI']]
    test(test_cases, encrypt, 'encrypt')

def test_decrypt():
    test_cases = [['LLASUWSXWSFQWWKASI','SESAME', 'THISISATESTMESSAGE']]
    test(test_cases, decrypt, 'decrypt')



key = 'SESAME'
msg = 'THISISATESTMESSAG'

test_add_letters()
test_encrypt()
test_substract_letters()
test_decrypt()

