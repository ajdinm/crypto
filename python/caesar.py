import numpy

def total_variation_distance(X, Y):
    if len(X) != len(Y):
        raise ValueError('lenghts missmatch')
    difference = map(lambda i: abs(X[i] - Y[i]), range(len(X)))
    return 0.5 * sum(difference)

def get_letter(number):
    return chr(ord('A') + number)

def count_letter_occurance(text, letter):
    return sum([x == letter for x in text])

def get_letter_probs(text):
    removal = [' ', ',', '.', ':', '’', '-', ';']
    text = ''.join([x if x not in removal else '' for x in text])

    text = text.upper()
    letter_counts = map(lambda i: count_letter_occurance(text, get_letter(i)), range(26)) # assume english
    letter_probs = map(lambda p: float(p) / len(text), letter_counts)

    return letter_probs

def shift_letter(letter, shift):
    offset = ord('Z') - ord('A') + 1 
    if ord(letter) + shift <= ord('Z'):
        offset = 0
    return chr(ord(letter) + shift - offset)

def test_shift_letter():
    letters = map(lambda i: chr(ord('A') + i), range(26))
    n = 13
    rolled = list(numpy.roll(letters, n))
    shifted = map(lambda x: shift_letter(x, n), letters)
    print rolled
    print shifted
def shift_text(text, shift):
    removal = [' ', ',', '.', ':', '’', '-', ';']
    return ''.join(map(lambda x: x if x in removal else shift_letter(x, shift), text))

english_letter_freq = [8.2, 1.5, 2.8, 4.2, 12.7, 2.2,
                       2.0, 6.1, 7.0, 0.1, 0.8, 4.0,
                       2.4, 6.7, 7.5, 1.9, 0.1, 6.0,
                       6.3, 9.0, 2.8, 1.0, 2.4, 0.1,
                       2.0, 0.1]

test_text = 'GB OR, BE ABG GB OR: GUNG VF GUR DHRFGVBA: \
JURGURE ’GVF ABOYRE VA GUR ZVAQ GB FHSSRE\
GUR FYVATF NAQ NEEBJF BS BHGENTRBHF SBEGHAR, \
BE GB GNXR NEZF NTNVAFG N FRN BS GEBHOYRF, \
NAQ OL BCCBFVAT RAQ GURZ? GB QVR: GB FYRRC; \
AB ZBER; NAQ OL N FYRRC GB FNL JR RAQ \
GUR URNEG-NPUR NAQ GUR GUBHFNAQ ANGHENY FUBPXF \
GUNG SYRFU VF URVE GB, ’GVF N PBAFHZZNGVBA \
QRIBHGYL GB OR JVFU’Q. GB QVR, GB FYRRC; \
GB FYRRC: CREPUNAPR GB QERNZ: NL, GURER’F GUR EHO; \
SBE VA GUNG FYRRC BS QRNGU JUNG QERNZF ZNL PBZR \
JURA JR UNIR FUHSSYRQ BSS GUVF ZBEGNY PBVY,\
ZHFG TVIR HF CNHFR: GURER’F GUR ERFCRPG \
GUNG ZNXRF PNYNZVGL BS FB YBAT YVSR;'

english_prob = map(lambda x: x/100, english_letter_freq)
text_prob = get_letter_probs(test_text)
shift_dist = map(lambda i:total_variation_distance(english_prob, list(numpy.roll(text_prob, i))), range(26))
rotate = shift_dist.index(min(shift_dist))

print shift_text(test_text, rotate)
test_shift_letter()



