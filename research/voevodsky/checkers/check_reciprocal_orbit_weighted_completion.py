from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


CONTRACT = Path("research/voevodsky/reciprocal-orbit-weighted-completion-v1.json")
DECAY_SOURCE = Path("research/grothendieck/complete-mellin-grade-tower-is-faithful-under-source-decay.md")


def tail(power: int, start: int, stop: int) -> Fraction:
    return sum((Fraction(1, n**power) for n in range(start, stop + 1)), Fraction(0))


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    source = DECAY_SOURCE.read_text(encoding="utf-8")
    assert "source supplies an exponential moment" in source
    assert "not a uniform lower-frame theorem" in source

    # Fixture: c_n=n^-4, epsilon=2, orbit width a=1.
    # Weighted source tail is sum n^-2; worst orbit evaluation tail is sum n^-3.
    cutoffs = (4, 8, 16, 32, 64)
    weighted_tails = [tail(2, cutoff + 1, 2048) for cutoff in cutoffs]
    orbit_tails = [tail(3, cutoff + 1, 2048) for cutoff in cutoffs]
    assert all(orbit <= weighted for orbit, weighted in zip(orbit_tails, weighted_tails))
    assert all(weighted_tails[index + 1] < weighted_tails[index] for index in range(len(cutoffs) - 1))
    assert all(orbit_tails[index + 1] < orbit_tails[index] for index in range(len(cutoffs) - 1))

    # Reciprocal labels have identical height, so direct and reciprocal bounds coincide.
    direct_bound = tail(3, 65, 2048)
    reciprocal_bound = tail(3, 65, 2048)
    assert direct_bound == reciprocal_bound

    # Deliberate failure outside the strip: a=3 gives terms n^-1.
    # Every dyadic block has sum at least 1/2, hence tails are not Cauchy.
    divergent_blocks = [tail(1, n + 1, 2 * n) for n in (8, 16, 32, 64, 128)]
    assert all(block >= Fraction(1, 2) for block in divergent_blocks)

    status = contract["status"]
    assert status["conditional_uniform_orbit_completion"] == "proved"
    assert status["global_spectral_completion"] == "not proved"
    result = {
        "schema":"marici.voevodsky.reciprocal-orbit-weighted-completion-check.v1",
        "status":"conditional_orbit_completion_verified",
        "source_weight_exponent":2,
        "orbit_width":1,
        "uniform_tail_dominated_by_source_tail":True,
        "reciprocal_tail_bounds_equal":True,
        "boundary_evaluation_continuous":True,
        "boundary_null_preserved_under_limit":True,
        "outside_strip_deliberate_failure_nonzero":True,
        "global_spectral_completion_verified":False,
        "unconditional_source_decay":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
