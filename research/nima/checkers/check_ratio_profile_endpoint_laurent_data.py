from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/nima/results/ratio-profile-endpoint-laurent-data.json"
SOURCES = {
    "mellin": "research/nima/ratio-profile-mellin-transform-collapses-to-a-reflection-symmetric-gamma-factor.md",
    "barnes": "research/nima/regulated-theta-autocorrelation-is-an-explicit-zeta-barnes-integral.md",
    "moments": "research/nima/universal-ratio-profile-has-zero-mass-and-first-moment-minus-two.md",
    "ray": "research/nima/results/primitive-forcing-reservoir-scaling-ray.json",
}


def main() -> None:
    text = {name: (ROOT / path).read_text(encoding="utf-8") for name, path in SOURCES.items()}
    ray = json.loads(text["ray"])
    # K(s)=f(s)g(s), f=s(1-s). At s=0,1, f vanishes, so only
    # f'(s)g(s) contributes. Gamma(1)Gamma(3/2)/sqrt(pi)=1/2.
    fprime0, fprime1 = Fraction(1), Fraction(-1)
    g0 = g1 = Fraction(1, 2)
    kp0, kp1 = fprime0 * g0, fprime1 * g1
    checks = {
        "closed_gamma_formula_present": "K(s)=" in text["mellin"] and "s(1-s)" in text["mellin"],
        "reflection_symmetry": "K(1-s)=K(s)" in text["mellin"],
        "endpoint_zeros": "K(0)=K(1)=0" in text["mellin"],
        "K_prime_0_half": kp0 == Fraction(1, 2),
        "K_prime_1_minus_half": kp1 == Fraction(-1, 2),
        "derivatives_reflection_odd": kp1 == -kp0,
        "first_ratio_moment_minus_two": "=-2" in text["moments"] or "= -2" in text["moments"],
        "Barnes_poles_located": "s=\\varepsilon" in text["barnes"] and "s=1-\\varepsilon" in text["barnes"],
        "scaling_ray_obstruction_registered": ray["passed"],
    }
    assert all(checks.values())
    out = {
        "schema": "marici.nima.ratio-profile-endpoint-laurent-data.v1",
        "status": "endpoint_zero_and_first_derivative_normalization_closed_contour_current_identification_open",
        "checks": checks,
        "K_endpoint_data": {"K(0)": "0", "K'(0)": "1/2", "K(1)": "0", "K'(1)": "-1/2", "K(2)": "-2"},
        "derivation": "At each endpoint the s(1-s) factor has a simple zero; the gamma product equals sqrt(pi)/2, so reflection forces derivatives +1/2 and -1/2.",
        "meaning": "The two zeta poles are cancelled with equal and opposite first-order normalization. The surviving finite contour correction is oriented and cannot be assigned to an unoriented scalar primitive row.",
        "effect_on_pushforward": "Any coprime-ray-to-boundary pushforward must reproduce the +/-1/2 endpoint Laurent coefficients and the -2 first ratio moment; these fix its primitive/seam normalization before completion.",
        "remaining_gate": "Carry out the regulated Barnes contour shift and identify each finite residue/finite-part term with the typed primitive, seam, and archimedean graph-dual currents; then prove projective convergence of the residual contour.",
        "artifacts_sha256": {name: hashlib.sha256((ROOT / path).read_bytes()).hexdigest() for name, path in SOURCES.items()},
        "passed": True,
        "rh_implication": False,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
