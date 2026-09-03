from __future__ import annotations

import json
import sympy as sp


def order_norm(labels: list[sp.Rational], coeffs: list[sp.Rational]) -> sp.Rational:
    assert sum(coeffs) == 0
    value = sp.Rational(0)
    for i in range(len(labels) - 1):
        tail = sum(coeffs[i + 1 :])
        value += 2 * (labels[i + 1] - labels[i]) * tail**2
    return sp.simplify(value)


def main() -> None:
    labels = [sp.Rational(0), sp.Rational(2), sp.Rational(5), sp.Rational(9)]
    amplitudes = [sp.Rational(3), sp.Rational(-1), sp.Rational(4)]
    total = sum(amplitudes)
    anchored = [-total, *amplitudes]
    assert sum(anchored) == 0

    # Change the anchor from label 0 to label 2 while retaining source amplitudes
    # at labels 5 and 9; the difference is total mass times an adjacent dipole.
    source = [sp.Rational(-1), sp.Rational(4)]
    mass = sum(source)
    anchor_at_0 = [-mass, 0, *source]
    anchor_at_2 = [0, -mass, *source]
    residual = [a - b for a, b in zip(anchor_at_0, anchor_at_2)]
    assert residual == [-mass, mass, 0, 0]
    assert order_norm(labels, residual) == 2 * mass**2 * (labels[1] - labels[0])

    result = {
        "schema":"marici.voevodsky.anchored-zero-sum-lift-check.v1",
        "status":"anchor_residual_verified",
        "zero_sum_lift_constructed":True,
        "anchor_change_residual":"mass*(e_b-e_a)",
        "anchor_change_norm_squared":"2*|mass|^2*|lambda_b-lambda_a|",
        "canonical_anchor_source_derived":False,
        "prime_amplitude_map_constructed":False,
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
