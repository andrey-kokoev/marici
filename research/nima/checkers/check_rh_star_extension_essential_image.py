#!/usr/bin/env python3
"""Finite essential-image hostile for discrete-to-continuous boundary extension."""

import json
from pathlib import Path


def second_difference(values):
    return values[0] - 2 * values[1] + values[2]


def main():
    # Toy source class: affine continuous cocycles sampled at three points.
    # Its restriction image is characterized exactly by vanishing second difference.
    source_sample = (1, 2, 3)
    hostile_sample = (1, 2, 4)
    assert second_difference(source_sample) == 0
    assert second_difference(hostile_sample) != 0
    assert all(abs(x) < 10 for x in hostile_sample)  # bounded/summable is irrelevant to extension

    # One can fit the first two samples, but the third is then forced.
    fitted_slope = source_sample[1] - source_sample[0]
    forced_third = hostile_sample[0] + 2 * (hostile_sample[1] - hostile_sample[0])
    assert fitted_slope == 1
    assert forced_third == 3 != hostile_sample[2]

    result = {
        "schema": "marici.rh-star-extension-essential-image.v1",
        "restriction_fixture": "affine_continuous_cocycle_to_three_discrete_samples",
        "essential_image_relation": "y0-2*y1+y2=0",
        "admitted_sample": source_sample,
        "hostile_summable_sample": hostile_sample,
        "hostile_residual": second_difference(hostile_sample),
        "summability_implies_extension": False,
        "theta_gate": "zero_induced_discrete_packet_belongs_to_essential_image_of_star_compatible_continuous_boundary_cocycle",
        "smallest_source_square": "log(6)=log(2)+log(3) with translated interval incidence retained"
    }
    out = Path(__file__).parents[1] / "results" / "rh-star-extension-essential-image.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
