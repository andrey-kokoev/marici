"""Directed interval certificate for the sharp unit-slope limiting critical point."""

from __future__ import annotations

from decimal import Decimal
from math import comb

from theta_inner_interval_certificate import I, scale


def product(left: list[I], right: list[I]) -> list[I]:
    order = len(left) - 1
    return [
        sum((scale(left[k] * right[n-k], comb(n, k)) for k in range(n + 1)), I.point(0))
        for n in range(order + 1)
    ]


def add(*jets: list[I]) -> list[I]:
    return [sum((jet[n] for jet in jets), I.point(0)) for n in range(len(jets[0]))]


def jet_scale(jet: list[I], scalar: int | str) -> list[I]:
    return [scale(value, scalar) for value in jet]


def function_jet(x: I) -> list[I]:
    order = 2
    exponential = scale(x, 2).exp()
    t0 = (exponential - I.point(1)) / (exponential + I.point(1))
    s0 = I.point(1) - t0.power(2)
    t = [t0, s0, -scale(t0 * s0, 2)]
    xj = [x, I.point(1), I.point(0)]
    one = [I.point(1), I.point(0), I.point(0)]
    t2 = product(t, t)
    s = add(one, jet_scale(t2, -1))
    s2 = product(s, s)
    first = product(t2, s)
    second = jet_scale(product(product(product(xj, t), s2), one), -2)
    third_factor = add(one, jet_scale(t2, 3))
    third = product(product(product(xj, xj), third_factor), s2)
    return add(first, second, third)


def main() -> None:
    left = Decimal("1.0532")
    right = Decimal("1.0533")
    left_derivative = function_jet(I.point(left))[1]
    right_derivative = function_jet(I.point(right))[1]
    cells = 128
    second_cells = []
    for index in range(cells):
        cell_left = left + (right-left) * Decimal(index) / Decimal(cells)
        cell_right = left + (right-left) * Decimal(index+1) / Decimal(cells)
        second_cells.append(function_jet(I(cell_left, cell_right))[2])
    cell_second = I(min(value.lo for value in second_cells), max(value.hi for value in second_cells))
    curvature = -cell_second / I.point(4)
    print(f"f_prime_left={left_derivative}")
    print(f"f_prime_right={right_derivative}")
    print(f"f_second_cell={cell_second}")
    print(f"normalized_curvature_cell={curvature}")
    certified = left_derivative.lo > 0 and right_derivative.hi < 0 and cell_second.hi < 0 and curvature.lo > Decimal("0.59")
    print(f"certified={certified}")


if __name__ == "__main__":
    main()
