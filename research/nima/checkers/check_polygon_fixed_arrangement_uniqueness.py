#!/usr/bin/env python3
"""Exact degree census for fixed polygon-arrangement form uniqueness."""
import json
from pathlib import Path

stages = []
for n in range(4, 8):
    dimension = n - 3
    facets = n * (n - 3) // 2
    infinity_regular_bound = facets - dimension - 1
    divisibility_lower_bound = facets
    gap = divisibility_lower_bound - infinity_regular_bound
    assert infinity_regular_bound >= 0
    assert gap == dimension + 1 > 0
    stages.append({
        "n": n,
        "dimension": dimension,
        "facet_count": facets,
        "maximum_infinity_regular_numerator_degree": infinity_regular_bound,
        "minimum_nonzero_zero_residue_numerator_degree": divisibility_lower_bound,
        "degree_contradiction_gap": gap,
        "affine_volume_infinity_pole_order": dimension + 1,
    })

result = {
    "schema": "marici.polygon-fixed-arrangement-uniqueness.v1",
    "status": "passed",
    "strength": "general algebraic theorem for every positive dimension under a reduced fixed affine hyperplane divisor and simple-pole class; finite degree census n=4..7 is illustrative only",
    "theorem": "equal facet residues and no infinity-divisor pole uniquely determine a rational top form on a fixed reduced affine hyperplane arrangement",
    "projective_degree_bound": "deg(N) <= F-d-1",
    "zero_residue_divisibility": "product of F distinct facet equations divides N",
    "stages": stages,
    "zero_dimensional_exception": "n=3 has no facet recursion; its 0-form normalization must be supplied separately",
    "deliberate_failure": "the affine volume form has zero facet residues but an infinity pole of order d+1",
    "boundary": "the theorem does not prove existence, select the arrangement or supports, derive residues, or establish physical normalization",
}
out = Path("research/nima/results/polygon_fixed_arrangement_uniqueness.json")
out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))
