import itertools

def permutations(string):
    #your code here
    chrs = list(string)
    permutations = set()

    def permute(chrs, n, prefix, level, permutations):
        if n == 1:
            prefix[level] = chrs[0]
            permutations.add(''.join(prefix))

        for i in range(n):
            chrs[0], chrs[i] = chrs[i], chrs[0]
            prefix[level] = chrs[0]
            permute(chrs[1:], n - 1, prefix, level + 1, permutations)

    n = len(chrs)
    if n <= 1:
        return string

    perfix = [' '] * n
    permute(chrs, n, perfix, 0, permutations)

    return list(permutations)


def permutations_native(string):
    return list("".join(p) for p in set(itertools.permutations(string)))


r = permutations('aabb')

print(r)
pass
