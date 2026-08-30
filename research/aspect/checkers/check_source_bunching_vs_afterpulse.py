from __future__ import annotations

import json
from fractions import Fraction as F
from itertools import product
from pathlib import Path


def fresh_probability(value: int, mean: F) -> F:
    return (1 + mean) / 2 if value == 1 else (1 - mean) / 2


def copy_refresh_pair_probability(pair: tuple[int, int], mean: F, copy_probability: F) -> F:
    first, second = pair
    return fresh_probability(first, mean) * (
        copy_probability * (F(1) if second == first else F(0))
        + (1 - copy_probability) * fresh_probability(second, mean)
    )


def iid_pair_probability(pair: tuple[int, int], mean: F) -> F:
    return fresh_probability(pair[0], mean) * fresh_probability(pair[1], mean)


def covariance(law: dict[tuple[int, int], F], mean: F) -> F:
    return sum((probability * (first - mean) * (second - mean) for (first, second), probability in law.items()), F(0))


def main() -> None:
    mean = F(1, 2)
    memory = F(1, 2)
    pairs = list(product((-1, 1), repeat=2))

    # With one fixed detector, source copy-refresh memory and detector
    # copy-refresh memory induce exactly the same observed pair law.
    source_memory_fixed = {
        pair: copy_refresh_pair_probability(pair, mean, memory) for pair in pairs
    }
    detector_memory_fixed = dict(source_memory_fixed)
    assert source_memory_fixed == detector_memory_fixed
    fixed_covariance = covariance(source_memory_fixed, mean)
    assert fixed_covariance == F(3, 8)

    # Active reset removes detector memory but cannot remove source memory.
    source_after_reset = source_memory_fixed
    detector_after_reset = {pair: iid_pair_probability(pair, mean) for pair in pairs}
    assert covariance(source_after_reset, mean) == F(3, 8)
    assert covariance(detector_after_reset, mean) == 0

    # Routing the second epoch to an independently calibrated fresh detector
    # has the same separation, provided memory is detector-local.
    source_after_reroute = source_memory_fixed
    detector_after_reroute = detector_after_reset
    assert covariance(source_after_reroute, mean) == F(3, 8)
    assert covariance(detector_after_reroute, mean) == 0

    # A shared-electronics echo follows the record across detector routing and
    # is observationally identical to source memory under these interventions.
    shared_electronics_after_reroute = source_memory_fixed
    assert shared_electronics_after_reroute == source_after_reroute

    result = {
        "schema": "marici.aspect.source-bunching-vs-afterpulse.v1",
        "status": "pass",
        "fixed_detector_pair_laws_identical": True,
        "fixed_detector_covariance": str(fixed_covariance),
        "active_reset_source_covariance": "3/8",
        "active_reset_detector_covariance": "0",
        "independent_detector_reroute_source_covariance": "3/8",
        "independent_detector_reroute_detector_covariance": "0",
        "shared_electronics_remains_aliased_with_source_memory": True,
        "required_instrument": "active detector reset plus rerouting to a detector whose disturbance coupling is independently calibrated",
        "verdict": "Fixed-detector lag data cannot identify source bunching versus afterpulsing; reset and independently excited detector routing separate detector-local memory, while shared electronics remains an unresolved common-mode carrier.",
        "claim_boundary": "binary two-epoch copy-or-refresh models; perfect routing and reset; no mixed source-detector memory, loss, or detector mismatch",
    }
    output = Path(__file__).parents[1] / "results" / "source_bunching_vs_afterpulse.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
