import itertools
import json
from pathlib import Path


verified_dimensions = {}
for n in range(1, 9):
    checked = 0
    for vector in itertools.product((0, 1), repeat=n):
        if any(vector):
            assert sum(vector) > 0
            checked += 1
    verified_dimensions[str(n)] = checked

signed_witness = (1, -1, 0)
assert sum(signed_witness) == 0
assert signed_witness != (0, 0, 0)

result = {
    "schema": "marici.rh-cone-zero-reflection.v1",
    "cone": "nonnegative_orthant",
    "scalar_port": "ell(x)=sum_i x_i",
    "zero_reflecting_on_cone": True,
    "full_linear_span": True,
    "verified_nonzero_boolean_points_by_dimension": verified_dimensions,
    "signed_linear_hostile": list(signed_witness),
    "injective_on_linear_span": False,
    "correction": "rank_lower_bound_applies_to_linear_joint_injectivity_not_cone_zero_reflection",
    "live_gate": "source_derived_preserved_pointed_cone_with_endpoint_in_interior_dual",
}

out = Path(__file__).parents[1] / "results" / "rh-cone-zero-reflection.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
