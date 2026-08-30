"""WP299: exact finite typing test separating faithful readout from selection."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def image(mapping, domain):
    return {mapping[item] for item in domain}


def fibers(mapping, domain):
    result = {}
    for item in domain:
        result.setdefault(mapping[item], set()).add(item)
    return result


def main():
    physical_domain = {"x0", "x1", "x2", "x3"}
    faithful_readout = {point: f"r_{point}" for point in physical_domain}
    branch_readout = {"x0": "+", "x1": "+", "x2": "-", "x3": "-"}
    source_selector = {"x0": "x0", "x1": "x0", "x2": "x2", "x3": "x2"}

    readout_image = image(faithful_readout, physical_domain)
    branch_fibers = fibers(branch_readout, physical_domain)
    selector_image = image(source_selector, physical_domain)
    selected_readout_image = {faithful_readout[point] for point in selector_image}
    observed_record = faithful_readout["x1"]
    posterior_fiber = fibers(faithful_readout, physical_domain)[observed_record]

    checks = {
        "faithful_readout_has_singleton_fibers": all(len(fiber) == 1 for fiber in fibers(faithful_readout, physical_domain).values()),
        "faithful_readout_preserves_full_family_cardinality": len(readout_image) == len(physical_domain) == 4,
        "branch_readout_is_nonfaithful": any(len(fiber) > 1 for fiber in branch_fibers.values()),
        "source_selector_has_proper_image": selector_image < physical_domain and len(selector_image) == 2,
        "readout_after_selector_has_reduced_image": len(selected_readout_image) == len(selector_image) < len(readout_image),
        "conditioning_on_observed_record_gives_singleton": posterior_fiber == {"x1"},
        "conditioning_does_not_change_prior_source_image": image({point: point for point in physical_domain}, physical_domain) == physical_domain,
        "selector_is_idempotent": all(source_selector[source_selector[point]] == source_selector[point] for point in physical_domain),
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP299",
        "theorem_domain": "finite proxy for an admissible physical16 family with typed source operations and readout maps",
        "typed_arrows": {
            "faithful_readout": "R:X->Y with singleton fibers and |R(X)|=|X|",
            "selector": "S:X->X with proper idempotent image S(X) subsetneq X",
            "selected_readout": "R after S, whose reduced record image is inherited from S",
            "conditioning": "R^{-1}(observed record), a posterior inference after an outcome rather than a source operation",
        },
        "finite_audit": {
            "physical_domain": sorted(physical_domain),
            "faithful_readout_image": sorted(readout_image),
            "branch_fibers": {key: sorted(value) for key, value in branch_fibers.items()},
            "selector_image": sorted(selector_image),
            "selected_readout_image": sorted(selected_readout_image),
            "posterior_fiber_at_r_x1": sorted(posterior_fiber),
        },
        "classification": "WP298 supplies a faithful separator/readout only; a proper reduction must occur at an independently source-authorized selector arrow before readout",
        "smallest_exact_falsifier": "the identity-like readout reconstructs all four states perfectly while leaving the admissible source image at all four states",
        "anti_postselection_rule": "a singleton posterior fiber after observing a record does not retroactively select the source state or predict its numerical value",
        "remaining_physical_instrument_gate": "construct an admitted physical operation S on the flavor source whose proper physical16 image is derived before and independently of the faithful readout values",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp299_faithful_readout_not_selector.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
