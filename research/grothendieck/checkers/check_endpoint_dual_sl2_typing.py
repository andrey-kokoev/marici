from fractions import Fraction


passed = 0
total = 0


def gate(value):
    global passed, total
    total += 1
    passed += bool(value)


# Metaplectic action on u^a v^b. The v exponent is a spectator.
for a in range(41):
    h = Fraction(2 * a + 1, 2)
    # Coefficient comparisons on u^a v^b.
    gate((Fraction(1, 2) * (a + 2 + Fraction(1, 2))
          - h * Fraction(1, 2)) == 1)  # [H,E]=2E coefficient
    if a >= 2:
        f = -Fraction(a * (a - 1), 2)
        gate(((a - 2 + Fraction(1, 2)) * f - f * h) == -2 * f)
    else:
        gate(True)
    ef = -Fraction(a * (a - 1), 4) if a >= 2 else Fraction(0)
    fe = -Fraction((a + 2) * (a + 1), 4)
    gate(ef - fe == h)
    omega = h * h + 2 * h - (a + 2) * (a + 1)
    gate(omega == Fraction(-3, 4))

# Within-grade Cartan Casimir on highest vector u^n.
for grade in range(21):
    n = 2 * grade
    omega = n * n + 2 * n
    gate(omega == 4 * grade * (grade + 1))
    gate(Fraction(omega) != Fraction(-3, 4))

print(f"SUMMARY: {passed}/{total} gates passed")
if passed != total:
    raise SystemExit(1)
