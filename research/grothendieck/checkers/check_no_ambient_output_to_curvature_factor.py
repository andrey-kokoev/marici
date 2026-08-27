#!/usr/bin/env python3
"""Exact kernel obstruction to an ambient output-to-curvature factor."""


def main():
    state = (1, -1)
    scalar_output = state[0] + state[1]
    ward_packet = (state[0], state[0], state[1])
    ward_norm_squared = sum(value * value for value in ward_packet)

    assert scalar_output == 0
    assert ward_norm_squared == 3

    # If W=K L, every vector in ker L lies in ker W. This witness violates
    # that necessary condition. It also rules out ||Wc|| <= C |Lc|.
    print("state=in_scalar_kernel")
    print("state=outside_curvature_kernel")
    print("ambient_factorization=impossible")
    print("required_domain=dynamical_scalar_null_pullback")


if __name__ == "__main__":
    main()

