"""Exact checks for the constructible-terminal rank obstruction."""

from fractions import Fraction
import json


def q(v):
    return sum(v, Fraction(0))


def sub_scaled(u, v, a, b):
    """Return b*u-a*v, where a=q(u), b=q(v)."""
    return tuple(b * x - a * y for x, y in zip(u, v))


u = (Fraction(1), Fraction(0))
v = (Fraction(0), Fraction(1))
a, b = q(u), q(v)
k = sub_scaled(u, v, a, b)

# Identity is the strongest possible terminal observer.
observed_k = k

checks = {
    "two_independent_states": u != v,
    "constructed_kernel_vector_nonzero": any(x != 0 for x in k),
    "constructed_vector_is_scalar_null": q(k) == 0,
    "identity_observer_is_faithful_on_kernel_vector": observed_k == k and any(x != 0 for x in observed_k),
    "canonical_hostile_is_scalar_null": q((Fraction(1), Fraction(-1))) == 0,
    "rank_one_control_is_transverse": q((Fraction(1),)) != 0,
}

result = {
    "schema": "marici.grothendieck.constructible-terminal-rank-obstruction.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "witness": {
        "u": [str(x) for x in u],
        "v": [str(x) for x in v],
        "kernel_vector": [str(x) for x in k],
        "scalar_readout": str(q(k)),
        "observer_output": [str(x) for x in observed_k],
    },
}

print(json.dumps(result, indent=2, sort_keys=True))
