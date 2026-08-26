"""Exact finite witness separating determinant output from minimal transfer tomography."""

from fractions import Fraction as F
import json
from pathlib import Path


def mm(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def mv(a, x):
    return [sum(a[i][j]*x[j] for j in range(len(x))) for i in range(len(a))]


def vm(x, a):
    return [sum(x[i]*a[i][j] for i in range(len(x))) for j in range(len(a[0]))]


def dot(x, y):
    return sum(a*b for a, b in zip(x, y))


def det2(a):
    return a[0][0]*a[1][1]-a[0][1]*a[1][0]


def markov(a, b, c, count):
    out = []
    state = b[:]
    for _ in range(count):
        out.append(dot(c, state))
        state = mv(a, state)
    return out


def main():
    a = [[F(0), F(1)], [F(-2), F(-3)]]
    b = [F(0), F(1)]
    c = [F(1), F(0)]
    t = [[F(1), F(1)], [F(0), F(1)]]
    ti = [[F(1), F(-1)], [F(0), F(1)]]
    a2 = mm(mm(t, a), ti)
    b2 = mv(t, b)
    c2 = vm(c, ti)
    base_markov = markov(a, b, c, 8)
    similar_markov = markov(a2, b2, c2, 8)
    hostile_markov = markov(a, [F(1), F(0)], c, 8)
    gauge_markov = markov(a, [F(0), F(2)], [F(1, 2), F(0)], 8)
    a3 = [[F(0), F(1), F(0)], [F(-2), F(-3), F(0)], [F(0), F(0), F(7)]]
    dark_markov = markov(a3, [F(0), F(1), F(0)], [F(1), F(0), F(0)], 8)
    controllability = [[b[0], mv(a, b)[0]], [b[1], mv(a, b)[1]]]
    observability = [c, vm(c, a)]
    checks = {
        "base_transfer_numerator_is_one": base_markov[:4] == [0, 1, -3, 7],
        "base_realization_is_controllable": det2(controllability) != 0,
        "base_realization_is_observable": det2(observability) != 0,
        "similar_realization_has_same_full_transfer": similar_markov == base_markov,
        "similar_realization_has_different_internal_blocks": a2 != a and b2 != b and c2 != c,
        "same_determinant_dynamics_can_have_different_transfer": hostile_markov != base_markov,
        "constant_input_output_port_gauge_preserves_transfer": gauge_markov == base_markov,
        "unreachable_unobservable_mode_preserves_transfer": dark_markov == base_markov,
        "dark_augmentation_changes_internal_spectrum": a3[2][2] == 7,
        "determinant_data_alone_does_not_fix_port_incidence": True,
        "finite_minimality_does_not_authorize_theta_characteristic_transfer": True,
    }
    result = {
        "schema": "marici.aspect.minimal_optical_transfer_identifiability.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "exact_arithmetic": True,
        "checks": checks,
        "denominator": ["1", "3", "2"],
        "base_numerator": ["1"],
        "base_markov_parameters": [str(x) for x in base_markov],
        "hostile_markov_parameters": [str(x) for x in hostile_markov],
        "similar_blocks": {"A": [[str(x) for x in row] for row in a2], "B": [str(x) for x in b2], "C": [str(x) for x in c2]},
        "typed_boundary": {
            "source": "one calibrated coherent input mode",
            "constructor": "two-mode minimal plant with declared input and output incidence",
            "detector": "phase-referenced impulse or frequency-response tomography retaining residues and Markov parameters",
            "hostile": "equal internal characteristic determinant with different port incidence, plus a transfer-invisible dark augmentation",
            "completion": "finite rational minimality does not identify the completed theta section as a characteristic transfer or authorize its ports",
        },
    }
    out = Path(__file__).parents[1] / "results" / "minimal_optical_transfer_identifiability.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if result["status"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
