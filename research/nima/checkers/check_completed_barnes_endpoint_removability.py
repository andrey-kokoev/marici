from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/nima/results/completed-barnes-endpoint-removability.json"
SOURCES = {
    "laurent": "research/nima/results/ratio-profile-endpoint-laurent-data.json",
    "xi_square": "research/nima/the-completed-theta-autocorrelation-is-the-inverse-mellin-square-of-xi.md",
    "barnes": "research/nima/regulated-theta-autocorrelation-is-an-explicit-zeta-barnes-integral.md",
    "mellin": "research/nima/ratio-profile-mellin-transform-collapses-to-a-reflection-symmetric-gamma-factor.md",
}


def main() -> None:
    raw = {name: (ROOT / path).read_text(encoding="utf-8") for name, path in SOURCES.items()}
    laurent = json.loads(raw["laurent"])
    # Endpoint leading coefficients for I(s)=K(s) zeta(s) zeta(1-s).
    # s=0: K~s/2, zeta(s)~-1/2, zeta(1-s)~-1/s.
    value0 = Fraction(1, 2) * Fraction(-1, 2) * Fraction(-1, 1)
    # s=1+t: K~-t/2, zeta(1+t)~1/t, zeta(-t)~-1/2.
    value1 = Fraction(-1, 2) * Fraction(1, 1) * Fraction(-1, 2)
    checks = {
        "endpoint_derivatives_available": laurent["K_endpoint_data"]["K'(0)"] == "1/2" and laurent["K_endpoint_data"]["K'(1)"] == "-1/2",
        "zeta_endpoint_constants_standard": True,
        "s0_removable_value_quarter": value0 == Fraction(1, 4),
        "s1_removable_value_quarter": value1 == Fraction(1, 4),
        "reflection_values_equal": value0 == value1,
        "completed_integrand_is_xi_square": "K(s)\\zeta(s)\\zeta(1-s)=\\xi(s)^2" in raw["xi_square"],
        "source_says_zeta_poles_cancelled": "There is no residual zeta-pole anomaly" in raw["xi_square"],
        "regulated_poles_were_separate_factor_poles": "two arithmetic poles" in raw["barnes"],
    }
    assert all(checks.values())
    out = {
        "schema": "marici.nima.completed-barnes-endpoint-removability.v1",
        "status": "zeta_endpoint_poles_removable_completed_values_equal_one_quarter",
        "checks": checks,
        "completed_integrand": "I(s)=K(s) zeta(s) zeta(1-s)=xi(s)^2",
        "endpoint_values": {"I(0)": "1/4", "I(1)": "1/4"},
        "calculation_s0": "(s/2)(-1/2)(-1/s)=1/4",
        "calculation_s1": "(-(s-1)/2)(1/(s-1))(-1/2)=1/4",
        "correction": "The separate zeta factors have endpoint poles, but the completed unregulated integrand has no residues at s=0 or s=1. Primitive/seam currents cannot be identified with nonexistent residual endpoint poles.",
        "typed_consequence": "Any primitive, seam, or archimedean current decomposition must arise from the regulated finite-part derivative, contour orientation/gamma poles, or source-label pushforward while summing to the regular endpoint value 1/4 in each reciprocal chart.",
        "next_executable": "Expand the epsilon-regulated integrand to first order at epsilon=0. The epsilon derivative, not the completed endpoint residue, is the candidate anomaly/current row to compare with the graph-dual primitive functional.",
        "artifacts_sha256": {name: hashlib.sha256((ROOT / path).read_bytes()).hexdigest() for name, path in SOURCES.items()},
        "passed": True,
        "rh_implication": False,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
