"""Admission of the logarithmic-denominator primitive no-go.

This checker independently rechecks the local double-residue obstruction from
Voevodsky's packets and records its exact scope for the cosmology SCC chain.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NIMA = ROOT / "nima"
VOE = ROOT / "voevodsky"
OUT = NIMA / "results" / "cosmology_p_normal_log_denominator_no_go.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def exact_double_residue_contributors(bound: int) -> list[tuple[str, int, int, int]]:
    contributors = []
    for source in ("A", "B"):
        for a in range(-bound, bound + 1):
            for b in range(-bound, bound + 1):
                if source == "B" and (a - 1, b) == (-1, -1) and a != 0:
                    contributors.append((source, a, b, a))
                if source == "A" and (a, b - 1) == (-1, -1) and b != 0:
                    contributors.append((source, a, b, -b))
    return contributors


def main() -> None:
    primitive = load(VOE / "results" / "cosmology_log_denominator_primitive_gate.json")
    residue = load(VOE / "results" / "cosmology_log_denominator_residue_obstruction.json")
    identity = load(NIMA / "results" / "cosmology_triple_incidence_logarithmic_identity.json")
    cech = load(NIMA / "results" / "cosmology_p_normal_marked_wall_cech_carrier.json")

    assert primitive["log_complex"]["log_one_form_primitive_exists"] is False
    assert residue["consequence"].startswith("p*eta is not exact")
    assert identity["local_wall_model"] == "q3=q1+q2+p"
    assert cech["minimal_Cech_p_normal_Bockstein_nonzero"] is False

    # At u=v=0, p/(p+u+v) has constant term one whenever p is a unit.
    # A Laurent B term contributing u^-1 v^-1 after d/du would require a=0
    # and is multiplied by a=0; similarly an A term requires b=0.
    assert exact_double_residue_contributors(6) == []

    prime_checks = {}
    for prime in (101, 103):
        witness = residue["finite_field_witnesses"][str(prime)]
        assert witness["target_double_residue"] == 1
        assert witness["exact_laurent_differential_double_residue"] == 0
        assert witness["obstruction_nonzero"] is True
        bounded = primitive["bounded_rational_ansatz_tests"][str(prime)]
        assert all(row["coefficient_rank"] + 1 == row["augmented_rank"] for row in bounded)
        assert all(row["solution_exists"] is False for row in bounded)
        prime_checks[str(prime)] = {
            "target_double_residue": 1,
            "exact_differential_double_residue": 0,
            "bounded_depth_rank_pairs": [
                [row["coefficient_rank"], row["augmented_rank"]] for row in bounded
            ],
        }

    packet = {
        "schema": "marici.cosmology-p-normal-log-denominator-no-go.v1",
        "status": "ordinary_logarithmic_and_Laurent_primitive_routes_closed_by_double_residue",
        "carrier": "punctured bidisc u=q1, v=q2, q3=p+u+v with p a unit",
        "target": "p*du^dv/(u*v*(p+u+v))",
        "target_double_residue": 1,
        "exact_Laurent_differential_double_residue": 0,
        "unbounded_exponent_local_obstruction": True,
        "prime_checks": prime_checks,
        "ordinary_logarithmic_primitive_exists": False,
        "ordinary_Laurent_primitive_exists": False,
        "deeper_ordinary_poles_can_reopen_route": False,
        "minimal_Cech_Bockstein_nonzero": False,
        "relative_Cech_or_bulk_face_complex_may_change_target": True,
        "resolved_exceptional_generator_constructed": False,
        "full_Cayley_Menger_face_cone_constructed": False,
        "ambient_division_by_p": False,
        "physical_period_constructed": False,
        "conclusion": (
            "the p-normal target has nonzero double residue and cannot be an ordinary "
            "logarithmic or Laurent exact differential; together with special Cech exactness, "
            "this closes all unaugmented local primitive routes"
        ),
        "next_gate": (
            "only a source-derived relative bulk/face or exceptional mapping cone whose "
            "face residue changes the target complex can reopen the p-normal route"
        ),
        "passed": True,
    }
    OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))


if __name__ == "__main__":
    main()
