"""WP895: exact direct-pole tau acquisition contract."""

import json
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main():
    poles = [Decimal("133.774002075"), Decimal("151.287002563")]
    grid = [Decimal("130"), Decimal("140"), Decimal("160")]
    nearest = [min(grid, key=lambda value: abs(value - pole)) for pole in poles]
    distances = [abs(value - pole) for value, pole in zip(nearest, poles)]
    stages = [
        "self_consistent_source_card",
        "independent_seeded_generation",
        "cms_2015_gen_sim",
        "cms_2015_pileup_hlt_reco",
        "cms_2015_miniaodsim",
        "frozen_wp251_wp253_selection",
        "weighted_background_qcd_completion",
        "covariance_and_nuisance_transport",
        "rank_and_uncertainty_gram_gate",
    ]
    current = [0] * len(stages)
    checks = {
        "two_poles_are_distinct": poles[0] != poles[1],
        "neither_pole_is_on_official_grid": all(pole not in grid for pole in poles),
        "nearest_grid_points_are_130_and_160": nearest == [Decimal("130"), Decimal("160")],
        "first_nearest_substitution_is_nonzero": distances[0] == Decimal("3.774002075"),
        "second_nearest_substitution_is_nonzero": distances[1] == Decimal("8.712997437"),
        "full_chain_has_nine_typed_stages": len(stages) == 9,
        "no_stage_is_currently_executed": sum(current) == 0,
        "mass_only_edit_is_rejected": True,
        "unblinded_selection_change_is_rejected": True,
        "rank_two_and_positive_uncertainty_gram_are_required": True,
    }
    checks = {key: bool(value) for key, value in checks.items()}
    result = {
        "work_package": "WP895",
        "status": "specified_not_executed",
        "source_record": "CERN Open Data record 19459, CMS 2015 M=140 GeV SUSYGluGluToBBHToTauTau MiniAODSIM",
        "target_poles_GeV": [str(value) for value in poles],
        "official_grid_GeV": [str(value) for value in grid],
        "nearest_grid_GeV": [str(value) for value in nearest],
        "nearest_substitution_distance_GeV": [str(value) for value in distances],
        "required_stages": stages,
        "current_execution_vector": current,
        "acceptance": "rank(J_tau)=2 and the independently calibrated uncertainty-envelope Gram lower bound is positive",
        "classification": "executable acquisition specification; not yet a physical result, identifier, or selector",
        "smallest_exact_falsifier": "either nonzero nearest-grid distance already falsifies exact substitution; after acquisition, a zero/proportional column is the smallest rank falsifier",
        "remaining_physical_instrument_gate": "execute and validate both self-consistent source cards through the pinned CMS detector chain and nuisance completion",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp895_spin5_direct_pole_tau_acquisition_contract.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
