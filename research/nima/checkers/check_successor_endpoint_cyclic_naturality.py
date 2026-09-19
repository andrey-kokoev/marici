from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/nima/results/successor-endpoint-cyclic-naturality.json"
SOURCES = {
    "cyclic": "research/voevodsky/the-cyclic-trace-bridge-commutes-with-the-complete-bordered-pair-response.v1.json",
    "endpoint": "research/voevodsky/the-ordinary-and-derivative-wall-prime-shell-residuals-form-an-explicit-holomorphic-two-term-block.v1.json",
    "stokes": "research/nima/the-radial-stokes-identity-fixes-the-exact-combined-diagonal-reciprocal-linking-section.md",
    "split": "research/aspect/contracts/regular-derivative-wall-port-split.v1.json",
    "v17": "research/aspect/contracts/theta-rh-interaction-net-state.v17.json",
}


def load_json(rel: str) -> dict:
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def main() -> None:
    cyclic = load_json(SOURCES["cyclic"])
    endpoint = load_json(SOURCES["endpoint"])
    split = load_json(SOURCES["split"])
    v17 = load_json(SOURCES["v17"])
    stokes_text = (ROOT / SOURCES["stokes"]).read_text(encoding="utf-8")

    checks = {
        "cyclic_E_formula_exists": "E_g" in cyclic["pair_response"]["generator_packet"],
        "cyclic_shell_action_is_scalar": cyclic["cyclic_action"]["generator_value"] == "R_2(s)(P_p tensor beta_g)=p^(-2s)beta_g",
        "endpoint_block_is_explicit_and_holomorphic": endpoint["analytic_transpose_lane"]["derivative_plus_wall"] == "I_end(z)=Phi(b)u_z(b)-Phi(a)u_z(a)",
        "regular_and_wall_ports_share_source": "transported together" in endpoint["distributional_origin"]["consequence"],
        "endpoint_shell_concatenation": split["shell_difference"]["shell_concatenation"],
        "all_parameter_jets_continuous": split["continuity"]["all_Evans_parameter_jets"],
        "source_identity_Iend_equals_minus_2E": "= -2E(z)." in stokes_text or "=-2E(z)" in stokes_text,
        "canonical_G4_is_TPB": v17["admitted_G4"]["forward_realization"] == "T_PB=T_pair_to_border",
        "legacy_comparison_inactive": not v17["correction"]["legacy_G4_exists"],
    }
    assert all(checks.values())

    out = {
        "schema": "marici.nima.successor-endpoint-cyclic-naturality.v1",
        "status": "canonical_successor_E_naturality_closed",
        "checks": checks,
        "endpoint_identification": "I_end(z)=Phi(b)u_z(b)-Phi(a)u_z(a)=-2E(z)",
        "square": {
            "top_then_right": "P_p tensor E_g -> p^(-2s)E_g -> -2 p^(-2s)E_g",
            "left_then_bottom": "P_p tensor E_g -> -2E_g -> p^(-2s)(-2E_g)",
            "identity": "(-2) M_(p^-2s) E_g = M_(p^-2s) (-2 E_g)",
        },
        "jet_naturality": "The source endpoint identity is holomorphic; endpoint trace commutes with every finite z derivative on the Evans graph.",
        "shell_bonding": "The regular-derivative and wall atoms are retained together and their oriented endpoint differences concatenate exactly.",
        "correction": "The open comparison in regular-derivative-wall-port-split.v1 concerns mismatched raw cut-atom versus moving-seam conventions. The later aligned radial-Stokes source identity fixes the canonical successor comparison as I_end=-2E.",
        "consequence": "The E coordinate has an exact conservative/cyclic naturality cell for the canonical successor contracts.",
        "nonclaim": "This does not identify a nonexistent legacy conservative metric or prove transverse Evans membership.",
        "artifacts_sha256": {name: hashlib.sha256((ROOT / path).read_bytes()).hexdigest() for name, path in SOURCES.items()},
        "passed": True,
        "rh_implication": False,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
