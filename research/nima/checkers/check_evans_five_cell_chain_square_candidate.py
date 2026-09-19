from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CONTRACT = ROOT / "research/nima/contracts/evans-five-cell-chain-square-candidate.v1.json"
OUT = ROOT / "research/nima/results/evans-five-cell-chain-square-candidate.json"


def main() -> None:
    c = json.loads(CONTRACT.read_text(encoding="utf-8"))
    fields = {
        "common_closed_domain": c["source"]["common_closed_domain_locator"],
        "graph_norm": c["source"]["graph_norm_locator"],
        "five_cell_differential": c["target"]["five_cell_differential_matrix"],
        "K_formula": c["observer"]["K_formula"],
        "V_formula": c["observer"]["V_formula"],
        "observer_matrix": c["observer"]["matrix_on_common_basis"],
        "R_Xi_matrix": c["source_pencil"]["matrix_on_common_basis"],
        "K_continuity": c["continuity"]["tail_K"],
        "V_continuity": c["continuity"]["tail_V"],
        "assembled_bound": c["continuity"]["assembled_graph_norm_bound"],
        "tail_C4_intertwining": c["coherence"]["analytic_tail_C4_intertwining"],
        "Tate_phase": c["coherence"]["Tate_fourfold_phase"],
    }
    domain_locator = c["source"]["common_closed_domain_locator"]
    domain_path = domain_locator.split("#", 1)[0] if domain_locator else ""
    pencil_locator = c["source_pencil"].get("source_locator")
    pencil_path = pencil_locator.split("#", 1)[0] if pencil_locator else ""
    available = {
        "source_and_target_typed": bool(c["source"]["carrier"] and c["target"]["carrier"]),
        "common_domain_locator_resolves": bool(domain_path) and (ROOT / domain_path).exists(),
        "graph_norm_declared": bool(c["source"]["graph_norm_locator"]),
        "R_Xi_operator_matrix_materialized": bool(c["source_pencil"]["matrix_on_common_basis"]),
        "R_Xi_source_locator_resolves": bool(pencil_path) and (ROOT / pencil_path).exists(),
        "bulk_formula": bool(c["observer"]["bulk_formula"]),
        "endpoint_formula": bool(c["observer"]["endpoint_formula"]),
        "multiplicity_linear": c["coherence"]["xi_multiplicity_linear"],
        "prohibited_shortcuts_declared": len(c["prohibited_shortcuts"]) == 4,
    }
    assert all(available.values())
    missing = [name for name, value in fields.items() if value is None]
    first_executable = [
        "K_formula", "V_formula", "five_cell_differential", "observer_matrix"
    ]
    out = {
        "schema": "marici.nima.evans-five-cell-chain-square-candidate.result.v1",
        "status": "rosenbrock_domain_and_matrix_recovered_tail_observers_and_target_differential_open",
        "available_checks": available,
        "missing_fields": missing,
        "minimal_first_packet": first_executable,
        "recovered": {
            "common_domain": c["source"]["common_closed_domain_locator"],
            "graph_norm": c["source"]["graph_norm_locator"],
            "R_Xi_matrix": c["source_pencil"]["matrix_on_common_basis"]
        },
        "first_blocker": "No source locator gives K and V as operators on the recovered common stable-H1 Rosenbrock domain, and d_5cell is not materialized on the five-cell target.",
        "acceptance_test": "Once populated, multiply the three matrices symbolically and require B_Ev R_Xi-d_5cell B_Ev=0 coefficientwise before Xi specialization; then test graph-norm bounds and C4/Tate covariance.",
        "promotion_ready": False,
        "passed": True,
        "claim_boundary": "Pass certifies an exact non-circular input deficit and executable acceptance interface; it does not certify the chain map.",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
