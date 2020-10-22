"""
Base32H Encoder/Decoder for Python

https://base32h.github.io/

"""

base32h_code = {0: ['0', 'O', 'o'],
                1: ['1', 'I', 'i'],
                2: ['2', ''],
                3: ['3', ''],
                4: ['4', ''],
                5: ['5', 'S', 's'],
                6: ['6', ''],
                7: ['7', ''],
                8: ['8', ''],
                9: ['9', ''],
                10: ['A', 'a'],
                11: ['B', 'b'],
                12: ['C', 'c'],
                13: ['D', 'd'],
                14: ['E', 'e'],
                15: ['F', 'f'],
                16: ['G', 'g'],
                17: ['H', 'h'],
                18: ['J', 'j'],
                19: ['K', 'k'],
                20: ['L', 'l'],
                21: ['M', 'm'],
                22: ['N', 'n'],
                23: ['P', 'p'],
                24: ['Q', 'q'],
                25: ['R', 'r'],
                26: ['T', 't'],
                27: ['V', 'v', 'U', 'u'],
                28: ['W', 'w'],
                29: ['X', 'x'],
                30: ['Y', 'y'],
                31: ['Z', 'z'], }

base32_decode = {}
for k, v in base32h_code.items():
    for c in v:
        base32_decode[c] = k


def encode_digit(n):
    if type(n) == int and n >= 0 and n < 32:
        return base32h_code[n][0]
    raise Exception("Invalid coding digit:" + str(n))


def encode_number(n):
    if type(n) == int and n >= 0:
        code = encode_digit(n % 32)
        if n == 0:
            return code
        quotient = int(n/32)
        if quotient > 0:
            return encode_number(quotient) + code
        # last digit - return it.
        return code
    raise Exception("Invalid encoding number:" + str(n))


def decode_base32h(code):
    cum = 0
    for n in str(code):
        cum *= 32
        cum += base32_decode[n]
    return cum
