import pydes
from des import *
from bitarray import bitarray

def print_array(array):
    for x in array:
        print x

key = "secret_k"
text= "Hello wo"
d = pydes.des()
cipher = d.encrypt(key,text)
plain = d.decrypt(key,cipher)

correct_keys = d.get_round_keys()

ba = bitarray()
ba.fromstring(key)
key = ba.to01()
test_keys = get_round_keys(key)
ba = bitarray()
ba.fromstring(text)
msg = ba.to01()
my_des_cipher = des_seq(msg,key)

print 'key: ' + key
print 'msg: ' + msg
print 'result: \t' + my_des_cipher
print 'expected: \t' + '1010100101011010101001100001000110111000011110001101101111101101'

