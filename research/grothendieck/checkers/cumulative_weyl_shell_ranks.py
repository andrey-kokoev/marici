"""Finite audit of cumulative versus local Weyl-rank rounding."""

import math


def smooth_count(t: int, constant: float = 7 / 8) -> float:
    return t / (2 * math.pi) * math.log(t / (2 * math.pi)) - t / (2 * math.pi) + constant


start = 100
stop = 100_000
cumulative = [math.floor(smooth_count(k + 1)) - math.floor(smooth_count(k)) for k in range(start, stop)]
assert min(cumulative) >= 0
telescoped = sum(cumulative)
exact_difference = math.floor(smooth_count(stop)) - math.floor(smooth_count(start))
assert telescoped == exact_difference

local = [math.floor(math.log(k / (2 * math.pi)) / (2 * math.pi)) for k in range(start, stop)]
local_error = sum(local) - (smooth_count(stop) - smooth_count(start))
cumulative_error = telescoped - (smooth_count(stop) - smooth_count(start))
assert abs(cumulative_error) < 1
assert abs(local_error) > 1000

result = {
    "cumulative_ranks_nonnegative_on_test_range": True,
    "telescoping_identity_exact": True,
    "cumulative_count_error_less_than_one": True,
    "independent_floor_error_is_macroscopic": True,
    "tested_shells": stop - start,
    "constant_term_still_requires_source_boundary_derivation": True,
}

if __name__ == "__main__":
    import json
    from pathlib import Path

    output = Path(__file__).parents[1] / "results" / "cumulative-weyl-shell-ranks.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")

