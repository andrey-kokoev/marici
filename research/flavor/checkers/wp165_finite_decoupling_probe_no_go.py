"""Exact bounded witness for failure of uniform finite decoupling probes."""

from fractions import Fraction
import json
from pathlib import Path


probes = (
    {"coefficient": 1, "power": 2, "threshold": Fraction(1, 100)},
    {"coefficient": 3, "power": 4, "threshold": Fraction(1, 100)},
    {"coefficient": 5, "power": 6, "threshold": Fraction(1, 100)},
)


def response(probe: dict[str, object], mass: int) -> Fraction:
    return Fraction(int(probe["coefficient"]), mass ** int(probe["power"]))


def resolved(probe: dict[str, object], mass: int) -> bool:
    return response(probe, mass) >= probe["threshold"]


minimal_blind_mass = next(
    mass for mass in range(1, 1000)
    if all(not resolved(probe, mass) for probe in probes)
)

responses_at_10 = [response(probe, 10) for probe in probes]
responses_at_11 = [response(probe, 11) for probe in probes]

checks = {
    "probe_family_is_finite": len(probes) == 3,
    "all_powers_are_positive": all(int(probe["power"]) > 0 for probe in probes),
    "all_thresholds_are_positive": all(probe["threshold"] > 0 for probe in probes),
    "all_responses_are_positive_at_finite_mass": all(response(probe, 11) > 0 for probe in probes),
    "leading_probe_is_exactly_at_threshold_at_mass10": responses_at_10[0] == Fraction(1, 100),
    "at_least_one_probe_resolves_at_mass10": any(resolved(probe, 10) for probe in probes),
    "all_probes_are_unresolved_at_mass11": all(not resolved(probe, 11) for probe in probes),
    "minimal_integer_blind_mass_is_eleven": minimal_blind_mass == 11,
    "mass_dilation_preserves_formal_nonzero_responses": all(value > 0 for value in responses_at_11),
    "detector_maps_all_mass11_responses_to_zero": [int(resolved(probe, 11)) for probe in probes] == [0, 0, 0],
    "larger_masses_remain_blind": all(all(not resolved(probe, mass) for probe in probes) for mass in range(11, 101)),
    "finite_family_has_no_uniform_positive_margin": max(responses_at_11) < min(probe["threshold"] for probe in probes),
}

result = {
    "work_package": "WP165",
    "title": "Finite decoupling-probe uniform no-go",
    "domain": "unbounded positive protector mass M",
    "probe_family": [
        {
            "response": f"{probe['coefficient']}/M^{probe['power']}",
            "threshold": "1/100",
        }
        for probe in probes
    ],
    "minimal_integer_blind_mass": minimal_blind_mass,
    "responses_at_blind_mass": [str(value) for value in responses_at_11],
    "classification": "no finite positive-threshold decoupling family is uniformly faithful on an unbounded mass domain",
    "selector": False,
    "source_identification": "nonuniform",
    "physical_instrument": "finite detector family typed but uniformly insufficient",
    "smallest_exact_falsifier": "at M=11 all three formal responses are positive but each is below 1/100",
    "checks": checks,
    "passed": sum(checks.values()),
    "total": len(checks),
    "all_passed": all(checks.values()),
}

output = Path(__file__).resolve().parents[1] / "results" / "wp165_finite_decoupling_probe_no_go.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

