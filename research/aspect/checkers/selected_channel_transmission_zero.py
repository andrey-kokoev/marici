"""Exact selected-channel transmission-zero checks."""

from fractions import Fraction as F
import json
from pathlib import Path


def det2(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def main():
    A, B = F(0), F(1)
    Cs, Ds = F(-1, 2), F(1, 2)
    Cc, Dc = F(1, 2), F(1, 2)

    # Rosenbrock determinant det([[lambda-A,-B],[Cs,Ds]]).
    def rosenbrock_det(lam):
        return (lam - A) * Ds + B * Cs

    zero = F(1)
    x = u = F(1)
    selected = Cs * x + Ds * u
    complementary = Cc * x + Dc * u
    full_readout = [[Cs, Ds], [Cc, Dc]]

    # Evaluate S(q)=1/2[[1-q,1+q],[1+q,1-q]] at q=+/-1.
    def scattering(q):
        return [[(1 - q) / 2, (1 + q) / 2],
                [(1 + q) / 2, (1 - q) / 2]]

    S_dc = scattering(F(1))
    S_nyquist = scattering(F(-1))

    # At q=1 the selected scalar h=(1-q)/2 is zero. Its real part
    # cannot satisfy a strict positive lower bound, and z=1 is a boundary zero.
    h_at_zero = S_dc[0][0]

    checks = {
        "selected_rosenbrock_zero_at_one": rosenbrock_det(zero) == 0,
        "dark_trajectory_is_nontrivial": selected == 0 and x != 0 and u != 0,
        "complementary_output_detects_dark_trajectory": complementary == 1,
        "complete_detector_family_is_faithful": det2(full_readout) != 0,
        "selected_realization_is_controllable": B != 0,
        "selected_realization_is_observable": Cs != 0,
        "dc_scattering_is_lossless_and_reciprocal": S_dc == [[0, 1], [1, 0]],
        "nyquist_scattering_is_lossless_and_reciprocal": S_nyquist == [[1, 0], [0, 1]],
        "passive_reciprocal_selected_channel_has_zero": h_at_zero == 0,
        "strict_positive_realness_not_implied": h_at_zero == 0,
        "strict_minimum_phase_not_implied": zero == 1,
    }
    result = {
        "schema": "marici.aspect.selected_channel_transmission_zero.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "exact_arithmetic": True,
        "checks": checks,
        "witness": {
            "A": str(A), "B": str(B), "C_selected": str(Cs), "D_selected": str(Ds),
            "C_complement": str(Cc), "D_complement": str(Dc),
            "transmission_zero": str(zero),
            "rosenbrock_determinant_formula": "(lambda-1)/2",
            "kernel_trajectory": {"x": str(x), "u": str(u)},
            "selected_output": str(selected),
            "complementary_output": str(complementary),
            "full_readout_determinant": str(det2(full_readout)),
        },
        "separation": {
            "total_scattering": "unitary and reciprocal complete two-port family",
            "tomography": "two output rows faithfully recover the declared (x,u) pair",
            "selected_zero_freeness": "false at z=1 for h(z)=(z-1)/(2z)",
        },
        "stronger_source_native_condition_found": False,
        "missing_for_stronger_claim": [
            "pre-scalar collocation", "strict positive-real certificate",
            "outer factorization", "bounded inverse", "independent phase authority",
        ],
        "claim_boundary": "finite optical transmission-zero taxonomy; no RH claim",
    }
    out = Path(__file__).parents[1] / "results" / "selected_channel_transmission_zero.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if result["status"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
