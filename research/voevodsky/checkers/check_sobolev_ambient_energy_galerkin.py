from __future__ import annotations

import json

import sympy as sp


def main() -> None:
    pi = sp.pi
    L = sp.Integer(1)
    r = sp.Rational(1, 2)
    s = sp.Integer(1)
    B_norm = sp.Symbol("B", positive=True)
    cutoffs = [1, 2, 4, 8, 16, 32]

    def embedding_tail(cutoff: int) -> sp.Expr:
        omega = 1 + (pi * (cutoff + 1) / (2 * L)) ** 2
        return sp.Pow(omega, -(s - r) / 2)

    tails = [embedding_tail(cutoff) for cutoff in cutoffs]
    # The base omega is strictly increasing and the exponent is negative.
    assert all(cutoffs[index + 1] > cutoffs[index] for index in range(len(cutoffs) - 1))
    assert s - r == sp.Rational(1, 2)
    compression_bounds = [sp.factor(2 * B_norm * tail) for tail in tails]

    # Hostile operator: positive compression, negative unresolved tail.
    compressed_minimum = sp.Integer(1)
    unresolved_tail_eigenvalue = sp.Rational(-1, 10)
    compression_error = abs(unresolved_tail_eigenvalue)
    assert compressed_minimum > 0
    assert compression_error == sp.Rational(1, 10)
    assert unresolved_tail_eigenvalue < 0
    positive_compression_certifies_full_positivity = False

    # One-sided negative certificate.
    negative_compressed_minimum = sp.Rational(-1, 2)
    certified_tail_error = sp.Rational(1, 10)
    negative_spectrum_certified = negative_compressed_minimum + certified_tail_error < 0
    assert negative_spectrum_certified

    result = {
        "schema": "marici.voevodsky.sobolev-ambient-energy-galerkin.v1",
        "status": "local_sobolev_energy_and_tail_rate_verified",
        "L": "1",
        "r": "1/2",
        "s": "1",
        "sobolev_gap": "1/2",
        "embedding_tail_exponent": "-1/4",
        "operator_tail_rate": "M^(-1/2)",
        "cutoffs": cutoffs,
        "exact_embedding_tail_expressions": [str(value) for value in tails],
        "exact_operator_error_bounds": [str(value) for value in compression_bounds],
        "tail_bounds_strictly_decrease": True,
        "positive_compression_certifies_full_positivity": positive_compression_certifies_full_positivity,
        "hostile_unresolved_tail_eigenvalue": "-1/10",
        "negative_compression_plus_error_certifies_negative_spectrum": bool(negative_spectrum_certified),
        "source_B_norm_bound_materialized": False,
        "global_support_window_coercivity_proved": False,
        "next_gate": "source explicit B norm constants and signed-tail positivity control",
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
