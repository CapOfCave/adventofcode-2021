import itertools

numbers = [
    0b1110111,
    0b0010010,
    0b1011101,
    0b1011011,
    0b0111010,
    0b1101011,
    0b1101111,
    0b1010010,
    0b1111111,
    0b1111011
]

def translate_code(code, permutation):
    val = 0
    for i in range(7):
        if permutation[i] in code:
            val += 2 ** (6 - i)
    return val

def number_exists(code, permutation):
    return translate_code(code, permutation) in numbers

def get_digit(code, permutation):
    return numbers.index(translate_code(code, permutation))

def get_number(codes, permutation):
    return sum([10 ** (3 - index) * get_digit(code, permutation) for index, code in enumerate(codes)])

def is_valid_permutation(permutation, codes):
    return all(number_exists(code, permutation) for code in codes)

with open('input.txt') as input:
    entrysum = 0
    for entry in input.readlines():
        signalpatterns, output = [e.split() for e in entry.split(" | ")]
        ret = []
        for permutation in itertools.permutations(['a', 'b', 'c', 'd', 'e', 'f', 'g']):
            if is_valid_permutation(permutation, signalpatterns):
                entrysum += get_number(output, permutation)
    print(entrysum) # 1009098