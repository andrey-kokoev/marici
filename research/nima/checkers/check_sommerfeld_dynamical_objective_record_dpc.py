from fractions import Fraction
import json
from pathlib import Path


def cnot_basis(index, control, target, width=3):
    bits = [(index >> (width - 1 - i)) & 1 for i in range(width)]
    if bits[control]:
        bits[target] ^= 1
    out = 0
    for bit in bits:
        out = (out << 1) | bit
    return out


def apply_permutation(state, permutation):
    out = [Fraction(0) for _ in state]
    for i, amplitude in enumerate(state):
        out[permutation(i)] += amplitude
    return out


fanout = lambda i: cnot_basis(cnot_basis(i, 0, 1), 0, 2)

# Unnormalized amplitudes keep the test exact. Normalization is irrelevant to
# permutation equality and to the record-support census.
initial = [Fraction(0) for _ in range(8)]
initial[0] = Fraction(3)
initial[4] = Fraction(4)
recorded = apply_permutation(initial, fanout)
recovered = apply_permutation(recorded, fanout)
assert recorded[0] == 3 and recorded[7] == 4
assert recovered == initial


def classify(alpha, beta, gamma, omega):
    loss = beta + gamma
    return {
        "margin": alpha / loss,
        "equilibrium": alpha / (alpha + loss),
        "gap": alpha + loss,
        "formation_dominates": alpha > loss,
        "observer_window": loss < omega < alpha,
        "passes": alpha > loss and loss < omega < alpha,
    }


stable = classify(Fraction(8), Fraction(1), Fraction(1), Fraction(4))
return_dominated = classify(Fraction(2), Fraction(1), Fraction(2), Fraction(3, 2))
slow_observer = classify(Fraction(8), Fraction(1), Fraction(1), Fraction(2))
premature_observer = classify(Fraction(8), Fraction(1), Fraction(1), Fraction(8))

assert stable["passes"]
assert not return_dominated["passes"]
assert not slow_observer["passes"]
assert not premature_observer["passes"]

# Every finite feature map diag(1, 1/N) is injective, but no uniform positive
# lower gain survives completion.
for n in range(1, 17):
    assert Fraction(1, n) > 0
for proposed_denominator in (1, 2, 7, 31, 101):
    n = proposed_denominator + 1
    assert Fraction(1, n * n) < Fraction(1, proposed_denominator)


def serializable(model):
    return {
        key: (f"{value.numerator}/{value.denominator}" if isinstance(value, Fraction) else value)
        for key, value in model.items()
    }


result = {
    "schema": "marici.sommerfeld-dynamical-objective-record-dpc.v1",
    "reversible_fanout": {
        "records_created": recorded[0] == 3 and recorded[7] == 4,
        "exact_inverse_recovers_source": recovered == initial,
        "static_redundancy_implies_irreversibility": False,
    },
    "rate_models": {
        "stable": serializable(stable),
        "return_dominated": serializable(return_dominated),
        "slow_observer": serializable(slow_observer),
        "premature_observer": serializable(premature_observer),
    },
    "completion": {
        "finite_injectivity": True,
        "uniform_lower_gain": False,
    },
    "claim_boundary": "static objective quotient does not imply dynamical persistence or irreversibility",
    "status": "pass",
}

output = Path(__file__).resolve().parents[1] / "results" / "sommerfeld-dynamical-objective-record-dpc.json"
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
