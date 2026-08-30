import json

# Gaussian integers are represented as (real, imaginary).
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
            phase = powers_minus_i[(k * n) % 4]
            total = add(total, mul(phase, value))
        out.append(total)
    return out


omega = [one, one, one, one]
g = [one, (-1, 0), zero, zero]
fourier_omega = dft4(omega)
fourier_g = dft4(g)
control = [one, zero, zero, zero]

checks = {
    "augmentation_maps_to_four_times_control": fourier_omega == [(4, 0), zero, zero, zero],
    "augmentation_line_not_preserved": fourier_omega != omega,
    "scalar_null_source_has_zero_control_frequency": fourier_g[0] == zero,
    "nonzero_dual_state_survives": any(value != zero for value in fourier_g[1:]),
    "transported_exterior_anchor_is_control": fourier_omega[0] == (4, 0),
}

out = {
    "schema": "marici.grothendieck.fourier-augmentation-control-rotation.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "witness": {
        "omega": omega,
        "fourier_omega": fourier_omega,
        "g": g,
        "fourier_g": fourier_g,
        "control": control,
    },
}

print(json.dumps(out, indent=2, sort_keys=True))
raise SystemExit(0 if out["passed"] else 1)

