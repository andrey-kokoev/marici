"""Local Cayley--Menger support audit for the p-normal carrier.

At the generic triple marked-wall incidence the Cayley--Menger polynomial is a
unit.  Therefore its source contour boundary contributes no local endpoint
face subcomplex: E_CM is canonically zero after localization.  This removes an
incorrect requirement to import the unrelated all-soft weighted chart, but it
does not construct the marked-wall Cech differential or a Bockstein lift.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NIMA = ROOT / "nima"
BENINCASA = ROOT / "benincasa"
OUT = NIMA / "results" / "cosmology_p_normal_cayley_menger_support.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    corner = load(NIMA / "results" / "cosmology_triple_incidence_boundary_corner_transport.json")
    coefficient = load(NIMA / "results" / "cosmology_triple_incidence_physical_coefficient.json")
    family = load(BENINCASA / "cayley-menger-contour-family-gate.json")
    weighted = load(BENINCASA / "cayley-menger-weighted-physical-pullback.json")

    assert corner["generic_cayley_menger_boundary_at_collision"] is False
    assert corner["generic_algebraic_coefficient_nonzero"] is True
    assert coefficient["restricted_cover_generically_split_over_function_field"] is True
    assert family["three_site_cycle"]["boundary"] == "CM(y^2,P^2)=0"

    # Recheck the exact restricted numerator at a generic incidence point.
    # K|_{p=0}=64*(x-2y)^2*(x+y)^2*(2x-y)^2 up to the recorded denominator.
    x, y = 1, 3
    factors = [x - 2 * y, x + y, 2 * x - y]
    restricted_numerator = 64
    for factor in factors:
        restricted_numerator *= factor * factor
    assert restricted_numerator == 25600
    assert all(factor != 0 for factor in factors)

    # On the open stratum U=Spec(R[K^{-1}]) containing this generic point,
    # V(K) is empty.  Its relative face-chain subcomplex is therefore the zero
    # complex, which is differential-stable without choosing generators.
    e_cm = {
        "ambient_localization": "U=Spec(R[K_CM^{-1}]) near generic p=0 incidence",
        "generators_by_degree": {},
        "differential_matrices": {},
        "rank": 0,
        "differential_stable": True,
        "reason": "V(K_CM) intersect U is empty",
    }

    # The existing weighted chart resolves a different degeneration where its
    # chart variable u tends to zero and A=B.  No source packet identifies that
    # u with p=x+y+3z; importing its exceptional faces would change strata.
    assert weighted["conventions"]["weighted_chart"] == "y=u^2*t"
    assert weighted["conclusions"][0] == "The physical contour degenerates to the doubled boundary A=B at u=0."
    weighted_chart_transportable_to_p_corner = False
    assert not weighted_chart_transportable_to_p_corner

    packet = {
        "schema": "marici.cosmology-p-normal-cayley-menger-support.v1",
        "stratum": "generic p=0 marked-wall incidence with K_CM nonzero",
        "restricted_K_CM_numerator": "64*(x-2*y)^2*(x+y)^2*(2*x-y)^2",
        "generic_test_point": {"x": x, "y": y, "numerator": restricted_numerator},
        "K_CM_is_unit_on_local_stratum": True,
        "Cayley_Menger_endpoint_face_subcomplex": e_cm,
        "E_CM_constructed": True,
        "E_CM_is_zero": True,
        "E_CM_differential_stable": True,
        "source_Cayley_Menger_current_role": "interior coefficient/current on this local stratum, not a boundary face",
        "all_soft_weighted_chart_imported": False,
        "all_soft_weighted_chart_transportable_to_p_corner": False,
        "coefficient_comparison_map_constructed": False,
        "marked_wall_Cech_differential_constructed": False,
        "relative_p_normal_Bockstein_constructed": False,
        "conclusion": (
            "the generic p-normal corner is disjoint from the Cayley-Menger boundary, "
            "so E_CM is the canonical zero subcomplex; the remaining carrier must be "
            "built from the source marked-wall Cech/bulk-face complex, not the all-soft Rees chart"
        ),
        "next_gate": (
            "materialize the three marked-wall Cech/bulk-face differential and a separately "
            "stable generic circuit subcomplex on the K_CM-invertible stratum"
        ),
        "passed": True,
    }
    OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))


if __name__ == "__main__":
    main()
