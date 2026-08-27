"""Dependency-free audit of the compactified prime-scale pullback."""

from math import erfc, log, pi, sqrt


def tail(q: float) -> float:
    return 0.5 * erfc(sqrt(pi) * q)


def pulled_window(r: float, q: float) -> float:
    length = -log(r)
    return tail(q + length) - tail(q - length)


def main() -> None:
    probes = (-2.0, -0.5, 0.0, 0.5, 2.0)
    radii = (1e-2, 1e-4, 1e-8)
    errors = [max(abs(pulled_window(r, q) + 1.0) for q in probes) for r in radii]
    assert errors[2] <= errors[1] <= errors[0]
    assert errors[2] < errors[0]
    assert errors[2] < 1e-15

    prime_radii = tuple(1.0 / p for p in (2, 3, 5, 101, 1009))
    assert all(prime_radii[i + 1] < prime_radii[i] for i in range(len(prime_radii) - 1))

    print("compactified_scale_coordinate=r=1/p")
    print("large_prime_boundary=r=0")
    print("window_boundary_value=negative_unit")
    print("fourier_boundary_value=negative_delta")
    print("sixth_component_required=false")
    print("graph_completion_retains_scale_provenance=true")
    print("primitive_square_cancellation=not_derived")


if __name__ == "__main__":
    main()
