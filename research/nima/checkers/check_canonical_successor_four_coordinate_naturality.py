from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/nima/results/canonical-successor-four-coordinate-naturality.json"
SOURCES = {
    "old_frontier": "research/nima/results/conservative-cyclic-trace-coordinate-frontier.json",
    "endpoint": "research/nima/results/successor-endpoint-cyclic-naturality.json",
    "wronskian": "research/nima/results/successor-wronskian-cyclic-naturality.json",
    "crossing": "research/voevodsky/the-cyclic-trace-bridge-commutes-with-the-complete-bordered-pair-response.v1.json",
    "border": "research/aspect/contracts/g4-radial-to-bordered-target.v1.json",
    "v17": "research/aspect/contracts/theta-rh-interaction-net-state.v17.json",
}


def load(rel: str) -> dict:
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def main() -> None:
    d = {name: load(path) for name, path in SOURCES.items()}
    old_rows = {row["name"].split()[0]: row for row in d["old_frontier"]["coordinates"]}
    checks = {
        "rho0_independent_naturality_closed": old_rows["rho0"]["independent_conservative_trace_identification"],
        "E_naturality_closed": d["endpoint"]["passed"] and d["endpoint"]["status"] == "canonical_successor_E_naturality_closed",
        "W_naturality_closed": d["wronskian"]["passed"] and d["wronskian"]["status"] == "canonical_successor_W_naturality_closed",
        "cyclic_action_covers_R": "R_g" in d["crossing"]["pair_response"]["generator_packet"],
        "stokes_relation_fixed": d["border"]["border_operator"]["stokes_relation"] == "zR-rho0=E-W/2",
        "z0_continuation_removable": "removable holomorphic continuation" in d["border"]["border_operator"]["z0_rule"],
        "all_jet_action_declared": d["border"]["border_operator"]["all_jet_action"] == "differentiate the holomorphic continuation parameterwise",
        "cyclic_scalar_commutes_with_all_coordinates": d["crossing"]["cyclic_action"]["border_compatibility"].startswith("the scalar p^(-2s) commutes with rho0,E,W,R"),
        "canonical_G4_only": not d["v17"]["correction"]["legacy_G4_exists"],
    }
    assert all(checks.values())

    coordinates = {
        "rho0": {"status": "closed", "basis": "independent ordinary normalization"},
        "E": {"status": "closed", "basis": "I_end=-2E and scalar cyclic shell action"},
        "W": {"status": "closed", "basis": "K_link M_(p^-2s)=M_(p^-2s)K_link"},
        "R": {"status": "closed", "basis": "z delta_R=delta_rho0+delta_E-delta_W/2=0 off z=0; removable holomorphic continuation closes z=0"},
    }
    out = {
        "schema": "marici.nima.canonical-successor-four-coordinate-naturality.v1",
        "status": "all_four_canonical_successor_bordered_coordinate_cells_closed",
        "supersedes": "research/nima/results/conservative-cyclic-trace-coordinate-frontier.json at canonical-successor strength",
        "checks": checks,
        "coordinates": coordinates,
        "R_argument": "For the difference of the two canonical successor routes, Stokes gives z*delta_R=delta_rho0+delta_E-delta_W/2. The three right-hand differences vanish. Hence delta_R=0 for z!=0, and holomorphic removability gives delta_R(0)=0 and equality of every finite jet.",
        "consequence": "The canonical successor cyclic/conservative comparison is entrywise natural on (rho0,E,W,R), shellwise, after completion, and under every finite parameter derivative.",
        "nonclaim": "This is not an equality with a separately pre-existing legacy conservative complex and does not place the transverse Xi Evans state.",
        "artifacts_sha256": {name: hashlib.sha256((ROOT / path).read_bytes()).hexdigest() for name, path in SOURCES.items()},
        "passed": True,
        "rh_implication": False,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
