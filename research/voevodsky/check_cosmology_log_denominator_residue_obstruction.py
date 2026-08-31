"""Residue obstruction for the logarithmic denominator primitive gate.

This repeat iteration replaces the previous bounded rational no-go by a local
punctured-bidisc residue obstruction.  At the normal crossing q1=q2=0 with p a
unit, exact Laurent one-form differentials have zero double residue, while
p*dq1^dq2/(q1*q2*q3) has double residue one.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VOEVODSKY_RESULTS = ROOT / "research" / "voevodsky" / "results"
NIMA_RESULTS = ROOT / "research" / "nima" / "results"
OUT = VOEVODSKY_RESULTS / "cosmology_log_denominator_residue_obstruction.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def target_double_residue_mod(prime: int) -> int:
    # Generic normal chart p=1: q3=1+u+v is a unit at u=v=0.
    # p/q3 = 1/(1+u+v) has constant coefficient one in the completed local ring.
    return 1 % prime


def derivative_double_residue_from_laurent_support(bound: int, prime: int) -> dict:
    # A Laurent one-form A du + B dv has differential
    # (partial_u B - partial_v A) du^dv.  A monomial c*u^a*v^b in B contributes
    # c*a*u^(a-1)*v^b; to hit u^-1*v^-1 one needs a=0,b=-1, but then a=0.
    # A monomial in A contributes -c*b*u^a*v^(b-1); to hit u^-1*v^-1 one
    # needs a=-1,b=0, but then b=0.  Hence every basis coefficient maps to
    # zero double residue.
    checked = 0
    nonzero_contributors: list[dict[str, int | str]] = []
    for source in ("A", "B"):
        for a in range(-bound, bound + 1):
            for b in range(-bound, bound + 1):
                checked += 1
                if source == "B":
                    contributes = (a if (a - 1, b) == (-1, -1) else 0) % prime
                else:
                    contributes = (-b if (a, b - 1) == (-1, -1) else 0) % prime
                if contributes:
                    nonzero_contributors.append({"source": source, "u_power": a, "v_power": b, "coefficient": contributes})
    return {
        "support_bound": bound,
        "prime": prime,
        "basis_monomials_checked": checked,
        "exact_differential_double_residue_rank": 0,
        "nonzero_contributors": nonzero_contributors,
    }


def main() -> None:
    denominator_gate = load(VOEVODSKY_RESULTS / "cosmology_log_denominator_primitive_gate.json")
    log_identity = load(NIMA_RESULTS / "cosmology_triple_incidence_logarithmic_identity.json")
    boundary = load(NIMA_RESULTS / "cosmology_triple_incidence_boundary_corner_transport.json")

    assert denominator_gate["passed"] is True
    assert denominator_gate["status"] == "finite_denominator_gate_no_go_for_log_and_bounded_rational_primitives"
    assert log_identity["local_wall_model"] == "q3=q1+q2+p"
    assert boundary["local_coordinates"] == {"u": "q1", "v": "q2", "q3": "u+v+p"}

    witnesses = {}
    for prime in (101, 103):
        target_residue = target_double_residue_mod(prime)
        exact_residue = derivative_double_residue_from_laurent_support(bound=4, prime=prime)
        assert target_residue == 1
        assert exact_residue["nonzero_contributors"] == []
        witnesses[str(prime)] = {
            "target_double_residue": target_residue,
            "exact_laurent_differential_double_residue": 0,
            "support_check": exact_residue,
            "obstruction_nonzero": True,
        }

    result = {
        "schema": "marici.voevodsky.cosmology-log-denominator-residue-obstruction.v1",
        "status": "unbounded_local_residue_obstruction_to_denominator_primitive",
        "rechecked_inputs": [
            "research/voevodsky/results/cosmology_log_denominator_primitive_gate.json",
            "research/nima/results/cosmology_triple_incidence_logarithmic_identity.json",
            "research/nima/results/cosmology_triple_incidence_boundary_corner_transport.json",
        ],
        "local_chart": "u=q1, v=q2, q3=p+u+v with p a unit; finite-field witness sets p=1",
        "target_form": "p*du^dv/(u*v*(p+u+v))",
        "target_double_residue": "constant term of p/(p+u+v), equal to 1",
        "exactness_test": "the double residue of d(A du+B dv) is zero for every finite Laurent polynomial A,B; the same holds termwise in the completed local Laurent module",
        "finite_field_witnesses": witnesses,
        "consequence": "p*eta is not exact in the punctured-bidisc logarithmic denominator carrier, independently of the previous bounded rational ansatz",
        "ambient_division_by_p": False,
        "tautological_circuit_quotient_used": False,
        "physical_period_constructed": False,
        "remaining_possible_enlargements": [
            "relative Cech boundary map that changes the residue target",
            "resolved/Rees exceptional generator whose differential is not an ordinary punctured-bidisc de Rham differential",
            "full Cayley-Menger face mapping cone with a compensating face residue",
        ],
        "passed": True,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
