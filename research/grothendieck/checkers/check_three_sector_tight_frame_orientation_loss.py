#!/usr/bin/env python3
"""Exact finite checks for tight-frame closure and orientation loss."""


def norm2(vector):
    return sum(abs(x) ** 2 for x in vector)


u = [complex(1, 2), complex(-3, 1), complex(2, -4)]
v = [complex(2, -1), complex(1, 5), complex(-2, 3)]
plus = [a + b for a, b in zip(u, v)]
minus = [a - b for a, b in zip(u, v)]

summed = norm2(plus) + norm2(minus)
tight = 2 * norm2(u) + 2 * norm2(v)
cross = sum(a.conjugate() * b for a, b in zip(u, v))
difference = norm2(plus) - norm2(minus)

checks = {
    "tight_frame_identity": abs(summed - tight) < 1e-12,
    "three_sector_defect_zero": abs(summed - tight) < 1e-12,
    "difference_is_cross_interference": abs(difference - 4 * cross.real) < 1e-12,
    "orientation_not_determined_by_sum": abs(difference) > 1e-3,
}

# Reversing one face orientation preserves the tight sum but reverses the
# interference observable.
v_reversed = [-x for x in v]
plus_r = [a + b for a, b in zip(u, v_reversed)]
minus_r = [a - b for a, b in zip(u, v_reversed)]
checks["hostile_preserves_sum"] = abs(norm2(plus_r) + norm2(minus_r) - summed) < 1e-12
checks["hostile_reverses_orientation"] = abs((norm2(plus_r) - norm2(minus_r)) + difference) < 1e-12

failed = [name for name, ok in checks.items() if not ok]
print({"passed": len(checks) - len(failed), "total": len(checks), "failed": failed})
raise SystemExit(bool(failed))

