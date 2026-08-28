"""Dependency-free exact finite model of the moving-seam ternary identity."""

from fractions import Fraction


source = [Fraction(2), Fraction(3), Fraction(-1), Fraction(4), Fraction(1, 2)]
odd_character = [Fraction(0), Fraction(1), Fraction(-2), Fraction(3), Fraction(-1)]


def at(values, index):
    return values[index] if 0 <= index < len(values) else Fraction(0)


def window(length):
    return sum(
        2 * at(source, q) * at(source, q + d) * at(odd_character, d)
        for q in range(length)
        for d in range(len(source))
    )


checks = 0
assert window(0) == 0
checks += 1
for length in range(len(source)):
    increment = window(length + 1) - window(length)
    relative_tail = 2 * sum(
        at(source, length + d) * at(odd_character, d)
        for d in range(len(source))
    )
    local_response = at(source, length) * relative_tail
    assert increment == local_response
    checks += 1

full_direct = sum(
    2 * at(source, q) * at(source, q + d) * at(odd_character, d)
    for q in range(len(source))
    for d in range(len(source))
)
assert window(len(source)) == full_direct
checks += 1

print(f"PASS {checks}/{checks}: moving-seam ternary window differentiates to the relative response")

