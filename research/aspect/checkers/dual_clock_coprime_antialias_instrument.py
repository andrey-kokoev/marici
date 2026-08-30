"""Exact dual-clock sampling and finite anti-alias range audit."""

import json
from math import gcd
from pathlib import Path


def record(frequency, rates):
    return tuple(frequency % rate for rate in rates)


def main():
    rates = (4, 5)
    period = 20
    one_clock_collision = record(1, (4,)) == record(5, (4,))
    dual_separation = record(1, rates) != record(5, rates)
    band_records = [record(f, rates) for f in range(period)]
    hostile_a, hostile_b = 1, 21

    checks = {
        "sampling_rates_are_coprime": gcd(*rates) == 1,
        "four_clock_reproduces_frequency_one_five_alias": one_clock_collision,
        "second_clock_separates_one_from_five": dual_separation,
        "joint_record_is_injective_on_declared_twenty_class_band": len(set(band_records)) == period,
        "joint_period_is_twenty": all(record(f, rates) == record(f + period, rates) for f in range(period)),
        "unrestricted_hostile_one_and_twenty_one_still_collide": record(hostile_a, rates) == record(hostile_b, rates),
        "hostile_frequencies_are_distinct_before_sampling": hostile_a != hostile_b,
        "finite_coprime_clocks_do_not_prove_unrestricted_reconstruction": True,
    }
    result = {
        "schema": "marici.aspect.dual_clock_coprime_antialias_instrument.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "exact_arithmetic": True,
        "strength": "finite sampling-quotient theorem",
        "checks": checks,
        "sample_rates": list(rates),
        "declared_faithful_band": list(range(period)),
        "resolved_hostile": {"frequencies": [1, 5], "records": [list(record(1, rates)), list(record(5, rates))]},
        "surviving_hostile": {"frequencies": [hostile_a, hostile_b], "shared_record": list(record(hostile_a, rates))},
        "typed_boundary": {
            "source": "integer frequency class restricted to a declared finite band",
            "constructor": "two independently calibrated coprime sampling clocks",
            "detector": "ordered pair of phase-increment residues modulo four and five",
            "hostile": "frequencies separated by the joint period twenty have identical records",
            "completion": "continuous frequency, jitter, finite observation time, bandlimit, and reconstruction kernel remain open",
        },
    }
    out = Path(__file__).parents[1] / "results" / "dual_clock_coprime_antialias_instrument.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if result["status"] != "pass": raise SystemExit(1)


if __name__ == "__main__": main()
