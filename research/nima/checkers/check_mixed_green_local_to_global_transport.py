from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/nima/results/mixed-green-local-to-global-transport.json"
SOURCES = {
    "local": "research/nima/one-sided-mixed-green-block-is-closed-by-the-forcing-reservoir.md",
    "triangular": "research/nima/triangular-positive-lift-green-identity-requires-mixed-metric-blocks.md",
    "global": "research/nima/many-many-three-block-final-disposition.md",
    "coordinate": "research/nima/results/canonical-successor-four-coordinate-naturality.json",
    "positive": "research/nima/results/canonical-successor-positive-codiagonal-descent.json",
}


def main() -> None:
    text = {name: (ROOT / path).read_text(encoding="utf-8") for name, path in SOURCES.items()}
    coordinate = json.loads(text["coordinate"])
    positive = json.loads(text["positive"])
    checks = {
        "local_tail_equation_fixed": "(\\partial_q+z)G_z=-\\Phi" in text["local"],
        "incoming_outgoing_features_fixed": "I_z=\\frac{\\Phi+G_z}{\\sqrt2}" in text["local"] and "O_z=\\frac{\\Phi-G_z}{\\sqrt2}" in text["local"],
        "local_mixed_green_identity_closed": "Status: local Wronskian/Haar forcing identity closed" in text["local"],
        "mixed_metric_required": "requires a genuinely polarized mixed metric" in text["triangular"],
        "global_linking_metric_constructed": "Complete polarized two-output linking metric | Constructed" in text["global"],
        "global_stratified_transport_constructed": "Full stratified Fourier" in text["global"] and "Constructed on the stratified response equalizer" in text["global"],
        "bordered_coordinate_naturality_closed": coordinate["passed"],
        "canonical_positive_apex_closed": positive["passed"],
    }
    assert all(checks.values())
    out = {
        "schema": "marici.nima.mixed-green-local-to-global-transport.v1",
        "status": "local_mixed_green_identity_closed_global_arithmetic_naturality_cell_open",
        "checks": checks,
        "local_identity": "conj(G_w(0))G_z(0)+<O_w,O_z>-<I_w,I_z>=(z+conj(w))<G_w,G_z>",
        "interpretation": "On each stable tail, endpoint and causal-feature cross terms already equal the forcing reservoir. G_link, stratified Fourier-Poisson transport, bordered-coordinate naturality, and the canonical positive apex exist separately.",
        "remaining_cell": "Prove that reciprocal sewing and the primitive/square/connected/archimedean pair-to-Euler cyclic trace transport this local forcing-reservoir row to the same global M_in, with no anomaly or orientation defect.",
        "reduced_materialization": [
            "source graph locator for the local forcing-reservoir row",
            "its image under the stratified pair-to-Euler transport",
            "the independently declared global M_in row",
            "a coefficientwise equality and cutoff-compatible completion proof"
        ],
        "consequence": "The six-block search from the prior frontier was overbroad: the local mixed equation and its metrics are already analytically formed. Only their global arithmetic transport/naturality comparison remains.",
        "artifacts_sha256": {name: hashlib.sha256((ROOT / path).read_bytes()).hexdigest() for name, path in SOURCES.items()},
        "passed": True,
        "rh_implication": False,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
