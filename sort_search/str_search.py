


def kmp_search(txt: str, substr: str) -> int:
    """
        Search string using KMP algorithm
        str: txt
        str: substr
        return：position that substr first found, otherwise -1
    """
    n = len(substr)
    shift_table = [0] * n           # partial match table / shift table

    for i in range(2, n):
        shift = shift_table[i - 1]
        while shift > 0 and substr[i - 1] != substr[shift]:
            shift = shift_table[shift]
        if substr[i - 1] == substr[shift]:
            shift_table[i] = shift + 1

    m = len(txt)
    j = 0
    for i in range(m):
        while j > 0 and txt[i] != substr[j]:
            j = shift_table[j]

        if txt[i] == substr[j]:
            j += 1
            if j == n:
                return i - j + 1
        
    return -1


r = kmp_search('', '')
print(r)

r = kmp_search('a', '')
print(r)

r = kmp_search('abc', 'bc')
print(r)

r = kmp_search('abcadbabcabba', 'abcab')
print(r)

r = kmp_search('abcadbabcabba', 'abcab')
print(r)


