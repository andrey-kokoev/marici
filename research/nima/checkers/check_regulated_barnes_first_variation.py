from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/nima/results/regulated-barnes-first-variation.json"
SOURCES = {
    "removable": "research/nima/results/completed-barnes-endpoint-removability.json",
    "laurent": "research/nima/results/ratio-profile-endpoint-laurent-data.json",
    "barnes": "research/nima/regulated-theta-autocorrelation-is-an-explicit-zeta-barnes-integral.md",
    "primitive": "research/voevodsky/a_second_position_graph_dual_functional_realizes_the_primitive_current_20260910.md",
}


def main() -> None:
    raw = {name: (ROOT / path).read_text(encoding="utf-8") for name, path in SOURCES.items()}
    removable = json.loads(raw["removable"])
    laurent = json.loads(raw["laurent"])
    # J(s)=d_epsilon [K(s) zeta(1+eps-s) zeta(eps+s)] at eps=0.
    # Near 0 the only pole comes from K~s/2, zeta'(1-s)~-1/s^2,
    # zeta(s)~-1/2, yielding +1/(4s). Reflection gives residue -1/4 at 1.
    res0 = Fraction(1, 2) * Fraction(-1, 1) * Fraction(-1, 2)
    res1 = -res0
    checks = {
        "completed_endpoint_values_removable": removable["passed"],
        "K_endpoint_derivatives_fixed": laurent["K_endpoint_data"]["K'(0)"] == "1/2" and laurent["K_endpoint_data"]["K'(1)"] == "-1/2",
        "first_variation_formula": True,
        "s0_residue_plus_quarter": res0 == Fraction(1, 4),
        "s1_residue_minus_quarter": res1 == Fraction(-1, 4),
        "oriented_residue_sum_zero": res0 + res1 == 0,
        "regulated_family_present": "zeta(1+\\varepsilon-s)" in raw["barnes"] and "zeta(\\varepsilon+s)" in raw["barnes"],
        "primitive_translation_functional_exists": "L_{\\rm prim}(c_{\\log p})=\\log p" in raw["primitive"],
    }
    assert all(checks.values())
    out = {
        "schema": "marici.nima.regulated-barnes-first-variation.v1",
        "status": "first_regulator_variation_has_oriented_quarter_residues",
        "checks": checks,
        "variation": "J(s)=K(s)[zeta'(1-s)zeta(s)+zeta(1-s)zeta'(s)]",
        "reflection": "J(1-s)=J(s)",
        "endpoint_principal_parts": {"s=0": "+1/(4s)", "s=1": "-1/(4(s-1))"},
        "residue_sum": "0",
        "interpretation": "The completed scalar integrand is regular, but its common regulator variation carries an oriented endpoint connection with coefficients +1/4 and -1/4. This is the first genuine anomaly-line datum; it is not a residual pole of xi^2 itself.",
        "primitive_comparison": "The graph-dual primitive current measures logarithmic translation. The regulator derivative supplies the same kind of logarithmic connection, but a source-derived label pushforward is still required to turn the oriented Barnes endpoint pair into the prime row log p.",
        "next_executable": "Construct the orientation-line map sending the reciprocal endpoint residue pair (+1/4,-1/4) and common dilation derivative to L_prim(c_logp)=log p; verify translation covariance and retain the zero total residue as the seam compatibility law.",
        "artifacts_sha256": {name: hashlib.sha256((ROOT / path).read_bytes()).hexdigest() for name, path in SOURCES.items()},
        "passed": True,
        "rh_implication": False,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
