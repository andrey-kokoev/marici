"""Exact WP616 minimal U(1)_F anomaly map and inclusive-width probe."""

import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class WeylField:
    name: str
    d3: int
    d2: int
    t3: Fraction
    t2: Fraction
    hypercharge: Fraction
    flavor_charge: int


def family_fields(index: int, q: int, ell: int) -> tuple[WeylField, ...]:
    """One SM family plus a right-handed neutrino, in left-Weyl convention."""
    return (
        WeylField(f"Q{index}", 3, 2, Fraction(1, 2), Fraction(1, 2),
                  Fraction(1, 6), q),
        WeylField(f"u{index}c", 3, 1, Fraction(1, 2), Fraction(0),
                  Fraction(-2, 3), -q),
        WeylField(f"d{index}c", 3, 1, Fraction(1, 2), Fraction(0),
                  Fraction(1, 3), -q),
        WeylField(f"L{index}", 1, 2, Fraction(0), Fraction(1, 2),
                  Fraction(-1, 2), ell),
        WeylField(f"e{index}c", 1, 1, Fraction(0), Fraction(0),
                  Fraction(1), -ell),
        WeylField(f"N{index}c", 1, 1, Fraction(0), Fraction(0),
                  Fraction(0), -ell),
    )


def field_packet(
    quark_charges: tuple[int, int, int],
    lepton_charges: tuple[int, int, int],
) -> tuple[WeylField, ...]:
    return tuple(
        field
        for index, (q, ell) in enumerate(
            zip(quark_charges, lepton_charges), start=1
        )
        for field in family_fields(index, q, ell)
    )


def anomaly_packet(fields: tuple[WeylField, ...]) -> dict[str, Fraction]:
    return {
        "SU3^2-U1F": sum(
            (f.d2 * f.t3 * f.flavor_charge for f in fields), Fraction(0)
        ),
        "SU2^2-U1F": sum(
            (f.d3 * f.t2 * f.flavor_charge for f in fields), Fraction(0)
        ),
        "U1Y^2-U1F": sum(
            (f.d3 * f.d2 * f.hypercharge**2 * f.flavor_charge for f in fields),
            Fraction(0),
        ),
        "U1Y-U1F^2": sum(
            (f.d3 * f.d2 * f.hypercharge * f.flavor_charge**2 for f in fields),
            Fraction(0),
        ),
        "U1F^3": sum(
            (f.d3 * f.d2 * f.flavor_charge**3 for f in fields), Fraction(0)
        ),
        "gravity^2-U1F": sum(
            (f.d3 * f.d2 * f.flavor_charge for f in fields), Fraction(0)
        ),
    }


def exponent_matrix(charges: tuple[int, int, int]) -> list[list[int]]:
    return [[abs(left - right) for right in charges] for left in charges]


def inclusive_width_ratio(
    quark_charges: tuple[int, int, int],
    lepton_charges: tuple[int, int, int],
) -> Fraction:
    """Massless, fully open Z_F quark-to-lepton width ratio.

    Each quark family contributes two Dirac flavors and three colors; each
    lepton family contributes one charged and one neutral Dirac flavor.
    Common gauge coupling and line-shape normalization cancel in the ratio.
    """
    return Fraction(
        3 * sum(charge**2 for charge in quark_charges),
        sum(charge**2 for charge in lepton_charges),
    )


target_q = (3, 2, 0)
hostile_q = (4, 1, 0)
common_ell = (-5, -5, -5)
target_anomalies = anomaly_packet(field_packet(target_q, common_ell))
hostile_anomalies = anomaly_packet(field_packet(hostile_q, common_ell))
target_exponents = exponent_matrix(target_q)
hostile_exponents = exponent_matrix(hostile_q)
target_width_ratio = inclusive_width_ratio(target_q, common_ell)
hostile_width_ratio = inclusive_width_ratio(hostile_q, common_ell)

# The one nontrivial anomaly coordinate before imposing zero.
linear_target = sum(3 * q + ell for q, ell in zip(target_q, common_ell))
linear_hostile = sum(3 * q + ell for q, ell in zip(hostile_q, common_ell))

# Deliberate failure: perturb one lepton charge while keeping the quark packet.
broken_ell = (-4, -5, -5)
broken_anomalies = anomaly_packet(field_packet(target_q, broken_ell))
broken_residual = {
    key: value for key, value in broken_anomalies.items() if value != 0
}

checks = {
    "target_is_anomaly_free_in_fixed_field_content": all(
        value == 0 for value in target_anomalies.values()
    ),
    "hostile_is_anomaly_free_in_same_fixed_field_content": all(
        value == 0 for value in hostile_anomalies.values()
    ),
    "only_linear_sum_is_needed_for_both": linear_target == linear_hostile == 0,
    "hostile_has_distinct_charge_gap_geometry": target_exponents
    != hostile_exponents,
    "integer_lattice_does_not_remove_hostile_pair": all(
        isinstance(value, int) for value in target_q + hostile_q + common_ell
    ),
    "reflection_preserves_anomaly_free_zero_locus": all(
        value == 0
        for value in anomaly_packet(
            field_packet(
                tuple(-value for value in target_q),
                tuple(-value for value in common_ell),
            )
        ).values()
    ),
    "fixed_leptons_make_common_quark_translation_visible":
        sum(3 * (q + 1) + ell for q, ell in zip(target_q, common_ell)) == 9,
    "inclusive_width_probe_separates_hostile_pair":
        target_width_ratio == Fraction(13, 25)
        and hostile_width_ratio == Fraction(17, 25),
    "deleting_anomaly_balance_gives_nonzero_residual": bool(broken_residual),
}

if not all(checks.values()):
    raise SystemExit(f"WP616 check failed: {checks}")


def encode(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


result = {
    "work_package": "WP616",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "one gauged U(1)_F, a neutral Higgs, one charge-changing flavon, exactly three Standard Model families plus three right-handed neutrinos, no exotic chiral spectators",
    "charge_convention": "physical left- and right-handed members of each Dirac family have the same U(1)_F charge; all anomaly sums use left-handed Weyl conjugates",
    "source_authorized_probe_family": list(target_anomalies),
    "reduced_anomaly_coordinate": "sum_i(3 q_i + ell_i); SU2^2-U1F is one half of it and U1Y^2-U1F is minus one half of it; all other audited U1F anomalies cancel identically",
    "translation_response": "with lepton charges fixed, q_i -> q_i+c changes the reduced anomaly coordinate by 9c",
    "reflection_character": "simultaneous reversal of every U1F charge changes the linear anomaly sign and preserves its zero locus",
    "lattice_domain": "integral charges; both the target and hostile assignments survive",
    "target_quark_charges": list(target_q),
    "hostile_quark_charges": list(hostile_q),
    "common_lepton_charges": list(common_ell),
    "target_exponent_matrix": target_exponents,
    "hostile_exponent_matrix": hostile_exponents,
    "target_anomalies": {key: encode(value) for key, value in target_anomalies.items()},
    "hostile_anomalies": {key: encode(value) for key, value in hostile_anomalies.items()},
    "deliberate_failure_residual": {
        key: encode(value) for key, value in broken_residual.items()
    },
    "contextual_partition": "the anomaly-free fiber at fixed lepton charges contains every integral quark charge vector with sum five, including inequivalent hierarchy geometries",
    "classification": "minimal-spectrum anomaly cancellation fixes one origin-sensitive linear combination but is neither an orientation selector nor a charge-gap selector",
    "physical_probe": "if the U(1)_F gauge boson is produced above all fermion thresholds, the inclusive quark-to-lepton width ratio is 3 sum(q_i^2)/sum(ell_i^2)",
    "target_width_ratio": encode(target_width_ratio),
    "hostile_width_ratio": encode(hostile_width_ratio),
    "smallest_exact_falsifier": "the same fixed fermion content and lepton charges admit q=(3,2,0) and q=(4,1,0), while their exact inclusive width ratios are 13/25 and 17/25",
    "instrument_gate": "produce a resolved U(1)_F vector resonance, verify all relevant fermion channels are open, calibrate acceptance and invisible right-handed-neutrino width, and measure inclusive quark/lepton partial-width ratio in one line-shape fit",
    "remaining_source_gate": "derive an independent representation or index rule sensitive to charge-gap moments or orientation; the anomaly map only sees the charge sum",
}

out = ROOT / "results" / "wp616_minimal_u1f_anomaly_and_width_probe.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
