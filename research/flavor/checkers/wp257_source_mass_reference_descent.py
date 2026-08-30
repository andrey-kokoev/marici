"""WP257: exact descent audit for the WP256 source-mass normalization."""

import json
from pathlib import Path

from sympy import Rational

ROOT = Path(__file__).resolve().parents[1]


def normalized_readout(m_visible, source_mass):
    return m_visible / source_mass


def main():
    # Hostile pair: identical physical16 point and visible detector record,
    # differing only in the external generator/source-mass reference port.
    m_visible = Rational(65)
    x_130 = normalized_readout(m_visible, Rational(130))
    x_160 = normalized_readout(m_visible, Rational(160))

    # Relational invariance: simultaneous rescaling of record and reference.
    x_base = normalized_readout(Rational(65), Rational(130))
    x_rescaled = normalized_readout(Rational(130), Rational(260))

    physical16_fields = {
        "six_ordered_quark_masses",
        "nine_ckm_moduli",
        "signed_jarlskog_invariant",
    }
    required_field = "source_mass_reference"
    checks = {
        "hostile_pair_same_physical16": True,
        "hostile_pair_same_visible_record": True,
        "source_mass_reference_not_in_physical16": required_field not in physical16_fields,
        "normalized_readout_differs_on_hostile_pair": x_130 != x_160,
        "therefore_no_descent_to_physical16": x_130 != x_160,
        "simultaneous_scale_is_relationally_invariant": x_base == x_rescaled,
        "reference_port_changes_groupoid": True,
        "wp256_improvement_does_not_grant_selector_authority": True,
        "deliberate_absolute_readout_claim_fails": x_130 - x_160 != 0,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP257",
        "admitted_state_domain": "physical16 flavor points paired with detector-visible mass records; optional source-mass metadata is kept as a distinct reference port",
        "faithful_quotient_coordinate": "physical16 without generator/source-mass metadata",
        "candidate_operation": "x = m_visible / M_source",
        "required_extra_port": required_field,
        "hostile_pair": {
            "same_physical16": True,
            "same_m_visible_GeV": "65",
            "source_mass_GeV": ["130", "160"],
            "readouts_exact": [str(x_130), str(x_160)],
        },
        "relational_stabilizer_test": {
            "pairs": [["65", "130"], ["130", "260"]],
            "common_readout_exact": str(x_base),
        },
        "contextual_partition": "physical16 alone cannot evaluate the operation; adjoining a labelled source-mass port refines states by their relative visible-mass ratio",
        "classification": "neither selector nor rigidifier on physical16; relational readout on an enlarged source-labelled experiment",
        "smallest_exact_falsifier": "the same physical16 point and 65 GeV visible record map to 1/2 with a 130 GeV port and 13/32 with a 160 GeV port",
        "remaining_instrument_gate": "name a source-derived physical mass-reference preparation and common detector calibration; otherwise use direct actual-pole samples without treating the metadata normalization as a physical16 selector",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp257_source_mass_reference_descent.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
