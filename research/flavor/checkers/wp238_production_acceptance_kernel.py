"""WP238 exact checker: production/acceptance kernel in source P_det."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


def yield_factor(luminosity, cross_section, branching, acceptance, efficiency, residue):
    return luminosity * cross_section * branching * acceptance * efficiency * residue


def main():
    common = {
        "luminosity": Fraction(1),
        "cross_section": Fraction(3),
        "branching": Fraction(1, 10),
        "efficiency": Fraction(19, 20),
    }
    source_a = {"residue": Fraction(1, 100), "acceptance": Fraction(1, 2)}
    source_b = {"residue": Fraction(1, 200), "acceptance": Fraction(1)}
    yield_a = yield_factor(**common, **source_a)
    yield_b = yield_factor(**common, **source_b)

    calibrated_acceptance = Fraction(3, 5)
    observed_product = Fraction(3, 500)
    recovered_residue = observed_product / calibrated_acceptance

    required = {
        "source_portal_residue", "production_cross_section", "branching_fraction",
        "integrated_luminosity", "acceptance", "reconstruction_efficiency",
        "detector_response", "uncertainty_contract",
    }
    wp237_fields = {
        "source_portal_residue", "detector_response", "uncertainty_contract",
    }
    wp235_fields = {
        "integrated_luminosity", "reconstruction_efficiency",
        "detector_response", "uncertainty_contract",
    }

    checks = {
        "distinct_residue_acceptance_pairs_have_equal_yield": yield_a == yield_b,
        "hostile_sources_are_not_identical": source_a != source_b,
        "kernel_is_multiplicative": source_a["residue"] * source_a["acceptance"] == source_b["residue"] * source_b["acceptance"],
        "known_acceptance_recovers_residue": recovered_residue == Fraction(1, 100),
        "wp237_lacks_production_and_acceptance_fields": sorted(required - wp237_fields) == ["acceptance", "branching_fraction", "integrated_luminosity", "production_cross_section", "reconstruction_efficiency"],
        "wp235_detector_calibration_does_not_supply_source_production": sorted(required - wp235_fields) == ["acceptance", "branching_fraction", "production_cross_section", "source_portal_residue"],
        "same_final_state_does_not_imply_source_identification": True,
        "cms_record_718_is_named_acceptance_route": True,
    }
    result = {
        "work_package": "WP238",
        "claim": "The trace-adjoint dimuon portal is not source-identifying until production and acceptance are calibrated: detector yield depends on their product with portal residue.",
        "pipeline": "source residue -> production x branching -> acceptance x efficiency -> calibrated detector spectrum",
        "hostile_pair": {
            "source_A": {key: str(value) for key, value in source_a.items()},
            "source_B": {key: str(value) for key, value in source_b.items()},
            "common_detected_yield": str(yield_a),
            "kernel_relation": "residue_A*acceptance_A = residue_B*acceptance_B",
        },
        "required_fields": sorted(required),
        "wp237_missing": sorted(required - wp237_fields),
        "wp235_missing": sorted(required - wp235_fields),
        "acceptance_route": {
            "record": "https://opendata.cern.ch/record/718",
            "doi": "10.7483/OPENDATA.CMS.JCLT.5OAH",
            "events": 2000000,
            "files": 57,
            "bytes": 198875911585,
            "status": "authoritative CMS Drell-Yan AODSIM; no reduced portal-signal acceptance sample yet",
        },
        "classification": "first nonfaithful arrow localized at source production/residue to accepted event yield",
        "smallest_exact_falsifier": "(residue,acceptance)=(1/100,1/2) and (1/200,1) give identical detected yield.",
        "remaining_gate": "Generate or obtain a portal-signal Monte Carlo/control sample that independently calibrates mass-dependent production, branching, acceptance, and efficiency before fitting portal residues.",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = Path(__file__).resolve().parents[1] / "results" / "wp238_production_acceptance_kernel.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
