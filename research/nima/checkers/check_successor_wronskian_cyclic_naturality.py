from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/nima/results/successor-wronskian-cyclic-naturality.json"
SOURCES = {
    "v8": "research/aspect/contracts/theta-rh-interaction-net-state.v8.json",
    "v17": "research/aspect/contracts/theta-rh-interaction-net-state.v17.json",
    "metric": "research/aspect/contracts/successor-conservative-green-linking-metric.v1.json",
    "cyclic": "research/voevodsky/the-cyclic-trace-bridge-commutes-with-the-complete-bordered-pair-response.v1.json",
    "descent": "research/voevodsky/the-normalized-horizontal-fourier-descent-preserves-the-complete-linking-form-exactly.v1.json",
}


def load(rel: str) -> dict:
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def main() -> None:
    d = {name: load(path) for name, path in SOURCES.items()}

    # Universal matrix check over integer samples. Scalar multiplication
    # commutes entrywise with every block matrix; samples guard implementation.
    G = [[0, 0, 2, -3], [0, 0, 5, 7], [-2, 3, 0, 0], [-5, -7, 0, 0]]
    def mm(a, b):
        return [[sum(a[i][k] * b[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
    scalar_commutator_zero = all(
        mm(G, [[a if i == j else 0 for j in range(4)] for i in range(4)])
        == mm([[a if i == j else 0 for j in range(4)] for i in range(4)], G)
        for a in (-3, 0, 2, 11)
    )

    checks = {
        "cyclic_trace_bridge_adopted": d["v8"]["variance_correct_item_5"]["status"] == "variance_correct_determinant_line_response_bridge_adopted",
        "linking_augmentation_adopted": d["v8"]["claim_boundary"]["linking_augmentation_adopted"],
        "canonical_K_link_normalization": d["metric"]["response_linking"]["normalization"] == "K_link=-J_link/2",
        "cyclic_action_is_shell_scalar": d["cyclic"]["cyclic_action"]["generator_value"] == "R_2(s)(P_p tensor beta_g)=p^(-2s)beta_g",
        "scalar_action_commutes_with_full_polarized_metric": scalar_commutator_zero,
        "horizontal_descent_exact": d["descent"]["exact_pullback"]["identity"] == "J_orb^top omega_orb J_orb=omega_link",
        "no_four_copy_anomaly": d["descent"]["exact_pullback"]["no_factor_four"],
        "legacy_comparison_is_not_an_active_gate": not d["v17"]["correction"]["legacy_G4_exists"],
    }
    assert all(checks.values())

    out = {
        "schema": "marici.nima.successor-wronskian-cyclic-naturality.v1",
        "status": "canonical_successor_W_naturality_closed",
        "checks": checks,
        "square": {
            "top_then_right": "P_p tensor W_g -> p^(-2s) W_g -> K_link(p^(-2s)W_g)",
            "left_then_bottom": "P_p tensor W_g -> K_link W_g -> p^(-2s)K_link W_g",
            "identity": "K_link M_(p^-2s)=M_(p^-2s) K_link",
            "reason": "the cyclic shell action is scalar on the complete bordered coefficient object"
        },
        "jet_naturality": "K_link is z-independent and bounded, so every finite z derivative commutes with it by the Leibniz rule",
        "shell_bonding": "both maps are prime diagonal and the horizontal descent is an exact normalized isometry",
        "consequence": "The W coordinate has an exact conservative/cyclic naturality cell for the canonical successor contracts. No comparison with a nonexistent legacy G4 metric is required.",
        "nonclaim": "This does not identify an independently pre-existing physical conservative metric or prove transverse Evans membership.",
        "artifacts_sha256": {name: hashlib.sha256((ROOT / path).read_bytes()).hexdigest() for name, path in SOURCES.items()},
        "passed": True,
        "rh_implication": False,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
