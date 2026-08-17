"""Check the occurrence grading of the D03 three-face source cell."""

from __future__ import annotations

import json
from dataclasses import dataclass


@dataclass(frozen=True)
class Degree:
    x0: int = 0
    x1: int = 0
    x3: int = 0
    x4: int = 0

    def __add__(self, other: "Degree") -> "Degree":
        return Degree(*(a + b for a, b in zip(self.as_tuple(), other.as_tuple())))

    def __sub__(self, other: "Degree") -> "Degree":
        return Degree(*(a - b for a, b in zip(self.as_tuple(), other.as_tuple())))

    def as_tuple(self) -> tuple[int, int, int, int]:
        return (self.x0, self.x1, self.x3, self.x4)


E0 = Degree(x0=1)
E1 = Degree(x1=1)
E3 = Degree(x3=1)
E4 = Degree(x4=1)


def main() -> None:
    # Normalize deg(p)=0 and leave deg(xi)=tau symbolic.  A deliberately
    # generic test vector confirms the translation-invariant identities.
    tau = Degree(x0=7, x1=-2, x3=4, x4=1)
    p = Degree()
    h3 = E3 + p
    xi = tau
    qj = E3 + xi
    hmorse = qj

    source_top = hmorse + p
    source_generic = qj + p
    source_endpoint = xi + h3
    assert source_top == source_generic == source_endpoint

    e2 = Degree(x4=-1)
    e3 = Degree(x0=-1, x4=-1)
    e4 = Degree(x1=-1, x4=-1)
    assert E0 + e3 == e2
    assert E1 + e4 == e2

    sigma = source_generic
    ideal_slice_degree = sigma + E0 + E1 + E4
    assert ideal_slice_degree - sigma == E0 + E1 + E4

    print(json.dumps({
        "status": "proved_one_common_shift_target_offset_open",
        "source_shift_count": 1,
        "source_degree_identity": [
            "deg((H_Morse)p)",
            "deg(q_J p)",
            "deg((d xi_tilde) h3)",
        ],
        "endpoint_h0": "(x0,x1), shifted",
        "deciding_slice": "R_{sigma+eps0+eps1+eps4} intersect (x0,x1)",
        "missing_datum": "relative occurrence degree of q03^Q versus the endpoint-road generators",
        "conclusion": (
            "The endpoint graded Hom is no longer underdetermined by three "
            "source shifts. One target-relative offset decides it."
        ),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
