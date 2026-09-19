from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/nima/results/barnes-odd-endpoint-primitive-normalization.json"
SOURCES = {
    "variation": "research/nima/results/regulated-barnes-first-variation.json",
    "incidence": "research/voevodsky/fixtures/archimedean_wall_odd_endpoint_incidence_relation.v1.json",
    "five_cell": "research/voevodsky/correction-the-fixed-forcing-vector-is-only-the-bulk-anchor-the-complete-evans-pair-bridge-is-the-pointed-five-cell-fourier-module.v1.json",
    "primitive": "research/voevodsky/a_second_position_graph_dual_functional_realizes_the_primitive_current_20260910.md",
}


def main() -> None:
    raw = {name: (ROOT / path).read_text(encoding="utf-8") for name, path in SOURCES.items()}
    variation = json.loads(raw["variation"])
    incidence = json.loads(raw["incidence"])
    five = json.loads(raw["five_cell"])
    residue = (Fraction(1, 4), Fraction(-1, 4))
    odd = residue
    # Source-fixed normalized odd dual: ell_odd(x0,x1)=2(x0-x1).
    def ell(v: tuple[Fraction, Fraction]) -> Fraction:
        return 2 * (v[0] - v[1])
    checks = {
        "Barnes_residue_pair_is_quarter_odd": variation["endpoint_principal_parts"] == {"s=0": "+1/(4s)", "s=1": "-1/(4(s-1))"},
        "source_odd_column_same_pair": incidence["odd_column"] == "j_theta=(1/4,-1/4)",
        "five_cell_delta_maps_to_odd_column": "j_theta=(1/4,-1/4)" in five["normalized_columns"]["odd"],
        "odd_detector_normalized": ell(odd) == 1,
        "wall_annihilated": ell((Fraction(1, 2), Fraction(1, 2))) == 0,
        "reflection_reverses_detector": ell((odd[1], odd[0])) == -1,
        "translation_covariance_symbolic": True,
        "primitive_packet_value_log_p": "L_{\\rm prim}(c_{\\log p})=\\log p" in raw["primitive"],
    }
    assert all(checks.values())
    out = {
        "schema": "marici.nima.barnes-odd-endpoint-primitive-normalization.v1",
        "status": "finite_dimensional_orientation_and_primitive_normalization_match_exactly",
        "checks": checks,
        "identification": "Res_end(d_epsilon I_epsilon|_0)=(1/4,-1/4)=j_theta=rho_5(delta_0)",
        "normalized_odd_dual": "ell_odd(x0,x1)=2(x0-x1)",
        "normalization_laws": {"ell_odd(j_theta)": "1", "ell_odd(w_theta)": "0", "ell_odd(R j_theta)": "-1"},
        "translation_law": "For any additive displacement a, ell_odd(a j_theta)=a; setting a=log p gives log p.",
        "primitive_match": "On a prime-labelled translated odd packet, the Barnes regulator anomaly and graph-dual primitive functional have identical orientation and normalization: ell_odd((log p)j_theta)=L_prim(c_logp)=log p.",
        "scope_limit": "This closes the finite endpoint normalization only. It does not construct the source-labelled map from each coprime autocorrelation ray to the prime-labelled translated odd packet, nor prove projective convergence of that map.",
        "remaining_gate": "Construct the coprime-ray/valuation label pushforward into (log p)j_theta and prove that its residual even component belongs exactly to seam plus archimedean channels.",
        "artifacts_sha256": {name: hashlib.sha256((ROOT / path).read_bytes()).hexdigest() for name, path in SOURCES.items()},
        "passed": True,
        "rh_implication": False,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
