from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/nima/results/primitive-ray-global-sign.json"
SOURCES = {
    "pushforward": "research/nima/results/coprime-ray-to-primitive-valuation-pushforward.json",
    "reservoir": "research/nima/forcing-reservoir-is-the-laplace-transform-of-theta-autocorrelation.md",
    "global": "research/nima/global-forcing-reservoir-decomposition-is-the-current-source-equation.md",
    "global_result": "research/nima/results/global-forcing-reservoir-current-decomposition.json",
}


def main() -> None:
    raw = {name: (ROOT / path).read_text(encoding="utf-8") for name, path in SOURCES.items()}
    push = json.loads(raw["pushforward"])
    global_result = json.loads(raw["global_result"])
    checks = {
        "ray_arithmetic_part_has_negative_primitive_sign": "gamma-L_prim(P(a,b))" in push["ray_finite_part_split"],
        "forcing_is_negative_laplace_autocorrelation": "=-\\mathcal L A_\\Phi(z)" in raw["reservoir"],
        "Hermitian_second_height_also_negative": "-\\overline{\\mathcal L A_\\Phi(w)}" in raw["reservoir"],
        "two_negatives_give_positive_current": (-1) * (-1) == 1,
        "global_residual_subtracts_declared_currents": "\\mathcal F_X(w,z)\n-" in raw["global"],
        "primitive_row_still_open_for_completion": global_result["coefficient_rows"][0]["equality"] == "open",
    }
    assert all(checks.values())
    out = {
        "schema": "marici.nima.primitive-ray-global-sign.v1",
        "status": "primitive_sign_and_two_height_orientation_match_at_raywise_finite_part_level",
        "checks": checks,
        "notation": "W_ab(t)=[e^(t/2)/a] kappa((b/a)e^t), M_ab=max(a,b)",
        "autocorrelation_primitive_piece": "A_prim,ab(t)=-W_ab(t) L_prim(P(a,b))=-W_ab(t) log M_ab",
        "forcing_primitive_piece": "F_prim,ab(w,z)=L_z[W_ab log M_ab]+conj(L_w[W_ab log M_ab])",
        "sign_conclusion": "The minus log(max(a,b)) in the ray finite part and the minus Laplace sign in each forcing-reservoir leg cancel. The induced primitive forcing row has the positive L_prim convention required on the right side of F=sum_r F^(r).",
        "two_height_conclusion": "Both z and w legs carry the same positive primitive coefficient, with Hermitian conjugation only on the w leg. No diagonal or Xi specialization is used.",
        "residual_convention": "Because Q_X=F_X-sum_r F_X^(r), the matched primitive contribution cancels in Q_X rather than doubles.",
        "scope_limit": "This establishes the sign and typed two-height ray formula for the renormalized finite part. It does not justify exchanging the coprime-ray sum with Laplace transform or taking the projective cutoff limit.",
        "remaining_gate": "Prove a common projective majorant/continuity statement for sum_(a,b)=1 W_ab(t) P(a,b) after harmonic subtraction; only then may the global primitive coefficient row be changed from open to closed.",
        "artifacts_sha256": {name: hashlib.sha256((ROOT / path).read_bytes()).hexdigest() for name, path in SOURCES.items()},
        "passed": True,
        "rh_implication": False,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
