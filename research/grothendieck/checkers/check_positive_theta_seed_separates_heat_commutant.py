from fractions import Fraction


def rank(rows):
    a = [list(map(Fraction, row)) for row in rows]
    r = 0
    for c in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        p = a[r][c]
        a[r] = [x / p for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [x - q * y for x, y in zip(a[i], a[r])]
        r += 1
    return r


passed = 0
total = 0


def gate(value):
    global passed, total
    total += 1
    passed += bool(value)


# A degree-d polynomial multiplier agreeing with one at d+1 source points is
# identically one. Positivity means none of these constraints is erased by a
# zero of the seed.
for degree in range(13):
    points = [Fraction(k + 1) for k in range(degree + 1)]
    vandermonde = [[u ** j for j in range(degree + 1)] for u in points]
    gate(rank(vandermonde) == degree + 1)

# The hostile positive Fourier-side weights differ from one on every u>0.
for n in range(2, 14, 2):
    for u in [Fraction(1, 2), Fraction(1), Fraction(2)]:
        multiplier = 1 + u ** (2 * n)
        gate(multiplier != 1)
        gate(multiplier > 0)

print(f"SUMMARY: {passed}/{total} gates passed")
if passed != total:
    raise SystemExit(1)
