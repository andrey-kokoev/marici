"""WP309: exact parameter-free selector from reciprocal duality."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    ratio = sp.symbols("ratio", positive=True)
    duality = 1 / ratio
    potential = sp.expand((ratio - 1 / ratio) ** 2)
    transformed = sp.simplify(potential.subs(ratio, duality))
    stationary = sp.solve(sp.Eq(sp.diff(potential, ratio), 0), ratio)
    fixed = sp.solve(sp.Eq(ratio, duality), ratio)
    hessian_at_fixed = sp.simplify(sp.diff(potential, ratio, 2).subs(ratio, 1))

    scale = sp.symbols("scale", positive=True)
    scaled_duality = scale**2 / ratio
    scaled_fixed = sp.solve(sp.Eq(ratio, scaled_duality), ratio)[0]
    scaled_response = sp.diff(scaled_fixed, scale)

    checks = {
        "reciprocal_map_is_involution": sp.simplify(duality.subs(ratio, duality) - ratio) == 0,
        "potential_is_reciprocal_invariant": sp.simplify(transformed - potential) == 0,
        "positive_fixed_locus_is_singleton_one": fixed == [1],
        "positive_stationary_locus_is_singleton_one": stationary == [1],
        "potential_is_nonnegative_sum_square": potential == ratio**2 - 2 + ratio ** -2,
        "fixed_point_has_positive_hessian": hessian_at_fixed == 8,
        "scaled_duality_fixed_point_is_scale": scaled_fixed == scale,
        "scaled_duality_restores_unit_response": scaled_response == 1,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP309",
        "theorem_domain": "positive dimensionless ratio r with admitted reciprocal duality r->1/r",
        "selector_potential": "V(r)=(r-1/r)^2",
        "selected_point": "r_star=1",
        "source_response_rank": 0,
        "scaled_hostile_family": {
            "duality": "r->kappa^2/r",
            "fixed_point": str(scaled_fixed),
            "response_to_kappa": str(scaled_response),
        },
        "descent": "conditional on r being a weak-basis-invariant dimensionless coordinate and reciprocal duality being an admitted source operation rather than a chart relabelling",
        "classification": "genuine parameter-free dimensionless ratio selector and rigidifier on the declared duality quotient; not a selector of absolute physical16 scales",
        "smallest_exact_falsifier": "replacing the canonical reciprocal map by r->kappa^2/r moves the fixed point to kappa and restores rank-one source ambiguity",
        "remaining_physical_instrument_gate": "derive reciprocal duality from flavor source dynamics, identify its executable operation and invariant ratio, test anomalies and breaking, and map the selected ratio into physical16 without importing a fitted scale",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp309_reciprocal_ratio_selector.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
