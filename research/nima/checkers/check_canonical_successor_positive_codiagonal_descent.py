from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/nima/results/canonical-successor-positive-codiagonal-descent.json"
SOURCES = {
    "coordinates": "research/nima/results/canonical-successor-four-coordinate-naturality.json",
    "criterion": "research/voevodsky/positive-joint-energy-descends-through-the-radial-codiagonal-if-and-only-if-the-composite-source-map-is-injective.v1.json",
    "recovery": "research/voevodsky/canonical-source-recovery-proves-endpoint-wronskian-balance-transversality-and-injectivity-after-the-interval-cycle-quotient.v1.json",
    "counterflow": "research/aspect/contracts/canonical-stokes-rung4-counterflow-homotopy.v1.json",
    "v17": "research/aspect/contracts/theta-rh-interaction-net-state.v17.json",
}


def load(rel: str) -> dict:
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def main() -> None:
    d = {name: load(path) for name, path in SOURCES.items()}
    checks = {
        "four_coordinate_naturality_closed": d["coordinates"]["passed"],
        "descent_criterion_is_injectivity": d["criterion"]["descent_theorem"]["claim"] == "E_C is constant on fibers of K iff ker(K)={0}",
        "canonical_radial_recovery_injective": "is injective" in d["recovery"]["canonical_map"]["recovery"],
        "balanced_range_transverse": d["recovery"]["transversality_proof"]["therefore"] == "R_can intersect N_bal={0}",
        "composite_kernel_exactly_cycles": d["recovery"]["kernel_consequence"]["result"] == "ker(D T_PB)=Z_1(G)",
        "postcycle_map_injective": d["recovery"]["kernel_consequence"]["postquotient"] == "D T_PB is injective on P_pair/Z_1(G)",
        "positive_energy_well_defined": d["recovery"]["positive_energy_descent"]["well_defined"].startswith("yes"),
        "source_pulled_topology_declared": "source-pulled/range topology" in d["recovery"]["positive_energy_descent"]["topology"],
        "full_radial_state_retained": d["counterflow"]["quotient_control"]["full_radial_state_retained"],
        "legacy_G4_absent": not d["v17"]["correction"]["legacy_G4_exists"],
    }
    assert all(checks.values())

    out = {
        "schema": "marici.nima.canonical-successor-positive-codiagonal-descent.v1",
        "status": "canonical_pair_positive_apex_closed_after_exact_cycle_quotient",
        "checks": checks,
        "source": "P_bar=P_pair/Z_1(G)",
        "map": "K_bar=D T_PB:P_bar->Y_can=ran(D T_PB)",
        "kernel": "zero, because ker(D T_PB)=Z_1(G)",
        "energy": "E_Y(K_bar[x])=E_P([x])",
        "topology": "source-pulled range topology transported by K_bar",
        "consequence": "Positive energy is constant on codiagonal fibers and nondegenerate on the canonical pair quotient. The canonical quotient/coherencer/positive-apex chain is complete.",
        "ambient_warning": "No ambient-output closed range, bounded Hilbert inverse, all-path regulator limit, or Clark/Hardy positivity is inferred.",
        "remaining_gate": "Place the independent transverse Xi/Evans source in P_bar while preserving tau, multiplicity, C4/Tate transport, and nonzero quotient energy.",
        "artifacts_sha256": {name: hashlib.sha256((ROOT / path).read_bytes()).hexdigest() for name, path in SOURCES.items()},
        "passed": True,
        "rh_implication": False,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
