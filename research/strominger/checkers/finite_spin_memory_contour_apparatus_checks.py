"""Exact rank checks for the finite 45-contour spin-memory apparatus."""

import hashlib
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
ARTIFACT = ROOT / "research/strominger/finite-spin-memory-contour-apparatus.md"
x = sp.symbols("x", real=True)

latitudes = [sp.Rational(-2, 3), sp.Rational(-1, 3), sp.Integer(0),
             sp.Rational(1, 3), sp.Rational(2, 3)]
longitude_count = 9
degrees = [2, 3, 4]

cap_integrals = {
    degree: sp.integrate(sp.legendre(degree, x), (x, sp.Rational(1, 2), 1))
    for degree in degrees
}
expected_cap_integrals = {
    2: sp.Rational(3, 16),
    3: sp.Rational(3, 128),
    4: sp.Rational(-15, 256),
}

latitude_blocks = {}
for abs_m in range(5):
    admitted = [degree for degree in degrees if degree >= abs_m]
    matrix = sp.Matrix([
        [sp.assoc_legendre(degree, abs_m, latitude) for degree in admitted]
        for latitude in latitudes
    ])
    latitude_blocks[abs_m] = {
        "admitted_degrees": admitted,
        "rank": matrix.rank(),
        "columns": len(admitted),
    }

checks = {
    "five_distinct_latitudes": len(set(latitudes)) == 5,
    "nine_longitudes_resolve_m_minus4_through4": all(
        (left - right) % longitude_count != 0
        for left in range(-4, 5)
        for right in range(-4, 5)
        if left != right
    ),
    "cap_integrals_exact": cap_integrals == expected_cap_integrals,
    "all_cap_weights_nonzero": all(value != 0 for value in cap_integrals.values()),
    "all_contour_curvature_multipliers_nonzero": all(
        (degree - 1) * degree * (degree + 1) * (degree + 2) != 0
        for degree in degrees
    ),
    "each_latitude_block_full_column_rank": all(
        block["rank"] == block["columns"] for block in latitude_blocks.values()
    ),
    "total_complex_harmonic_rank_is_21": (
        latitude_blocks[0]["rank"]
        + 2 * sum(latitude_blocks[abs_m]["rank"] for abs_m in range(1, 5))
    ) == 21,
    "apparatus_port_count_is_45": len(latitudes) * longitude_count == 45,
    "rank_lower_bound_is_21": sum(2 * degree + 1 for degree in degrees) == 21,
    "apparatus_not_claimed_minimal": True,
    "apparatus_not_claimed_deletion_tolerant": True,
    "no_row_reduced_subfamily_given_source_authority": True,
}

failed = [name for name, passed in checks.items() if not passed]
payload = {
    "schema": "marici.strominger.finite-spin-memory-contour-apparatus-result.v1",
    "artifact_sha256": hashlib.sha256(ARTIFACT.read_bytes()).hexdigest().upper(),
    "passed": sum(checks.values()),
    "total": len(checks),
    "checks": checks,
    "observed": {
        "latitudes_cos_theta": [str(value) for value in latitudes],
        "longitude_count": longitude_count,
        "cap_radius": "pi/3",
        "cap_integrals_without_2pi": {
            str(degree): str(value) for degree, value in cap_integrals.items()
        },
        "latitude_blocks": latitude_blocks,
        "port_count": 45,
        "low_block_rank": 21,
        "minimum_possible_scalar_port_count": 21,
    },
    "verdict": "Five rational latitude rings, nine uniform longitudes, and common radius-pi/3 caps form an explicit 45-contour physical spin-memory apparatus of exact rank 21 on l=2,3,4. Minimality and robustness remain open.",
}
print(json.dumps(payload, indent=2, sort_keys=True))
if failed:
    raise SystemExit("failed checks: " + ", ".join(failed))
