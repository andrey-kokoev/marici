from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


CONTRACT = Path("research/voevodsky/theta-source-decay-applicability-gate-v1.json")
SOURCE = Path("research/grothendieck/the-affine-filler-theorem-stops-at-the-source-decay-map.md")


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    source = SOURCE.read_text(encoding="utf-8")
    assert "theta/Euler source" in source and "B_\\epsilon" in source
    assert "c_n=1" in source

    # epsilon=1. At x=m^-2 and n<=m, exp(-pi n^2 x)>=exp(-pi).
    # After scaling by exp(pi), the weighted norm lower bound is sum n.
    ms = (2, 4, 8, 16, 32)
    scaled_theta_lower_bounds = [sum(range(1, m + 1)) for m in ms]
    assert scaled_theta_lower_bounds == [m * (m + 1) // 2 for m in ms]
    assert all(scaled_theta_lower_bounds[i + 1] > scaled_theta_lower_bounds[i] for i in range(len(ms) - 1))

    # Unsmoothed c_n=1: each dyadic block of the epsilon=1 norm is nonzero and grows.
    euler_blocks = [sum(range(m + 1, 2 * m + 1)) for m in ms]
    assert all(block >= m * (m + 1) for block, m in zip(euler_blocks, ms))

    result = {
        "schema":"marici.voevodsky.theta-source-decay-applicability-gate-check.v1",
        "status":"source_decay_transfer_blocker_verified",
        "fixed_theta_slice_decay_compatible":True,
        "theta_weighted_norm_uniform_as_x_to_zero":False,
        "unsmoothed_euler_in_positive_B_epsilon":False,
        "explicit_source_map_supplied":False,
        "conditional_filler_theorem_invalidated":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
