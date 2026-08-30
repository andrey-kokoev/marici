"""Hostile test of G0>0 on 0<R<T<1 and 0<p<1."""

import json
import random


def g0(t, r, p):
    return (
        -3*r**4*t*p**2 + 3*r**3*t**2*p - r**3*p
        + 4*r**2*t**3 + 4*r**2*t*p**2 - 4*r**2*t
        - 3*r*t**2*p + r*p - 4*t**5 + 4*t**3 - t*p**2
    )


rng = random.Random(20260823)
trials = 1_000_000
minimum = (float("inf"), None)
negative = 0
critical_admissible = 0
critical_d_nonnegative = 0
critical_worst_d = (-float("inf"), None)
for _ in range(trials):
    t = rng.random()
    r = rng.random() * t
    p = rng.random()
    value = g0(t, r, p)
    if value < minimum[0]:
        minimum = (value, (t, r, p))
    if value < -1e-14:
        negative += 1
    z = r / t if t else 0.0
    x = t * t
    d = p - z + x * (-2*p*p*z + 3*p*z*z - 2*p + z)
    # G_q has the same sign as d in ratio coordinates.
    if abs(d) > 1e-15:
        q_critical = -value / d
        if 0.0 < q_critical < p:
            critical_admissible += 1
            if d >= 0.0:
                critical_d_nonnegative += 1
                if d > critical_worst_d[0]:
                    critical_worst_d = (d, (t, r, p, q_critical))

print(json.dumps({
    "trials": trials,
    "negative_beyond_1e-14": negative,
    "minimum": minimum,
    "algebraic_critical_packages_with_0_q_p": critical_admissible,
    "such_packages_with_D_nonnegative": critical_d_nonnegative,
    "largest_nonnegative_D_package": critical_worst_d,
}, indent=2))
