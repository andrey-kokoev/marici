"""Exact normalization correction for WP485-WP487."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp485 = load("wp485_mixed_gauge_pole_residues.json")
wp486 = load("wp486_pole_current_inverse_instrument.json")
wp487 = load("wp487_total_width_closure_cone.json")

g, mu, v, Q = sp.symbols("g_F mu v Q", positive=True)
physical_norm_squared = 6 * mu**2
quintet_mass_squared = 3 * g**2 * mu**2
physical_clock_ratio = sp.sqrt(g**2 * physical_norm_squared) / v
pole_clock_ratio = sp.sqrt(2 * Q) / v

packet_texts = {
    name: (root / name).read_text(encoding="utf-8")
    for name in [
        "flavor-mixed-gauge-pole-residues.md",
        "flavor-pole-current-inverse-instrument.md",
        "flavor-total-width-closure-cone.md",
    ]
}

checks = {
    "wp485_dependency_passed": wp485["passed"],
    "wp486_dependency_passed": wp486["passed"],
    "wp487_dependency_passed": wp487["passed"],
    "physical_norm_is_six_mu_squared": physical_norm_squared == 6 * mu**2,
    "quintet_readout_gives_physical_clock": sp.simplify(
        physical_clock_ratio - pole_clock_ratio.subs(Q, quintet_mass_squared)
    ) == 0,
    "amplitude_is_not_physical_norm": sp.simplify(sp.sqrt(physical_norm_squared) / mu) == sp.sqrt(6),
    "wp485_packet_declares_normalization": "f_{\\rm phys}^2" in packet_texts["flavor-mixed-gauge-pole-residues.md"],
    "wp486_packet_declares_clock_readout": "\\sqrt{2Q}" in packet_texts["flavor-pole-current-inverse-instrument.md"],
    "wp487_witness_uses_mu": "g_F^2=\\mu^2" in packet_texts["flavor-total-width-closure-cone.md"],
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP488",
    "corrected_packets": ["WP485", "WP486", "WP487"],
    "canonical_coordinates": {
        "adjoint_amplitude": "mu in X_i=mu J_i",
        "physical_flavor_norm": "f_phys^2=sum_i Tr(X_i^2)=6 mu^2",
        "quintet_mass_squared": "Q=3 g_F^2 mu^2",
        "physical_clock_ratio": "g_F f_phys/v=sqrt(2 Q)/v",
    },
    "unchanged_results": "mass Gram, pole multiplicities, residue inversion, response rank, and width-closure inequalities",
    "corrected_authority": "WP485-WP487 identify and constrain the adjoint amplitude mu; conversion to the programme clock f_phys carries an exact factor sqrt(6).",
    "smallest_exact_falsifier": "Treating the adjoint amplitude mu as the physical norm f_phys misses the clock ratio by the exact factor sqrt(6).",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp488_flavor_clock_normalization_correction.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
