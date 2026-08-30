"""Arb counterexample to total nonnegativity of the Burnol B kernel."""

from sage.all import RealBallField, matrix


R = RealBallField(256)
LENGTH = R(2).log()
RATES = [R(2 * n) + R(1) / 2 for n in range(1, 44)]


def kernel(t):
    return (t / 2).exp() - sum((-rate * t).exp() for rate in RATES)


AT_LENGTH = kernel(LENGTH)


def b_kernel(t):
    return AT_LENGTH - kernel(abs(t))


x = [R(11832377) / 10**8, R(15811552) / 10**8]
y = [R(7854827) / 10**8, R(11835137) / 10**8]
minor = matrix(R, [[b_kernel(a - b) for b in y] for a in x]).det()

print("schema=marici.burnol-b-kernel-tp2-counterexample.v1")
print(f"x={x}")
print(f"y={y}")
print(f"minor={minor}")
print(f"certified_negative={minor.upper() < 0}")
