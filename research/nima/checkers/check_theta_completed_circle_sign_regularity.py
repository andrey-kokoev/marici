"""High-precision finite scan of completed-circle spectral minors."""

from decimal import Decimal as D
from decimal import getcontext
from itertools import combinations

getcontext().prec = 80
PI = D("3.141592653589793238462643383279502884197169399375105820974944")


def b(t, x):
    return t ** (D(5) / D(4)) * x * (2 * PI * t * x - 3) * (-PI * t * x).exp()


def det(a):
    if len(a) == 1:
        return a[0][0]
    return sum(
        ((-1) ** j)
        * a[0][j]
        * det([row[:j] + row[j + 1 :] for row in a[1:]])
        for j in range(len(a))
    )


ts = list(map(D, ["1", "1.02", "1.05", "1.1", "1.25", "1.5"]))
xs = list(map(D, ["1", "4", "9", "16", "25", "36"]))
counts = {}
smallest = {}

for k in range(2, 7):
    expected = (-1) ** (k * (k - 1) // 2)
    counts[k] = 0
    for tt in combinations(ts, k):
        for xx in combinations(xs, k):
            value = det([[b(t, x) for x in xx] for t in tt])
            sign = (value > 0) - (value < 0)
            assert sign == expected, (k, tt, xx, value, expected)
            magnitude = abs(value)
            smallest[k] = min(smallest.get(k, magnitude), magnitude)
            counts[k] += 1

full = det([[b(t, x) for x in xs] for t in ts])
assert full < 0

print("tested minors by order:", counts)
print("smallest absolute determinant by order:", smallest)
print("full order-six determinant:", full)
print("PASS: expected reverse-sign-regular pattern on the declared grid")
