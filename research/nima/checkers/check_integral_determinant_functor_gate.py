from itertools import permutations


def parity(p):
    inversions = sum(
        p[i] > p[j]
        for i in range(len(p))
        for j in range(i + 1, len(p))
    )
    return -1 if inversions % 2 else 1


identity = (0, 1)
swap = (1, 0)

assert parity(identity) == 1
assert parity(swap) == -1

# An unordered two-label source admits both presentations.
presentation_signs = {parity(p) for p in permutations(range(2))}
assert presentation_signs == {-1, 1}

# A scalar Gram readout cannot detect the orientation reversal.
gram_identity = ((1, 0), (0, 1))
gram_after_swap = ((1, 0), (0, 1))
assert gram_identity == gram_after_swap

print("unordered rank-two source: orientation is not canonical")
print("swap determinant: -1 while scalar Gram data are unchanged")
print("required repair: typed determinant functor with coherent comparison signs")
