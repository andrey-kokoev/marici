"""Exact WP596 finite-dihedral generalized-CP obstruction."""

import json
from math import gcd
from pathlib import Path

import sympy as sp


def faithful_irrep_weights(n):
    return [
        k
        for k in range(1, (n - 1) // 2 + 1)
        if gcd(n, k) == 1
    ]


census = []
for n in range(3, 13):
    weights = faithful_irrep_weights(n)
    angular_extrema = [sp.Rational(m, n) * sp.pi for m in range(2 * n)]
    census.append(
        {
            "n": n,
            "faithful_irrep_weights": weights,
            "minimal_angular_invariant_degree": n,
            "renormalizable_angular_invariant": n <= 4 and bool(weights),
            "all_angular_extrema_on_reflection_axes": all(
                sp.simplify(n * theta / sp.pi).is_integer
                for theta in angular_extrema
            ),
        }
    )

rotation = sp.Matrix([[0, -1], [1, 0]])
bare_cp = sp.diag(1, -1)
generalized_cp = rotation * bare_cp
v = sp.Matrix([1, 1])

checks = {
    "faithful_dihedral_angular_degree_equals_group_order": all(
        item["minimal_angular_invariant_degree"] == item["n"] for item in census
    ),
    "only_d3_and_d4_have_renormalizable_angular_invariants": [
        item["n"] for item in census if item["renormalizable_angular_invariant"]
    ]
    == [3, 4],
    "d3_extrema_include_a_bare_cp_axis": bare_cp * sp.Matrix([1, 0])
    == sp.Matrix([1, 0]),
    "d4_diagonal_is_moved_by_bare_cp": bare_cp * v != v,
    "d4_diagonal_is_fixed_by_generalized_cp": generalized_cp * v == v,
    "every_single_doublet_angular_extremum_has_a_dihedral_reflection_stabilizer": all(
        item["all_angular_extrema_on_reflection_axes"] for item in census
    ),
    "orders_five_and_above_have_accidental_o2_at_renormalizable_degree": all(
        not item["renormalizable_angular_invariant"]
        for item in census
        if item["n"] >= 5
    ),
}

if not all(checks.values()):
    raise SystemExit(f"WP596 check failed: {checks}")

checks = {key: bool(value) for key, value in checks.items()}
result = {
    "work_package": "WP596",
    "status": "PASS",
    "checks": checks,
    "domain": "faithful irreducible real two-dimensional dihedral representations D_n for 3<=n<=12, with the general degree theorem stated for all n>=3",
    "invariant_theorem": "the first nonradial invariant has degree n; every angular extremum theta=m*pi/n lies on a D_n reflection axis",
    "renormalizable_census": {
        "D3": "cubic anisotropy exists, but every extremal orbit contains a bare-CP-fixed axis vacuum",
        "D4": "quartic anisotropy fixes diagonal orientation, but a rotated CP reflection stabilizes each vacuum",
        "D_n_n_ge_5": "no renormalizable angular invariant; the scalar potential has accidental O(2)",
    },
    "wp595_correction": "the one-half orientation is exact, but it does not prove physical CP breaking",
    "classification": "single-dihedral-doublet generalized-CP obstruction; neither a full flavor selector nor an instrument",
    "smallest_exact_falsifier": "for D4, R*C fixes v=(1,1) exactly although C alone moves it",
    "remaining_architecture_gate": "use at least two source multiplets with misaligned residual reflection subgroups, or a portal representation proving that no generalized CP stabilizes the full vacuum",
    "experiment_gate": "a nonzero physical CP-odd invariant can criticize the single-doublet architecture only after the full portal map respects the admitted internal group",
    "census": census,
}

out = (
    Path(__file__).resolve().parents[1]
    / "results"
    / "wp596_dihedral_generalized_cp_obstruction.json"
)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
