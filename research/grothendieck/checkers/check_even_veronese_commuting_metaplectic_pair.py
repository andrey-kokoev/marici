from fractions import Fraction


def apply(name, state):
    a, b, coefficient = state
    if name == "Eu":
        return a + 2, b, coefficient / 2
    if name == "Fu":
        return a - 2, b, -coefficient * a * (a - 1) / 2 if a >= 2 else 0
    if name == "Hu":
        return a, b, coefficient * (Fraction(a) + Fraction(1, 2))
    if name == "Ev":
        return a, b + 2, coefficient / 2
    if name == "Fv":
        return a, b - 2, -coefficient * b * (b - 1) / 2 if b >= 2 else 0
    if name == "Hv":
        return a, b, coefficient * (Fraction(b) + Fraction(1, 2))
    raise ValueError(name)


def compose(left, right, a, b):
    x, y, c = apply(right, (a, b, Fraction(1)))
    if c == 0:
        return x, y, Fraction(0)
    x, y, d = apply(left, (x, y, c))
    return x, y, d


def comm(left, right, a, b):
    x1, y1, c1 = compose(left, right, a, b)
    x2, y2, c2 = compose(right, left, a, b)
    assert (x1, y1) == (x2, y2) or c1 == 0 or c2 == 0
    return c1 - c2


passed = 0
total = 0


def gate(value):
    global passed, total
    total += 1
    passed += bool(value)


u_names = ["Eu", "Fu", "Hu"]
v_names = ["Ev", "Fv", "Hv"]

for a in range(13):
    for b in range(13):
        if (a + b) % 2:
            continue
        gate(comm("Hu", "Eu", a, b) == 1)  # 2 Eu has coefficient 1
        expected_fu = a * (a - 1) if a >= 2 else 0
        gate(comm("Hu", "Fu", a, b) == expected_fu)
        gate(comm("Eu", "Fu", a, b) == Fraction(a) + Fraction(1, 2))
        gate(comm("Hv", "Ev", a, b) == 1)
        expected_fv = b * (b - 1) if b >= 2 else 0
        gate(comm("Hv", "Fv", a, b) == expected_fv)
        gate(comm("Ev", "Fv", a, b) == Fraction(b) + Fraction(1, 2))
        for left in u_names:
            for right in v_names:
                gate(comm(left, right, a, b) == 0)
        hu = Fraction(a) + Fraction(1, 2)
        hv = Fraction(b) + Fraction(1, 2)
        gate(hu * hu + 2 * hu - (a + 2) * (a + 1) == Fraction(-3, 4))
        gate(hv * hv + 2 * hv - (b + 2) * (b + 1) == Fraction(-3, 4))

print(f"SUMMARY: {passed}/{total} gates passed")
if passed != total:
    raise SystemExit(1)
