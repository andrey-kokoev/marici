from fractions import Fraction
import json

Z = (Fraction(0), Fraction(0))
O = (Fraction(1), Fraction(0))
I = (Fraction(0), Fraction(1))


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def mul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def conj(a):
    return (a[0], -a[1])


def scale(a, c):
    return (c * a[0], c * a[1])


def inner(x, y):
    total = Z
    for a, b in zip(x, y):
        total = add(total, mul(conj(a), b))
    return total


powers_minus_i = [O, (Fraction(0), Fraction(-1)), (Fraction(-1), Fraction(0)), I]


def unitary_dft4(vector):
    out = []
    for k in range(4):
        total = Z
        for n, value in enumerate(vector):
            total = add(total, mul(powers_minus_i[(k * n) % 4], value))
        out.append(scale(total, Fraction(1, 2)))
    return out


x = [O, (Fraction(-1), Fraction(0)), Z, Z]
h = [Z, O, (Fraction(-1), Fraction(0)), Z]
omega = [O, O, O, O]

ux = unitary_dft4(x)
uh = unitary_dft4(h)
uomega = unitary_dft4(omega)

source_bivector_energy = inner(omega, omega)[0] * inner(x, x)[0] - inner(omega, x)[0] ** 2
dual_bivector_energy = inner(uomega, uomega)[0] * inner(ux, ux)[0] - (
    inner(uomega, ux)[0] ** 2 + inner(uomega, ux)[1] ** 2
)

checks = {
    "state_norm_preserved": inner(ux, ux) == inner(x, x),
    "forcing_norm_preserved": inner(uh, uh) == inner(h, h),
    "forcing_state_pairing_preserved": inner(uh, ux) == inner(h, x),
    "endpoint_anchor_transported": uomega == [(Fraction(2), Fraction(0)), Z, Z, Z],
    "bivector_endpoint_energy_preserved": source_bivector_energy == dual_bivector_energy,
}

out = {
    "schema": "marici.grothendieck.unitary-fourier-full-green-packet.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "witness": {
        "state_norm": str(inner(x, x)[0]),
        "forcing_norm": str(inner(h, h)[0]),
        "forcing_state_pairing": [str(v) for v in inner(h, x)],
        "source_bivector_energy": str(source_bivector_energy),
        "dual_bivector_energy": str(dual_bivector_energy),
    },
}

print(json.dumps(out, indent=2, sort_keys=True))
raise SystemExit(0 if out["passed"] else 1)

