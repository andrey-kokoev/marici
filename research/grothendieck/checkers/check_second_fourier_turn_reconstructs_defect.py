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
    return [
        sum_gaussian(
            mul(powers_minus_i[(k * n) % 4], value)
            for n, value in enumerate(vector)
        )
        for k in range(4)
    ]


def sum_gaussian(values):
    total = zero
    for value in values:
        total = add(total, value)
    return total


omega = [one, one, one, one]
control = [one, zero, zero, zero]
g = [one, (-1, 0), zero, zero]

f_omega = dft4(omega)
f_control = dft4(control)
f2_g = dft4(dft4(g))
reflected_g_times_four = [(4, 0), zero, zero, (-4, 0)]

checks = {
    "first_turn_augmentation_to_control": f_omega == [(4, 0), zero, zero, zero],
    "second_leg_control_to_augmentation": f_control == omega,
    "two_turns_equal_scaled_reflection": f2_g == reflected_g_times_four,
    "scalar_nullity_survives_reflection": sum(x[0] for x in f2_g) == 0,
    "faithful_defect_survives_two_turns": any(value != zero for value in f2_g),
}

out = {
    "schema": "marici.grothendieck.second-fourier-turn-reconstructs-defect.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "witness": {
        "F_omega": f_omega,
        "F_control": f_control,
        "g": g,
        "F2_g": f2_g,
    },
}

print(json.dumps(out, indent=2, sort_keys=True))
raise SystemExit(0 if out["passed"] else 1)

