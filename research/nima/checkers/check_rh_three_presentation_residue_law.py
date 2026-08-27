"""Exact finite model for the three-presentation, two-leg, one-residue law."""

from fractions import Fraction
import hashlib
import json
from pathlib import Path


def l_plus(a):
    return Fraction(a), Fraction(0)


def l_minus(b):
    return Fraction(0), Fraction(b)


def delta(a, b):
    plus = l_plus(a)
    minus = l_minus(b)
    return plus[0] - minus[0], plus[1] - minus[1]


def rho(vector):
    return vector[0] + vector[1]


def h(residue):
    residue = Fraction(residue)
    return residue, -residue


def cone_residual(a, b, residue):
    comparison = delta(a, b)
    lifted = h(residue)
    return comparison[0] - lifted[0], comparison[1] - lifted[1]


# Scalar cancellation with a nonzero comparison residue and trivial strict pullback.
comparison = delta(1, 1)
assert comparison == (Fraction(1), Fraction(-1))
assert rho(comparison) == 0
assert comparison != (Fraction(0), Fraction(0))

# Exactness: every vector in ker rho has the form h(r).
kernel_samples = [
    (Fraction(-3), Fraction(3)),
    (Fraction(0), Fraction(0)),
    (Fraction(5, 2), Fraction(-5, 2)),
]
for vector in kernel_samples:
    assert rho(vector) == 0
    assert h(vector[0]) == vector

# Every scalar zero a-b=0 lifts to a cone state with residue a.
zero_samples = [Fraction(-3), Fraction(0), Fraction(5, 2)]
for value in zero_samples:
    assert rho(delta(value, value)) == 0
    assert cone_residual(value, value, value) == (Fraction(0), Fraction(0))

# A nonzero scalar readout cannot be repaired by h because rho h = 0.
nonzero_comparison = delta(Fraction(2), Fraction(1))
assert rho(nonzero_comparison) == 1
for residue in [Fraction(-2), Fraction(0), Fraction(3)]:
    assert cone_residual(2, 1, residue) != (Fraction(0), Fraction(0))

# A wrong final cell does not classify the readout kernel.
def h_wrong(residue):
    return Fraction(residue), Fraction(0)


assert rho(h_wrong(1)) != 0
assert h_wrong(1) != comparison

payload = {
    "schema": "marici.research.check.v1",
    "claim": "three presentations and two incidence legs need an exact residue classifier to lift scalar zeros",
    "strict_pullback_hostile": {
        "comparison_residue": [str(x) for x in comparison],
        "scalar_readout": str(rho(comparison)),
        "strict_equalizer_witness": False,
    },
    "residue_exactness_samples": len(kernel_samples),
    "zero_lift_samples": len(zero_samples),
    "wrong_cell_rejected": True,
    "verdict": "final plus-one must be an exact residue classifier",
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
payload["sha256"] = hashlib.sha256(canonical).hexdigest()

out = Path(__file__).parents[1] / "results" / "rh-three-presentation-residue-law.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
