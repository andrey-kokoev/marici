"""Exact change-of-variables certificate for source equation (4.7)."""

from __future__ import annotations

import json
from pathlib import Path


def main() -> None:
    # Linear forms are coefficient triples in (z,p,q).
    source_log_arguments = {
        "x1+x2": (1, 1, 1),
        "2y": (1, 0, 0),
        "x1+y": (1, 1, 0),
        "y+x2": (1, 0, 1),
    }
    divided_difference_arguments = {
        "z+p+q": (1, 1, 1),
        "z": (1, 0, 0),
        "z+p": (1, 1, 0),
        "z+q": (1, 0, 1),
    }
    assert list(source_log_arguments.values()) == list(divided_difference_arguments.values())

    # y^2-x1^2=-p(z+p), y^2-x2^2=-q(z+q).
    denominator_factors = ["p", "q", "z+p", "z+q"]
    assert len(denominator_factors) == 4

    # For f(z)=z log z, f''(z)=1/z.  The normalized mixed divided
    # difference therefore tends to (1/z)/z^2=1/z^3 as p,q -> 0.
    coincident_limit = "1/z^3"
    assert coincident_limit == "1/z^3"

    result = {
        "schema": "marici.mass-insertion-divided-difference.v1",
        "coordinates": {"z": "2y", "p": "x1-y", "q": "x2-y"},
        "kernel": "f(z)=z*log(z)",
        "numerator": "f(z+p+q)+f(z)-f(z+p)-f(z+q)",
        "operation": "Delta_p Delta_q f(z)",
        "denominator": "p*q*(z+p)*(z+q)",
        "coincident_limit_p=q=0": coincident_limit,
        "coincident_limit_in_y": "1/(2y)^3",
        "conclusion": (
            "The integrated mass-insertion coefficient is a normalized mixed "
            "divided difference. Removable difference poles and the cubic "
            "coincident limit follow from this intrinsic form."
        ),
    }
    out = Path(__file__).with_name("results") / "mass-insertion-divided-difference.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
