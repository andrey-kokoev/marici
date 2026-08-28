"""WP990: exact joint faithfulness of q and k/q on the physical quotient."""

import json
from fractions import Fraction as F
from pathlib import Path


r_q = (F(0), F(2), F(0), F(-1))
r_rho = (F(2), F(4), F(-1), F(-5))
n_s = (F(-1, 2), F(0), F(-1), F(0))
n_A = (F(-3, 2), F(-1, 2), F(0), F(-1))


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def rank(rows):
    a = [list(row) for row in rows]
    pivots = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(pivots, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[pivots], a[pivot] = a[pivot], a[pivots]
        p = a[pivots][col]
        a[pivots] = [x / p for x in a[pivots]]
        for i in range(len(a)):
            if i != pivots and a[i][col]:
                q = a[i][col]
                a[i] = [x - q * y for x, y in zip(a[i], a[pivots])]
        pivots += 1
        if pivots == len(a):
            break
    return pivots


response_rank = rank((r_q, r_rho))
normalization_rank = rank((n_s, n_A))
combined_rank = rank((n_s, n_A, r_q, r_rho))

checks = {
    "q_row_descends": dot(r_q, n_s) == dot(r_q, n_A) == 0,
    "rho_row_descends": dot(r_rho, n_s) == dot(r_rho, n_A) == 0,
    "response_rank_two": response_rank == 2,
    "response_kernel_dimension_two": 4 - response_rank == 2,
    "normalization_orbit_rank_two": normalization_rank == 2,
    "kernel_equals_normalization_orbit": combined_rank == 4,
    "minimal_complement_count_is_one": rank((r_rho,)) == 1
    and response_rank == 2,
}

result = {
    "schema": "marici.flavor.wp990-two-response-physical-quotient-closure.v1",
    "status": "PASS" if all(checks.values()) else "FAIL",
    "checks": checks,
    "source_authorized_probe_family": ["q=mu^2/(2 m_A^2)", "rho=k/q"],
    "contextual_partition": "equality classes are exactly kinetic-normalization orbits",
    "separates_physical_points": True,
    "selects_proper_subfamily": False,
    "rigidifies_presentation": False,
    "requires_reference_port": False,
    "has_physical_instrument": False,
    "classification": "source-derived faithful quotient separator; neither selector nor rigidifier",
    "smallest_exact_falsifier": "a non-normalization tangent annihilated by both q and k/q",
    "remaining_physical_instrument_gate": "a common-frame calibrated rank-two source-to-record map for the q and k/q quotient directions",
}

out = Path(__file__).parents[1] / "results" / "wp990_two_response_physical_quotient_closure.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
