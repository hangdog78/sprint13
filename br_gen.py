BR_PAIRS = {
    '{':'}',
    '(':')',
    '[':']'
            }


def is_its_closing(op, cl):
    return BR_PAIRS[op] == cl


def is_correct_bracket_seq(seq):
    last_opened_br = []
    for element in seq:
        if element not in ('[', ']', '(', ')', '{', '}'):
            return False
        if element in BR_PAIRS.keys():
            last_opened_br.append(element)
        else:
            if len(last_opened_br) == 0 or not is_its_closing(last_opened_br[-1], element):
                return False
            last_opened_br.pop(-1)
    return len(last_opened_br) == 0

def gen_binary(n, prefix, result):
    if n == 0:
        str_res = ''
        for char in prefix:
            if char == '0':
                str_res += '('
            elif char == '1':
                str_res += ')'
        if is_correct_bracket_seq(str_res):
            result.append(str_res)
    else:
        gen_binary(n - 1, prefix + '0', result)
        gen_binary(n - 1, prefix + '1', result)


if __name__ == '__main__':
    length = int(input())
    result = []
    gen_binary(length*2, '', result)
    print(*result, sep='\n')





