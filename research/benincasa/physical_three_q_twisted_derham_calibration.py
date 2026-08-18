"""Full three-denominator product-pole calibration at generic weight."""

from __future__ import annotations

import argparse
import json

from physical_single_q_twisted_derham_calibration import Q_POLYNOMIALS
from physical_top_twisted_derham_calibration import PRIME
from physical_two_q_twisted_derham_calibration import filtered_dimension


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--k-depth", type=int, default=2)
    parser.add_argument("--q-depth", type=int, default=2)
    parser.add_argument("--ambient", type=int, default=10)
    parser.add_argument("--cutoff", type=int, default=5)
    parser.add_argument("--gamma", type=int, default=5)
    arguments = parser.parse_args()
    names = ("g1", "g2", "G12")
    dimension = filtered_dimension(
        tuple(Q_POLYNOMIALS[name] for name in names),
        arguments.k_depth,
        arguments.q_depth,
        arguments.ambient,
        arguments.cutoff,
        arguments.gamma % PRIME,
    )
    print(
        json.dumps(
            {
                "schema": "marici.benincasa.physical_three_q_twisted_derham_calibration.v1",
                "prime": PRIME,
                "kinematics": [2, 3, 4],
                "denominators": names,
                "gamma": arguments.gamma,
                "k_depth": arguments.k_depth,
                "q_depth_each": arguments.q_depth,
                "ambient_degree": arguments.ambient,
                "cutoff_degree": arguments.cutoff,
                "deletion_closed_binary_pole_image_dimension": dimension,
                "expected_deletion_closed_rank": 21,
                "calibration_passed": dimension == 21,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
