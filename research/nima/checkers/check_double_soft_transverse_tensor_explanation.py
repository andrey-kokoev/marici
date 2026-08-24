"""Explain the zero mixed Rees grade by transverse support and absent tensor."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
MARICI = ROOT.parents[1]


def main() -> None:
    closure = json.loads(
        (MARICI / "research" / "benincasa" / "double-soft-cospan-closure.json").read_text(
            encoding="utf-8"
        )
    )
    authority = json.loads(
        (ROOT / "results" / "c3-tate-square-physical-authority.json").read_text(
            encoding="utf-8"
        )
    )
    assert closure["double_soft_rees"]["presentation"] == ["1", "2*X1", "2*X2"]
    assert closure["double_soft_rees"]["mixed_grade_rank"] == 0
    assert authority["passing_carrier_product_count"] == 0

    # Bounded exact model of the tensorized resolution:
    # multiplication by x on Q[x] is injective, with one-dimensional cokernel.
    degree_reports = []
    for cutoff in range(1, 13):
        multiplication_x = sp.zeros(cutoff + 2, cutoff + 1)
        for degree in range(cutoff + 1):
            multiplication_x[degree + 1, degree] = 1
        kernel_dimension = len(multiplication_x.nullspace())
        cokernel_dimension = multiplication_x.rows - multiplication_x.rank()
        assert kernel_dimension == 0
        assert cokernel_dimension == 1
        degree_reports.append(
            {
                "cutoff": cutoff,
                "tor1_kernel_dimension": kernel_dimension,
                "tensor_cokernel_dimension": cokernel_dimension,
            }
        )

    result = {
        "status": "PASS",
        "rational_soft_module": "Q[x,y]/(x) direct_sum Q[x,y]/(y)",
        "fitting_determinant_factor": "x*y",
        "internal_mixed_generator_rank": 0,
        "derived_tensor_h0": "Q[x,y]/(x,y)",
        "derived_tensor_tor1": 0,
        "bounded_degree_reports": degree_reports,
        "physical_supported_tensor_admitted": False,
        "explanation": (
            "The two transverse unary support channels have a point intersection only after "
            "applying a binary tensor functor. Transversality supplies no excess Tor class, "
            "and the physical inventory admits no such tensor."
        ),
    }

    output = ROOT / "results" / "double-soft-transverse-tensor-explanation.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
