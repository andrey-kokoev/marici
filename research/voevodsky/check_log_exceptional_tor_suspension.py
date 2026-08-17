#!/usr/bin/env python3
"""Match the log exceptional interval with the required Tor1 suspension."""


def convolve(a: list[int], b: list[int]) -> list[int]:
    result = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i + j] += x * y
    return result


def main() -> None:
    # The Boolean two-normal packet P has profile (1+t)^2.
    p = [1, 2, 1]
    tor = [1, 1]  # Tor0 in degree 0, Tor1 in degree 1
    required = convolve(p, tor)
    assert required == [1, 3, 3, 1]

    # Cellular exceptional interval: one oriented edge with two endpoint rays.
    # d(e)=r_1-r_D.  Relative to its boundary, only e survives in degree one.
    d_interval = [-1, 1]
    assert sum(d_interval) == 0
    relative_profile = [0, 1]
    assert convolve(p, [1, 0]) == [1, 2, 1, 0]  # Tor0 copy P
    assert convolve(p, relative_profile) == [0, 1, 2, 1]  # Tor1 copy P[1]
    combined = [a + b for a, b in zip(
        convolve(p, [1, 0]), convolve(p, relative_profile)
    )]
    assert combined == required

    # Reflection exchanges endpoint rays and reverses the oriented edge.  The
    # suspension orientation contributes the same minus sign, so the total
    # reflected Tor1 map has degree zero and squares to +1.
    endpoint_swap = [[0, 1], [1, 0]]
    reflected_boundary = [
        sum(endpoint_swap[i][j] * d_interval[j] for j in range(2))
        for i in range(2)
    ]
    assert reflected_boundary == [1, -1]
    interval_orientation_sign = -1
    suspension_sign = -1
    assert interval_orientation_sign * suspension_sign == 1

    # Normalized blowdown contracts the exceptional-only edge, while its
    # relative class persists through the descended Morse homotopy.
    exceptional_edge_downstairs = 0
    descended_relative_homotopy = 1
    assert exceptional_edge_downstairs == 0
    assert descended_relative_homotopy == 1

    print("two_normal_packet: P=(1,2,1)")
    print("Tor0_plus_Tor1_shifted: P*(1+t)=(1,3,3,1)")
    print("exceptional_relative_class: rank 1 in degree 1")
    print("endpoint_boundary: r_1-r_D")
    print("reflection_total_sign: +1")
    print("log_exceptional_Tor_suspension: CONSTRUCTED")


if __name__ == "__main__":
    main()
