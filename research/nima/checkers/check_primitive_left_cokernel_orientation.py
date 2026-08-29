A = (1, 1)
K = (1, -1)
ell = (1, -1)
minus_ell = tuple(-x for x in ell)


def pair(row, column):
    return sum(x * y for x, y in zip(row, column))


assert pair(ell, A) == 0
assert pair(minus_ell, A) == 0
assert pair(ell, K) == 2
assert pair(minus_ell, K) == -2
assert abs(pair(ell, K)) == abs(pair(minus_ell, K))

print("primitive left cokernel annihilates the ordinary incidence image")
print("absolute defect pairing is canonical and nonzero")
print("signed defect pairing remains an orientation torsor")
