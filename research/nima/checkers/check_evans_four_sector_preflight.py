from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CONTRACT = ROOT / "research/nima/contracts/evans-four-sector-chain-square-candidate.v1.json"
CORRECTION = ROOT / "research/voevodsky/correction-the-evans-observer-target-must-retain-the-independent-stable-and-reciprocal-binary-factors.v1.json"
OUT = ROOT / "research/nima/results/evans-four-sector-preflight.json"


def kron(a, b):
    return [[a[i // len(b)][j // len(b[0])] * b[i % len(b)][j % len(b[0])]
             for j in range(len(a[0]) * len(b[0]))]
            for i in range(len(a) * len(b))]


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def mv(a, v):
    return [sum(x*y for x, y in zip(row, v)) for row in a]


def main() -> None:
    c = json.loads(CONTRACT.read_text(encoding="utf-8"))
    source = json.loads(CORRECTION.read_text(encoding="utf-8"))
    I = [[1, 0], [0, 1]]
    X = [[0, 1], [1, 0]]
    Rst, Rrec = kron(X, I), kron(I, X)
    forcing = c["distinguished_vectors"]["combined_forcing"]
    mismatch = c["distinguished_vectors"]["combined_mismatch"]
    checks = {
        "correction_requires_four_sectors": source["status"] == "five_cell_only_target_under_typed_four_sector_obstruction",
        "basis_exact": c["source"]["basis"] == source["minimum_matrix_test"]["basis"],
        "stable_and_reciprocal_involutions_commute": mm(Rst, Rrec) == mm(Rrec, Rst),
        "stable_even_forcing": mv(Rst, forcing) == forcing,
        "reciprocal_odd_forcing": mv(Rrec, forcing) == [-x for x in forcing],
        "stable_odd_mismatch": mv(Rst, mismatch) == [-x for x in mismatch],
        "reciprocal_odd_mismatch": mv(Rrec, mismatch) == [-x for x in mismatch],
        "forcing_and_mismatch_distinct": forcing != mismatch,
        "five_cell_candidate_marked_as_corrected": c["corrects"].endswith("evans-five-cell-chain-square-candidate.v1.json"),
    }
    assert all(checks.values())
    missing = [name for name, value in c["target"].items() if value is None]
    out = {
        "schema": "marici.nima.evans-four-sector-preflight.result.v1",
        "status": "four_sector_type_and_parity_closed_operator_chain_data_open",
        "checks": checks,
        "R_st": Rst,
        "R_rec": Rrec,
        "combined_forcing": forcing,
        "combined_mismatch": mismatch,
        "missing_target_data": missing,
        "correction": "The five-cell-only chain-square contract is under-typed. K and V must be materialized on the reciprocal doubling of the stable-history pencil, not on a conflated endpoint plane.",
        "next_executable": "Construct the sector differential and K,V observers as 4-sector block maps; then test both commuting naturality squares separately before Green polarization.",
        "artifacts_sha256": {
            "contract": hashlib.sha256(CONTRACT.read_bytes()).hexdigest(),
            "correction": hashlib.sha256(CORRECTION.read_bytes()).hexdigest()
        },
        "passed": True,
        "rh_implication": False,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
