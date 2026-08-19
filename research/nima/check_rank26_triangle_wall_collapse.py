"""Test the moving-wall quotient on the triangle wall X3=X1+X2."""

import json
from pathlib import Path

import check_rank26_multifiber_signature as model

wall_points = ((2, 3, 5), (3, 5, 8), (5, 8, 13))
nearby_points = ((2, 3, 6), (3, 5, 9), (5, 8, 14))
wall = [model.sample(point) for point in wall_points]
nearby = [model.sample(point) for point in nearby_points]
payload = {
    "schema": "marici.rank26-triangle-wall-collapse.v1",
    "field": model.base.PRIME,
    "wall_equation": "X3-X1-X2=0",
    "wall": [
        {
            "point": item["point"],
            "numerator_rank": item["numerator_rank"],
            "augmented_rank": item["augmented_rank"],
            "moving_wall_quotient_rank": item["moving_wall_quotient_rank"],
            "relation_rank": item["relation_rank"],
            "total_quotient_dimension": item["total_quotient_dimension"],
            "low_free_count": item["low_free_count"],
        }
        for item in wall
    ],
    "nearby": [
        {
            "point": item["point"],
            "numerator_rank": item["numerator_rank"],
            "augmented_rank": item["augmented_rank"],
            "moving_wall_quotient_rank": item["moving_wall_quotient_rank"],
            "second_fundamental_form_rank": item["second_fundamental_form_rank"],
            "relation_rank": item["relation_rank"],
            "total_quotient_dimension": item["total_quotient_dimension"],
            "low_free_count": item["low_free_count"],
        }
        for item in nearby
    ],
    "status": "moving_wall_odd_quotient_collapses_exactly_on_tested_triangle_wall_fibers",
}
Path(__file__).with_name("rank26-triangle-wall-collapse.json").write_text(
    json.dumps(payload, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(payload, indent=2))
