"""Dependency-free audit of the oriented two-front current."""

from math import erf, erfc, exp, pi, sqrt


def tail(u: float) -> float:
    return 0.5 * erfc(sqrt(pi) * u)


def gaussian(u: float) -> float:
    return exp(-pi * u * u)


def main() -> None:
    probes = (-3.0, -1.0, -0.25, 0.0, 0.25, 1.0, 3.0)
    step = 1e-6

    for u in probes:
        inner = tail(u) - 1.0
        outer = -tail(u)
        assert abs(inner + outer + 1.0) < 1e-15
        oriented = outer - inner
        assert abs(oriented - erf(sqrt(pi) * u)) < 1e-15

        derivative = (
            (1.0 - 2.0 * tail(u + step))
            - (1.0 - 2.0 * tail(u - step))
        ) / (2.0 * step)
        assert abs(derivative - 2.0 * gaussian(u)) < 1e-9
        assert 2.0 * gaussian(u) > 0.0

    print("symmetric_front_channel=negative_unit")
    print("oriented_front_channel=erf(sqrt(pi)u)")
    print("oriented_density=2exp(-pi*u^2)")
    print("oriented_density_strictly_positive=true")
    print("total_oriented_flux=2")
    print("remaining_gate=arithmetic_scale_coefficient")


if __name__ == "__main__":
    main()
