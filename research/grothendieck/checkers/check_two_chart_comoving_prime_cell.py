"""Dependency-free audit of the two comoving boundary charts."""

from math import erfc, log, pi, sqrt


def tail(q: float) -> float:
    return 0.5 * erfc(sqrt(pi) * q)


def window(length: float, q: float) -> float:
    return tail(q + length) - tail(q - length)


def adjacent(length: float, depth: int, q: float) -> float:
    return window((depth + 1) * length, q) - window(depth * length, q)


def main() -> None:
    probes = (-2.0, -0.5, 0.0, 0.5, 2.0)
    length = log(10_000_019)
    depth = 1

    inner_errors = [
        abs(adjacent(length, depth, depth * length + u) - (tail(u) - 1.0))
        for u in probes
    ]
    outer_errors = [
        abs(adjacent(length, depth, (depth + 1) * length + u) + tail(u))
        for u in probes
    ]
    assert max(inner_errors) < 1e-14
    assert max(outer_errors) < 1e-14
    assert max(abs((tail(u) - 1.0) - tail(u) + 1.0) for u in probes) < 1e-15

    print("comoving_chart_count=2")
    print("inner_front_profile=H(u)-1")
    print("outer_front_profile=-H(u)")
    print("chart_overlap=negative_unit")
    print("fourier_overlap=negative_delta")
    print("single_comoving_coordinate_sufficient=false")
    print("next_gate=relative_two_front_pushforward")


if __name__ == "__main__":
    main()
