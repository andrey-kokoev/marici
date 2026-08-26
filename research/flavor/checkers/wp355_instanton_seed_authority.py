"""WP355: exact authority and control audit for an instanton-generated CP seed."""

import json
import math
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    coupling = sp.symbols("g", real=True, positive=True)
    charge = sp.symbols("n", integer=True, positive=True)
    seed = sp.exp(-8 * sp.pi**2 * charge / coupling**2)
    logarithmic_coupling_response = sp.simplify(coupling * sp.diff(sp.log(seed), coupling))
    charge_ratio = sp.simplify(seed.subs(charge, charge + 1) / seed)
    wp353 = json.loads((ROOT / "results/wp353_complex_geometry_deformation.json").read_text(encoding="utf-8"))
    fitted_seed_estimate = float(wp353["leading_small_branch_t_estimate"])
    required_action = -math.log(fitted_seed_estimate)
    required_unit_charge_coupling = math.sqrt(8 * math.pi**2 / required_action)
    weak_coupling_ceiling = math.exp(-8 * math.pi**2)
    checks = {
        "zero_coupling_limit_selects_zero_seed": sp.limit(seed.subs(charge, 1), coupling, 0, dir="+") == 0,
        "unit_charge_seed_is_nonzero_for_positive_coupling": seed.subs(charge, 1).is_positive,
        "logarithmic_coupling_response_is_nonzero": logarithmic_coupling_response == 16 * sp.pi**2 * charge / coupling**2,
        "successive_charge_sectors_are_exponentially_distinct": charge_ratio == sp.exp(-8 * sp.pi**2 / coupling**2),
        "unit_charge_weak_coupling_seed_is_far_below_fitted_scale": weak_coupling_ceiling < fitted_seed_estimate * 1e-20,
        "required_unit_charge_coupling_exceeds_one": required_unit_charge_coupling > 1,
        "required_action_is_positive": required_action > 0,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP355",
        "admitted_state_domain": "positive coupling g and positive integer topological charge n with candidate seed t_n=exp(-8*pi^2*n/g^2); controlled weak-coupling test restricted to g<=1",
        "faithful_quotient_coordinate": "the CP-odd geometry-seed magnitude before multiplicative WP354 transport",
        "source_operation": "a quantized nonperturbative sector generates an exponentially small threshold seed",
        "seed_formula": str(seed),
        "logarithmic_coupling_response": str(logarithmic_coupling_response),
        "successive_charge_ratio": str(charge_ratio),
        "wp353_fitted_seed_estimate": fitted_seed_estimate,
        "required_action_for_estimate": required_action,
        "required_unit_charge_coupling": required_unit_charge_coupling,
        "unit_charge_g_at_most_one_seed_ceiling": weak_coupling_ceiling,
        "contextual_partition": "quantized n gives discrete seed branches, while continuous g moves every branch and survives to the flavor geometry",
        "classification": "a technically natural nonperturbative carrier of smallness, not a numerical selector; the coupling retains physical authority and the fitted scale lies outside the declared g<=1 control domain",
        "smallest_exact_falsifier": "d log(t_n)/d log(g)=16*pi^2*n/g^2 is nonzero, so quantized charge does not remove continuous coupling authority",
        "remaining_physical_instrument_gate": "derive and measure the relevant coupling and instanton prefactor at the threshold, prove semiclassical control or use a nonperturbative calculation, freeze RG matching, and test without fitting g to J",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp355_instanton_seed_authority.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
