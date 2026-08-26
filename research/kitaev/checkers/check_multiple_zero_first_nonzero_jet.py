#!/usr/bin/env python3
"""Exact audit of rank-two observability at multiple zeros."""

import hashlib
import json
from math import factorial
from pathlib import Path

from sympy import I, Matrix, Rational, Symbol, conjugate, diff, simplify


ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/kitaev/results/multiple-zero-first-nonzero-jet.json"


def adjoint(M):
    return conjugate(M.T)


def main():
    s = Symbol("s")
    multiplicity_checks = []
    for m in range(1, 7):
        F = s**m
        jets = [simplify(diff(F, s, k).subs(s, 0) / factorial(k)) for k in range(m + 1)]
        assert all(jet == 0 for jet in jets[:m])
        assert jets[m] == 1
        lower_ranks = []
        for k in range(m):
            rows = Matrix([[1, jets[k]], [1, -jets[k]]])
            assert rows.rank() == 1
            lower_ranks.append(rows.rank())
        rows_m = Matrix([[1, jets[m]], [1, -jets[m]]])
        gram_m = adjoint(rows_m) * rows_m
        assert rows_m.rank() == 2
        assert gram_m == Matrix([[2, 0], [0, 2]])
        multiplicity_checks.append({
            "multiplicity": m,
            "lower_jet_ranks": lower_ranks,
            "first_nonzero_jet": str(jets[m]),
            "rank_at_first_nonzero_jet": rows_m.rank(),
        })

    # Exact complex coefficient and sheet swap.
    z = Rational(2, 3) + Rational(1, 2) * I
    rows = Matrix([[1, z], [1, -z]])
    gram = (adjoint(rows) * rows).applyfunc(simplify)
    expected = Matrix([[2, 0], [0, 2 * conjugate(z) * z]]).applyfunc(simplify)
    assert gram == expected
    assert simplify(gram.det()) == Rational(25, 9)
    swap = Matrix([[0, 1], [1, 0]])
    assert swap * rows == Matrix([[1, -z], [1, z]])
    assert adjoint(swap * rows) * (swap * rows) == adjoint(rows) * rows

    # Any fixed finite jet tower misses sufficiently high multiplicity.
    fixed_order = 3
    missed = []
    for N in range(fixed_order + 1, fixed_order + 6):
        F = s**N
        visible_jets = [diff(F, s, k).subs(s, 0) for k in range(fixed_order + 1)]
        assert all(value == 0 for value in visible_jets)
        missed.append({"multiplicity": N, "visible_through_order": fixed_order, "all_visible_jets_zero": True})

    # Full finite rank with collapsing source-direction energy.
    collapse = []
    source_direction = Matrix([0, 1])
    for N in (2, 3, 5, 10, 20):
        zN = Rational(1, N)
        rows_N = Matrix([[1, zN], [1, -zN]])
        gram_N = rows_N.T * rows_N
        assert rows_N.rank() == 2
        energy = (source_direction.T * gram_N * source_direction)[0]
        assert energy == 2 * zN**2
        collapse.append({"N": N, "source_direction_energy": str(energy)})

    payload = {
        "schema": "marici.kitaev.multiple_zero_first_nonzero_jet.v1",
        "status": "pass",
        "strength": "finite rank-two jet-incidence theorem",
        "multiplicity_checks": multiplicity_checks,
        "complex_sheet_pair": {
            "z": str(z),
            "gramian": [[str(value) for value in gram.row(i)] for i in range(2)],
            "determinant": str(simplify(gram.det())),
            "sheet_swap_preserves_gramian": True,
        },
        "fixed_finite_tower_hostile": missed,
        "collapsing_nonzero_jet_family": collapse,
        "limiting_source_direction_energy": "0",
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope_exclusions": [
            "full generalized zero chain", "theta higher-jet derivation",
            "Riemann-zero multiplicity bound", "zero orientation",
            "completion stability", "RH"
        ],
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
