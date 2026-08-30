import json

zero = (0, 0)
one = (1, 0)
i = (0, 1)


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def mul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


powers_minus_i = [one, (0, -1), (-1, 0), i]


def dft4(vector):
    out = []
    for k in range(4):
        total = zero
        for n, value in enumerate(vector):
            total = add(total, mul(powers_minus_i[(k * n) % 4], value))
        out.append(total)
    return out


primitive = [zero, one, zero, one]
dual_control = dft4(primitive)
second_turn = dft4(dual_control)
four_primitive = [(4 * a, 4 * b) for a, b in primitive]

checks = {
    "primitive_image_is_complementary_support": dual_control == [(2, 0), zero, (-2, 0), zero],
    "primitive_line_not_fourier_stable": dual_control != primitive,
    "second_turn_returns_scaled_reflection": second_turn == four_primitive,
    "fourier_orbit_needs_at_least_two_components": primitive != dual_control,
    "full_orbit_closes_after_two_turns": second_turn == four_primitive,
}

out = {
    "schema": "marici.grothendieck.primitive-fourier-orbit-closure.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "witness": {
        "primitive": primitive,
        "F_primitive": dual_control,
        "F2_primitive": second_turn,
    },
}

print(json.dumps(out, indent=2, sort_keys=True))
raise SystemExit(0 if out["passed"] else 1)

