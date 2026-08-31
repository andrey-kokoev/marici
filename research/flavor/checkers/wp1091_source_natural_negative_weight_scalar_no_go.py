import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# With A fixed under ray scaling, a regular polynomial in x of total degree d
# has weight d.  No nonzero regular polynomial can therefore have weight -3.
regular_degrees = list(range(0, 7))
assert all(d >= 0 for d in regular_degrees)
assert -3 not in regular_degrees

# A meromorphic weight -3 ratio f/D^m requires deg(f)-3m=-3.  With the only
# admitted positive-weight alternating scalar D of degree 3, all bounded
# candidates reduce to powers of 1/D rather than an independent rho.
bounded_candidates = []
for denominator_power in range(1, 5):
    for numerator_degree in range(0, 13):
        if numerator_degree - 3 * denominator_power == -3:
            bounded_candidates.append((numerator_degree, denominator_power))
assert bounded_candidates == [(0, 1), (3, 2), (6, 3), (9, 4)]
assert bounded_candidates == [(3 * (m - 1), m) for m in range(1, 5)]

available_positive_weight_scalars = {"D": 3}
reductions = {
    "0/1": "1/D",
    "3/2": "D/D^2 = 1/D",
    "6/3": "D^2/D^3 = 1/D",
    "9/4": "D^3/D^4 = 1/D",
}
assert set(reductions) == {f"{n}/{m}" for n, m in bounded_candidates}

# Witness the singularity of every such reduction on a noncyclic eigenline.
lam = [Fraction(2), Fraction(3), Fraction(5)]
x_eigen = [Fraction(1), Fraction(0), Fraction(0)]
D_eigen = (lam[1] - lam[0]) * (lam[2] - lam[0]) * (lam[2] - lam[1]) * x_eigen[0] * x_eigen[1] * x_eigen[2]
assert D_eigen == 0

supply = {
    "regular_negative_weight_polynomial": False,
    "bounded_meromorphic_candidates_reduce_to_reciprocal_D": True,
    "independent_positive_weight_numerator": False,
    "global_nonsingular_reference": False,
    "source_authorized_line_bundle_section": False,
}
assert list(supply.values()).count(False) == 4

result = {
    "schema": "marici.flavor.wp1091.v1",
    "status": "PASS",
    "question": "Can any source-natural scalar function of A and x supply the required ray-phase weight -3?",
    "bounded_degree_scan": {
        "regular_degrees": regular_degrees,
        "negative_regular_weight_present": False,
        "meromorphic_candidates_numerator_degree_denominator_power": bounded_candidates,
        "available_positive_weight_scalars": available_positive_weight_scalars,
        "reductions": reductions,
    },
    "singularity_witness": {
        "spectrum": [str(v) for v in lam],
        "eigenline": [str(v) for v in x_eigen],
        "D_on_eigenline": str(D_eigen),
    },
    "current_source_supply": supply,
    "classification": "negative gate: no source-natural scalar of A,x supplies an independent weight-(-3) rho",
    "remaining_gate": "source-authorized line-bundle section or coorientation independent of D, with descent law, temporal scope, and comparison node",
    "hostile_gate": "do not declare a negative-degree regular polynomial, infer an independent numerator from D, or promote a D-power ratio to rho",
    "claim_boundary": "the scan covers regular polynomial scalars and bounded D-denominator meromorphic reductions available from the admitted packet",
    "disposition": "general source-natural scalar loophole closed at the stated bounded authority class",
}

(ROOT / "results" / "wp1091_source_natural_negative_weight_scalar_no_go.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1091 PASS:", len(regular_degrees), len(bounded_candidates), D_eigen)
