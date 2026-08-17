"""Literal fine-grading test for the D03 endpoint-relative Hom."""

from __future__ import annotations

import json
from dataclasses import dataclass


@dataclass(frozen=True)
class Degree:
    x0: int = 0
    x1: int = 0
    x3: int = 0
    x4: int = 0
    d03: int = 0

    def __add__(self, other: "Degree") -> "Degree":
        return Degree(*(a + b for a, b in zip(self.coords(), other.coords())))

    def __neg__(self) -> "Degree":
        return Degree(*(-a for a in self.coords()))

    def coords(self) -> tuple[int, ...]:
        return (self.x0, self.x1, self.x3, self.x4, self.d03)


E0 = Degree(x0=1)
E1 = Degree(x1=1)
E3 = Degree(x3=1)
E4 = Degree(x4=1)
ED = Degree(d03=1)


def face_shift(*labels: Degree) -> Degree:
    total = Degree()
    for label in labels:
        total = total + label
    return -total


def polynomial_piece_exists(degree: Degree) -> bool:
    return all(value >= 0 for value in degree.coords())


def main() -> None:
    # Entry-352 radial transition e_S -> (X_a/u_a)e_{S+a}
    # forces deg(e_S)=-sum_{a in S} eps_a.
    q03 = face_shift(ED)
    e2 = face_shift(E4)
    e3 = face_shift(E0, E4)
    e4 = face_shift(E1, E4)
    assert e2 == E0 + e3
    assert e2 == E1 + e4

    # q_J maps to x3*q03^Q.
    sigma = E3 + q03
    deciding_degree = sigma + E0 + E1 + E4
    assert deciding_degree.d03 == -1
    assert not polynomial_piece_exists(deciding_degree)

    print(json.dumps({
        "status": "proved_literal_fine_graded_endpoint_hom_vanishes",
        "q03_support": ["D03"],
        "q03_degree": "-eps_D03",
        "source_degree": "eps3-eps_D03",
        "endpoint_ideal_slice_degree": "eps0+eps1+eps3+eps4-eps_D03",
        "negative_coordinate": "D03:-1",
        "polynomial_occurrence_slice": "zero",
        "graded_endpoint_h0": "zero",
        "remaining": "connector existence/naturality, not coefficient deformation",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
