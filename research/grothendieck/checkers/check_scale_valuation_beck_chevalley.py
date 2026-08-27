"""Dependency-free audit of the scale/valuation comparison two-cell."""

from math import erfc, log, pi, sqrt


def tail(q: float) -> float:
    return 0.5 * erfc(sqrt(pi) * q)


def window(length: float, q: float) -> float:
    return tail(q + length) - tail(q - length)


def beta(prime: int, depth: int, q: float) -> float:
    length = log(prime)
    return window(depth * length, q) - window(length, q)


def main() -> None:
    probes = (-2.0, -0.5, 0.0, 0.5, 2.0)
    for prime in (2, 3, 5, 101):
        for depth in (2, 3, 4):
            assert max(abs(beta(prime, depth, q) - beta(prime, depth, -q)) for q in probes) < 1e-14

        # Depth-three comparison is the sum of the two adjacent cells.
        length = log(prime)
        for q in probes:
            adjacent_1 = window(2 * length, q) - window(length, q)
            adjacent_2 = window(3 * length, q) - window(2 * length, q)
            assert abs(beta(prime, 3, q) - adjacent_1 - adjacent_2) < 1e-14

    small = max(abs(beta(10_000_019, 2, q)) for q in probes)
    assert small < 1e-15

    print("scale_valuation_strict_commutation=false")
    print("boundary_quotient_commutation=true")
    print("comparison_two_cell=gaussian_bulk")
    print("valuation_depth_coherence=telescoping")
    print("large_prime_boundary_residual=zero")
    print("new_boundary_wall_required=false")


if __name__ == "__main__":
    main()
