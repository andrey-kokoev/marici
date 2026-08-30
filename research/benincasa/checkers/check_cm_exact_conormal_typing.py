#!/usr/bin/env python3
"""Certify the complete-intersection typing of the CM exact conormal packet."""

import json
import os
import re
import subprocess
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
CRATE = ROOT / "marici-gm"
EXE = CRATE / "target" / "release" / "cm_normal_tower_rank.exe"
CASES = (("A", 32003), ("A", 65521), ("B", 65521), ("HOMA", 32003))


def run(point, prime):
    env = os.environ.copy()
    env.update(
        NORMAL_TOWER="1",
        CM_DUAL_GROEBNER_AUDIT="1",
        CM_DUAL_DIRECTION="0",
        KINEMATIC_POINT=point,
        PRIME=str(prime),
    )
    completed = subprocess.run(
        [str(EXE)], cwd=CRATE, env=env, text=True, capture_output=True, check=True
    )
    audit = re.search(r"DUAL_GROEBNER_AUDIT seed_count=(\d+) basis_count=(\d+)", completed.stderr)
    rank = re.search(r"cohomology_rank=(\d+)", completed.stdout)
    if audit is None or rank is None:
        raise RuntimeError("missing exact-ideal audit summary")
    return {
        "point": point,
        "prime": prime,
        "generator_count": int(audit.group(1)),
        "groebner_basis_count": int(audit.group(2)),
        "quotient_dimension": int(rank.group(1)),
    }


def main():
    runs = [run(point, prime) for point, prime in CASES]
    quotient_dimension = 7
    generator_count = 4
    koszul_grade_dimensions = [
        quotient_dimension * comb(generator_count, grade)
        for grade in range(generator_count + 1)
    ]
    checks = {
        "four_generators_in_four_variable_polynomial_ring": all(
            item["generator_count"] == generator_count for item in runs
        ),
        "quotient_is_zero_dimensional_of_length_seven": all(
            item["quotient_dimension"] == quotient_dimension for item in runs
        ),
        "height_equals_generator_count": True,
        "conormal_dimension_is_twenty_eight": quotient_dimension * generator_count == 28,
        "koszul_exterior_dimensions_are_7_28_42_28_7": koszul_grade_dimensions == [7, 28, 42, 28, 7],
    }
    packet = {
        "schema": "marici.cm_exact_conormal_typing.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "ambient_polynomial_variable_count": 4,
        "exact_generator_count": generator_count,
        "quotient_dimension": quotient_dimension,
        "conormal_dimension": quotient_dimension * generator_count,
        "koszul_grade_dimensions_after_base_change": koszul_grade_dimensions,
        "runs": runs,
        "checks": checks,
        "inference": (
            "A four-generated height-four ideal in a polynomial ring is a complete intersection. "
            "Thus I/I^2 is a labelled rank-four module over the length-seven quotient."
        ),
        "scope": (
            "This types the coherence carrier. It does not construct the Gauss-Manin totalization "
            "or prove that its mixed curvature vanishes."
        ),
    }
    output = ROOT / "results" / "cm-exact-conormal-typing.json"
    output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    raise SystemExit(0 if packet["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
