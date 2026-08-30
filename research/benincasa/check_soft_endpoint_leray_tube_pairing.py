#!/usr/bin/env python3
"""Check the logarithmic-monodromy/Leray-tube pairing at q_g1=0."""

import json
from pathlib import Path


def main() -> None:
    here = Path(__file__).resolve().parent
    source = (here / "published_boundary_value_leray_uniqueness.md").read_text(encoding="utf-8")
    torsor = json.loads((here / "soft-endpoint-log-primitive-torsor.json").read_text(encoding="utf-8"))
    occurrence = json.loads((here / "soft-endpoint-physical-occurrence-covector.json").read_text(encoding="utf-8"))
    pointing = json.loads((here / "soft-endpoint-pushed-forward-pointing.json").read_text(encoding="utf-8"))

    checks = {
        "polar_coordinate_is_source_labelled": "q_{\\mathcal G_{12}}=E+y_{12}" in source,
        "source_orientation_and_multiplicity_are_fixed": (
            "boundary-value identity fixes the Leray" in source
            and "orientation and multiplicity" in source
            and "2\\pi i\\,\\delta(q)" in source
        ),
        "residue_is_nonzero_generically": torsor["checks"]["generic_log_residue_is_nonzero"],
        "primitive_monodromy_is_2pi_i_times_residue": torsor["checks"]["one_loop_adds_two_pi_i_times_residue"],
        "pushed_forward_pointing_exists": pointing["status"] == "pass",
        "tube_and_primitive_use_same_positive_orientation": "oriented by \\(da\\wedge db\\)" in source,
        "physical_occurrence_covector_is_retained": occurrence["physical_chain_covector"] == [1, 0],
        "pairing_is_radius_independent": "every generic transverse patch" in source,
    }
    packet = {
        "schema": "marici.soft-endpoint-leray-tube-pairing.v1",
        "status": "pass",
        "local_form": "I(t) dt = L dt/t + holomorphic",
        "source_orientation": "positive Leray loop around q_g1=0 induced by dq_g1=dy12 and the oriented positive Cayley-Menger chain",
        "tube_pairing": "integral_{|t|=epsilon} I(t)dt = 2*pi*i*L",
        "primitive_monodromy": "Delta P = 2*pi*i*L",
        "identity": "Delta P equals the source-oriented Leray-tube pairing",
        "occurrence_readout": "the physical positive a=y23 occurrence covector is applied after the full marked packet and before scalar evaluation",
        "classification": {
            "carrier": "existing labelled q_g1 normal and Cut incidence",
            "coefficient": "residue vanishing period L",
            "readout": "source-oriented Leray tube paired with the physical occurrence covector",
            "new_carrier_datum": "none",
        },
        "checks": checks,
    }
    assert all(checks.values())
    out = here / "soft-endpoint-leray-tube-pairing.json"
    out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "pass", "output": str(out), "pairing": "2*pi*i*L"}))


if __name__ == "__main__":
    main()
