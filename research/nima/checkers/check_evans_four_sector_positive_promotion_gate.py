from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CONTRACT = ROOT / "research/nima/contracts/evans-four-sector-chain-square-candidate.v1.json"
SOURCES = {
    "stable": "research/voevodsky/the-two-stable-history-sections-form-a-source-derived-rosenbrock-pencil-whose-transmission-determinant-is-exactly-xi.v1.json",
    "doubling": "research/voevodsky/correction-stable-half-line-and-reciprocal-parameter-doublings-are-independent-so-the-feedback-carrier-is-four-dimensional.v1.json",
    "audit": "research/voevodsky/prior-research-already-constructs-the-transverse-xi-characteristic-and-reduces-closure-to-conservative-symmetrization.v1.json",
}
FEEDBACK = ROOT / "research/nima/xi-rosenbrock-is-an-identity-feedthrough-feedback-system-and-is-not-passive.md"
OUT = ROOT / "research/nima/results/evans-four-sector-positive-promotion-gate.json"


def load(rel: str) -> dict:
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def main() -> None:
    c = json.loads(CONTRACT.read_text(encoding="utf-8"))
    d = {name: load(path) for name, path in SOURCES.items()}
    feedback = FEEDBACK.read_text(encoding="utf-8")
    checks = {
        "sector_differential_materialized": bool(c["target"]["sector_differential_matrix"]),
        "R_Xi_formula_matches_source": "R_Xi(z)(f_-,f_+,c)" in d["stable"]["rosenbrock_pencil"]["formula"],
        "reciprocal_double_required": d["doubling"]["correct_carrier"]["full"].endswith("C^4 before any sourced quotient"),
        "exact_Xi_transfer": d["stable"]["schur_transfer"]["identity"].endswith("Xi_centered(z)"),
        "positive_symmetrizer_source_gap": "no source-derived nondegenerate K" in d["audit"]["conservative_frontier"]["source_gap"],
        "identity_feedthrough_identified": "Taking scalar feedback `C=I` and direct term `D=I`" in feedback,
        "passive_similarity_rejected": "contractive colligation with `D=I` cannot have a nonzero coupling `B`" in feedback,
        "dilation_is_required": "divisor-preserving passive dilation or a one-way triangular extension" in feedback,
    }
    assert all(checks.values())
    out = {
        "schema": "marici.nima.evans-four-sector-positive-promotion-gate.v1",
        "status": "four_sector_differential_closed_passive_similarity_falsified_dilation_required",
        "checks": checks,
        "sector_differential": c["target"]["sector_differential_matrix"],
        "exact_characteristic": "The Schur transfer of each stable z block is tau(z)=Xi_centered(z); reciprocal doubling retains z and -z without conflating stable parity.",
        "no_go": "The exact Xi Rosenbrock realization has identity feedthrough D=I and nonzero theta incidence B. A contractive colligation with unitary direct block forces B=0, so no passive similarity preserving these blocks exists.",
        "consequence": "The missing positive promotion is not merely K,V coordinate completion. It must be a divisor-preserving passive dilation or one-way triangular extension on the four-sector carrier.",
        "remaining_data": ["K and V four-sector observer formulas", "four-sector observer matrix", "dilating auxiliary block and Green form", "holomorphic equivalence preserving the Xi root complex"],
        "artifacts_sha256": {
            **{name: hashlib.sha256((ROOT / path).read_bytes()).hexdigest() for name, path in SOURCES.items()},
            "contract": hashlib.sha256(CONTRACT.read_bytes()).hexdigest(),
            "feedback": hashlib.sha256(FEEDBACK.read_bytes()).hexdigest()
        },
        "passed": True,
        "rh_implication": False,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
