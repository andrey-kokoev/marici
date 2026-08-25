"""Requirement-by-requirement audit of the QED dispersive completion arc."""

import json
from pathlib import Path


NIMA = Path(__file__).parents[1]
RESULTS = NIMA / "results"


def load(name):
    return json.loads((RESULTS / name).read_text(encoding="utf-8"))


def all_gates(packet):
    return all(packet["gates"].values())


def main():
    conventions = load("qed-vector-dispersion-conventions.json")
    real = load("qed-phi1-full-dispersion-real.json")
    transfer = load("qed-phi1-dispersion-transfer-replication.json")
    complex_packet = load("qed-phi1-complex-continuation.json")
    phi25 = load("qed-phi25-full-dispersion.json")
    residual = load("qed-helicity-residual-factor.json")
    symmetry = load("qed-dispersion-completion-symmetry-audit.json")
    uniqueness = load("qed-oriented-cut-uniqueness.json")
    instrument = load("qed-elastic-pair-instrument.json")
    fixed_t = load("qed-fixed-t-subtraction-gate.json")

    cases = transfer["cases"]
    a_ratio = cases[1]["subtraction"]["a"] / cases[0]["subtraction"]["a"]
    b_ratio = cases[1]["subtraction"]["b"] / cases[0]["subtraction"]["b"]

    criteria = {
        "01_conventions_frozen": all_gates(conventions),
        "02_right_left_spectral_vectors_assembled": all(
            conventions["gates"][key]
            for key in (
                "moment_character_degree_2",
                "moment_character_degree_3",
                "phi1_crosses_to_declared_partner",
            )
        ),
        "03_coupled_dispersion_derived": (
            all_gates(real) and all_gates(phi25)
        ),
        "04_minimal_subtraction_space_classified": (
            conventions["gates"]["subtraction_space_has_two_parameters"]
            and fixed_t["maximum_net_power"] == "0"
            and 3.9 < a_ratio < 4.2
            and 1.9 < b_ratio < 2.1
        ),
        "05_hostile_real_and_complex_reconstruction": (
            all_gates(real) and all_gates(complex_packet) and all_gates(phi25)
        ),
        "06_independent_exact_amplitude_comparison": (
            real["heldout_relative_residual"] < 3e-6
            and max(p["relative_residual"] for p in complex_packet["points"])
            < 2e-6
        ),
        "07_residual_matrix_extracted": (
            residual["gates"]["full_diagonal_residual_is_identity"]
        ),
        "08_polynomial_and_cdd_classified": all_gates(uniqueness),
        "09_symmetry_and_optical_audit": all_gates(symmetry),
        "10_surviving_ambiguity_is_finite_and_source_authorized": (
            residual["gates"]["boundary_packet_has_dimension_four"]
            and uniqueness["ambiguity_classification"]["inner_or_CDD"]
            == "excluded within the exact one-loop analytic class"
        ),
        "11_elastic_plus_pair_channel_constructed": all_gates(instrument),
        "12_instrument_verdict_and_single_missing_datum": bool(
            instrument["single_missing_datum"]
        ),
    }
    criteria = {key: bool(value) for key, value in criteria.items()}
    assert all(criteria.values()), criteria

    result = {
        "schema": "marici.qed-vector-dispersion-completion-audit.v1",
        "criteria": criteria,
        "evidence": {
            "01-03": [
                "qed-vector-dispersion-conventions.json",
                "qed-phi1-full-dispersion-real.json",
                "qed-phi25-full-dispersion.json",
            ],
            "04": [
                "qed-fixed-t-subtraction-gate.json",
                "qed-phi1-dispersion-transfer-replication.json",
            ],
            "05-06": [
                "qed-phi1-complex-continuation.json",
                "qed-phi25-full-dispersion.json",
            ],
            "07-10": [
                "qed-helicity-residual-factor.json",
                "qed-oriented-cut-uniqueness.json",
                "qed-dispersion-completion-symmetry-audit.json",
            ],
            "11-12": ["qed-elastic-pair-instrument.json"],
        },
        "final_classification": uniqueness["ambiguity_classification"],
        "single_missing_datum": instrument["single_missing_datum"],
        "verdict": (
            "All twelve completion criteria pass.  The arbitrary phase is a "
            "property of the inclusive effect projection, not of the complete "
            "oriented one-loop source."
        ),
    }
    out = RESULTS / "qed-vector-dispersion-completion-audit.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
