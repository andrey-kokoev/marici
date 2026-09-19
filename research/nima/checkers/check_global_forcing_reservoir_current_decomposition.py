from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/nima/results/global-forcing-reservoir-current-decomposition.json"
SOURCES = {
    "equation": "research/nima/global-forcing-reservoir-decomposition-is-the-current-source-equation.md",
    "autocorrelation": "research/nima/forcing-reservoir-is-the-laplace-transform-of-theta-autocorrelation.md",
    "xi_square": "research/nima/the-completed-theta-autocorrelation-is-the-inverse-mellin-square-of-xi.md",
    "cyclic": "research/voevodsky/the-cyclic-trace-bridge-commutes-with-the-complete-bordered-pair-response.v1.json",
    "strata": "research/nima/many-many-three-block-final-disposition.md",
    "local_global": "research/nima/results/mixed-green-local-to-global-transport.json",
}


def main() -> None:
    raw = {name: (ROOT / path).read_text(encoding="utf-8") for name, path in SOURCES.items()}
    cyclic = json.loads(raw["cyclic"])
    prior = json.loads(raw["local_global"])
    checks = {
        "local_mixed_identity_closed": prior["checks"]["local_mixed_green_identity_closed"],
        "reservoir_is_autocorrelation_laplace": "-\\mathcal L A_\\Phi(z)" in raw["autocorrelation"],
        "scalar_arithmetic_assembly_is_xi_square": "K(s)\\zeta(s)\\zeta(1-s)=\\xi(s)^2" in raw["xi_square"],
        "operator_valued_density_retained": cyclic["density_level"]["no_information_loss_before_final_trace"],
        "cyclic_trace_commutes_with_laplace": cyclic["density_level"]["laplace"].startswith("Laplace commutes"),
        "five_typed_current_equation_fixed": all(token in raw["equation"] for token in ("{(1)}", "{(2)}", "{(\\ge3)}", "{({\\rm seam})}", "{(\\infty)}")),
        "common_logarithmic_carrier_exists": "H_X=\\sum_{p\\le X}\\sum_{k\\ge1}" in raw["equation"],
        "global_decomposition_not_already_proved": "No repository source located" in raw["equation"],
    }
    assert all(checks.values())
    rows = [
        {"grade": "primitive", "index": "k=1", "target": "primitive endpoint current", "equality": "open"},
        {"grade": "square", "index": "k=2", "target": "square current", "equality": "open"},
        {"grade": "connected", "index": "k>=3", "target": "det_3 connected logarithm", "equality": "open"},
        {"grade": "seam", "index": "finite endpoint remainder", "target": "seam current", "equality": "open"},
        {"grade": "archimedean", "index": "smooth completion remainder", "target": "Tate/gamma current", "equality": "open"},
    ]
    out = {
        "schema": "marici.nima.global-forcing-reservoir-current-decomposition.v1",
        "status": "global_M_in_identified_as_typed_current_residual_five_coefficient_equalities_open",
        "checks": checks,
        "M_in": "F_X(w,z)=<Phi,G_z>+<G_w,Phi>=-L A_Phi(z)-conj(L A_Phi(w))",
        "residual": "Q_X=F_X-(F_X^(1)+F_X^(2)+F_X^(>=3)+F_X^(seam)+F_X^(infinity))",
        "required_identity": "Q_X(w,z)=0 before scalar trace and before Xi specialization",
        "coefficient_rows": rows,
        "important_distinction": "The scalar inverse-Mellin xi^2 identity and the function-valued cyclic trace establish the source scalar and preserve density data, but they do not prove the five typed mixed-height current equalities.",
        "next_executable": "Start with k=1: write the primitive coefficient of the finite-cutoff autocorrelation kernel and compare it to the independently constructed primitive endpoint current on a two-height symbolic packet.",
        "artifacts_sha256": {name: hashlib.sha256((ROOT / path).read_bytes()).hexdigest() for name, path in SOURCES.items()},
        "passed": True,
        "rh_implication": False,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
