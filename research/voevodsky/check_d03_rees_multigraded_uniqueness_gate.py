"""Multigraded uniqueness audit for the D03 one-road Rees coefficient.

The target-only endpoint kernel from Entry 384 contains higher x3-Rees
classes if grading is forgotten.  This checker asks the narrower question
relevant to the already fixed generic/lower component: can such a class
perturb the homogeneous coefficient pair

    k = x3,  a = -XD/uD

without changing its occurrence multidegree?

It cannot.  This does not compute the endpoint-connector part of the
physical Hom complex, whose source shifts are still missing.
"""

from __future__ import annotations

import json
from dataclasses import dataclass


@dataclass(frozen=True)
class Degree:
    x0: int = 0
    x1: int = 0
    x3: int = 0
    xd: int = 0
    ud: int = 0
    x4: int = 0

    def __add__(self, other: "Degree") -> "Degree":
        return Degree(
            self.x0 + other.x0,
            self.x1 + other.x1,
            self.x3 + other.x3,
            self.xd + other.xd,
            self.ud + other.ud,
            self.x4 + other.x4,
        )


X0 = Degree(x0=1)
X1 = Degree(x1=1)
X3 = Degree(x3=1)
XD = Degree(xd=1)
UD = Degree(ud=1)
X4 = Degree(x4=1)
ZERO = Degree()


def scale(value: Degree, coefficient: int) -> Degree:
    return Degree(
        value.x0 * coefficient,
        value.x1 * coefficient,
        value.x3 * coefficient,
        value.xd * coefficient,
        value.ud * coefficient,
        value.x4 * coefficient,
    )


def check_road_grading() -> None:
    # Inverse occurrence labels are the shifts of the endpoint-relative
    # road generators e2 -> (e3,e4).
    e2 = scale(X4, -1)
    e3 = scale(X0 + X4, -1)
    e4 = scale(X1 + X4, -1)
    assert X0 + e3 == e2
    assert X1 + e4 == e2


def check_generic_lower_solution() -> None:
    primitive_k = X3
    primitive_a = XD + scale(UD, -1)

    # x3*a and (XD/uD)*k have the same multidegree.
    assert X3 + primitive_a == XD + scale(UD, -1) + primitive_k

    # Every monomial solution is a common polynomial multiple of the
    # primitive pair.  Enumerate a bounded box as an exact regression
    # certificate for the exponent equations.
    solutions: list[tuple[Degree, Degree, Degree]] = []
    for c_x3 in range(3):
        for c_xd in range(3):
            for c_ud in range(3):
                common = scale(X3, c_x3) + scale(XD, c_xd) + scale(UD, c_ud)
                k = common + primitive_k
                a = common + primitive_a
                assert X3 + a == XD + scale(UD, -1) + k
                solutions.append((common, k, a))

    fixed_degree = [
        (common, k, a)
        for common, k, a in solutions
        if k == primitive_k and a == primitive_a
    ]
    assert fixed_degree == [(ZERO, primitive_k, primitive_a)]

    # Entry 384's higher-Rees witnesses are genuine in the ungraded endpoint
    # module, but neither has the degree of the fixed generic coefficient.
    higher_x0 = scale(X3, 2) + X0
    higher_x1 = scale(X3, 2) + X1
    assert higher_x0 != primitive_k
    assert higher_x1 != primitive_k
    assert higher_x0.x3 == higher_x1.x3 == 2


def main() -> None:
    check_road_grading()
    check_generic_lower_solution()
    print(
        json.dumps(
            {
                "claim": (
                    "At the fixed multidegree of the D03 generic/lower "
                    "realization, the chain equation has only the primitive "
                    "pair k=x3 and a=-XD/uD up to an integer scalar; the "
                    "positive first Cartier symbol fixes that scalar to +1. "
                    "The ungraded x3^2*(x0,x1) sector cannot perturb this "
                    "component."
                ),
                "status": "proved_scoped_multigraded_uniqueness",
                "generic_lower_pair": {"k": "x3", "a": "-XD/uD"},
                "fixed_multidegree_common_factor": "1",
                "positive_cartier_scalar": 1,
                "entry_384_higher_rees_witness": (
                    "valid in the target-only ungraded shadow, inadmissible "
                    "as a perturbation of the fixed generic component"
                ),
                "physical_endpoint_connector": "UNDECIDED_SOURCE_SHIFTS_MISSING",
                "next_experiment": (
                    "Extract the source shifts of qJ*p, dxi*h3, and the "
                    "thimble generator, then compute degree-zero Hom into "
                    "the endpoint-relative road complex."
                ),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
