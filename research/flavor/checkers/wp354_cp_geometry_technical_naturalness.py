"""WP354: exact distinction between CP technical naturalness and selection."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    seed, anomalous, interval = sp.symbols("t0 a ell", real=True)
    transported = sp.simplify(seed * sp.exp(anomalous * interval))
    beta_function = anomalous * sp.symbols("t", real=True)
    logarithmic_seed_response = sp.simplify(seed * sp.diff(transported, seed) / transported)
    anomalous_response = sp.simplify(sp.diff(sp.log(sp.Abs(transported)), anomalous))
    interval_response = sp.simplify(sp.diff(sp.log(sp.Abs(transported)), interval))
    cp_even_observable = sp.symbols("t", real=True) ** 2
    checks = {
        "zero_is_exact_rg_fixed_locus": beta_function.subs(sp.symbols("t", real=True), 0) == 0,
        "zero_seed_remains_zero": transported.subs(seed, 0) == 0,
        "sign_is_preserved_by_real_multiplicative_transport": sp.exp(anomalous * interval).is_positive,
        "logarithmic_seed_response_is_one": logarithmic_seed_response == 1,
        "transport_depends_on_anomalous_dimension": anomalous_response == interval,
        "transport_depends_on_scale_interval": interval_response == anomalous,
        "cp_even_readout_is_quadratic_near_zero": sp.diff(cp_even_observable, sp.symbols("t", real=True), 2) == 2,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP354",
        "admitted_state_domain": "a real CP-odd geometry coordinate t with multiplicative transport dt/dell=a*t between a frozen source boundary and flavor matching scale",
        "faithful_quotient_coordinate": "signed t when a CP-orientation instrument is admitted, or t^2 for CP-even readout",
        "source_operation": "CP symmetry enforces the fixed locus t=0; multiplicative RG transports a declared breaking seed t0",
        "transport_solution": str(transported),
        "beta_function": str(beta_function),
        "logarithmic_seed_response": str(logarithmic_seed_response),
        "anomalous_dimension_response": str(anomalous_response),
        "scale_interval_response": str(interval_response),
        "contextual_partition": "zero and nonzero seeds remain distinct under finite multiplicative transport; CP-even readout further identifies opposite signs",
        "classification": "technical naturalness and stability of a small CP-breaking geometry, not a selector of its nonzero magnitude; the boundary seed retains unit logarithmic authority",
        "smallest_exact_falsifier": "rescaling t0 by any factor rescales the matched t by the same factor, since d log|t|/d log|t0|=1",
        "remaining_physical_instrument_gate": "derive a nonzero boundary seed or threshold kick independently of flavor data, fix a and the scale interval in one scheme, and test the transported J prediction without retuning",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp354_cp_geometry_technical_naturalness.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
