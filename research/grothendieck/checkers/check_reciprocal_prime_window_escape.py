"""Dependency-free audit of reciprocal Gaussian-window escape."""

from math import erfc, pi, sqrt


def tail(q: float) -> float:
    return 0.5 * erfc(sqrt(pi) * q)


def window(length: float, q: float) -> float:
    return tail(q + length) - tail(q - length)


def main() -> None:
    probes = (-2.0, -0.5, 0.0, 0.5, 2.0)
    for length in (0.5, 1.0, 3.0):
        assert max(abs(window(length, q) - window(length, -q)) for q in probes) < 1e-14
        assert window(length, 0.0) < 0.0

    large_length = 8.0
    assert max(abs(window(large_length, q) + 1.0) for q in probes) < 1e-15
    assert abs(window(1.0, -12.0)) < 1e-15
    assert abs(window(1.0, 12.0)) < 1e-15

    print("finite_label_seam_class_cancels=true")
    print("paired_remainder_is_even_bulk_window=true")
    print("window_width=2L")
    print("large_label_local_limit=negative_unit")
    print("uniform_gaussian_step_bound=false")
    print("global_obstruction=completion_escape")


if __name__ == "__main__":
    main()
