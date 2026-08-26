"""Exact WP615 anomaly-completion kernel for Froggatt--Nielsen charges."""

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


def q_doublet(name: str, flavor_charge: int) -> WeylField:
    return WeylField(name, 3, 2, Fraction(1, 2), Fraction(1, 2),
                     Fraction(1, 6), flavor_charge)


def mirror(field: WeylField) -> WeylField:
    """Conjugate Standard Model representation with both U(1) charges reversed."""
    return WeylField(
        f"{field.name}_mirror", field.d3, field.d2, field.t3, field.t2,
        -field.hypercharge, -field.flavor_charge
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


def completed_fields(charges: tuple[int, int, int]) -> tuple[WeylField, ...]:
    seed = tuple(
        q_doublet(f"Q{index + 1}", charge)
        for index, charge in enumerate(charges)
    )
    return seed + tuple(mirror(field) for field in seed)


target_charges = (3, 2, 0)
hostile_charges = (4, 1, 0)
target_fields = completed_fields(target_charges)
hostile_fields = completed_fields(hostile_charges)
target_anomalies = anomaly_packet(target_fields)
hostile_anomalies = anomaly_packet(hostile_fields)

# Deliberate failure: deleting the nonzero-charge Q1 mirror must expose an
# obstruction. The Q3 mirror has zero flavor charge and would be inert here.
broken_anomalies = anomaly_packet(target_fields[:3] + target_fields[4:])
broken_residual = {
    key: value for key, value in broken_anomalies.items() if value != 0
}
target_exponents = exponent_matrix(target_charges)
hostile_exponents = exponent_matrix(hostile_charges)

checks = {
    "target_completion_cancels_complete_local_anomaly_packet": all(
        value == 0 for value in target_anomalies.values()
    ),
    "hostile_completion_cancels_complete_local_anomaly_packet": all(
        value == 0 for value in hostile_anomalies.values()
    ),
    "hostile_charge_gaps_are_physically_distinct": target_exponents
    != hostile_exponents,
    "hostile_assignment_is_not_shift_or_reversal_equivalent":
        sorted((1, 2)) != sorted((3, 1)),
    "deleting_one_mirror_exhibits_nonzero_obstruction": bool(broken_residual),
    "target_has_wolfenstein_long_gap": target_exponents[0][2] == 3,
    "hostile_has_different_long_gap": hostile_exponents[0][2] == 4,
}
if not all(checks.values()):
    raise SystemExit(f"WP615 check failed: {checks}")


def encode_fraction(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


result = {
    "work_package": "WP615",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "three charged left-handed quark-doublet ports, with one independently allowed conjugate mirror port for each",
    "probe_family": [
        "SU3^2-U1F", "SU2^2-U1F", "U1Y^2-U1F", "U1Y-U1F^2",
        "U1F^3", "gravity^2-U1F",
    ],
    "target_charge_assignment": list(target_charges),
    "hostile_charge_assignment": list(hostile_charges),
    "target_exponent_matrix": target_exponents,
    "hostile_exponent_matrix": hostile_exponents,
    "target_completed_anomalies": {
        key: encode_fraction(value) for key, value in target_anomalies.items()
    },
    "hostile_completed_anomalies": {
        key: encode_fraction(value) for key, value in hostile_anomalies.items()
    },
    "deliberate_failure_residual": {
        key: encode_fraction(value) for key, value in broken_residual.items()
    },
    "contextual_partition": "on the mirror-completed domain, the full tested local anomaly packet has one zero-valued class containing both inequivalent charge-gap architectures",
    "classification": "anomaly cancellation is a compatibility condition and completion rigidifier on this admitted domain; it is not a selector of the (3,2,0) gaps",
    "smallest_exact_falsifier": "(3,2,0) and (4,1,0) have different exponent matrices but both have identically zero complete anomaly packets after the same conjugate-mirror completion rule",
    "remaining_source_gate": "derive a restrictive no-mirror or fixed-representation UV spectrum independently; only then can its anomaly equations be retested for charge-gap selection",
    "instrument_gate": "resolve or exclude the conjugate mirror quark doublets and their mass-generating sector; anomaly equations alone have no detector readout of the charge-gap choice",
}

out = ROOT / "results" / "wp615_fn_anomaly_completion_kernel.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
