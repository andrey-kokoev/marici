"""WP319: exact authority audit for a fixed-charge sector centered at N."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def ratio(magnitude):
    return sp.sqrt(magnitude**2 + 1) + magnitude


def energy(magnitude, center):
    return (magnitude - center) ** 2


def main():
    centers = [1, 2, 63, 64, 65]
    domain = list(range(1, 101))
    minima = {
        center: [m for m in domain if energy(m, center) == min(energy(k, center) for k in domain)]
        for center in centers
    }
    selected_ratios = {center: ratio(center) for center in centers}
    N = sp.symbols("N", positive=True)
    response = sp.simplify(sp.diff(sp.sqrt(N**2 + 1) + N, N))
    checks = {
        "each_center_selects_itself": all(minima[center] == [center] for center in centers),
        "center_64_selects_charge_64": minima[64] == [64],
        "neighboring_centers_select_different_charges": minima[63] == [63] and minima[65] == [65],
        "selected_ratio_depends_on_center": len(set(selected_ratios.values())) == len(centers),
        "continuous_center_response_is_strictly_positive": sp.simplify(response - 1) > 0,
        "unit_center_recovers_wp316": selected_ratios[1] == 1 + sp.sqrt(2),
        "magnitude_64_value_is_exact": selected_ratios[64] == 64 + sp.sqrt(4097),
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP319",
        "admitted_state_domain": "positive integer flux magnitudes m from 1 through 100 with a family of source energies E_N(m)=(m-N)^2",
        "faithful_quotient_coordinate": "flux magnitude after sign exchange, followed conditionally by the hierarchy ratio sqrt(m^2+1)+m",
        "source_authorized_probe_family": "energy minimization for a declared but otherwise free integer center N",
        "contextual_partition": {str(center): minima[center] for center in centers},
        "selected_ratios": {str(center): str(value) for center, value in selected_ratios.items()},
        "center_response": str(response),
        "classification": "the centered energy is a rigid selector conditional on N, but N carries the full discrete numerical authority; it does not explain magnitude 64",
        "smallest_exact_falsifier": "changing the admissible center from N=64 to N=63 changes the unique selected orbit from magnitude 64 to magnitude 63 while preserving the same constructor grammar",
        "remaining_physical_instrument_gate": "derive N=64 as a theorem of an independently admitted source topology or conservation law, rather than imposing it as a boundary sector selected after flavor readout",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp319_fixed_charge_center_authority.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
