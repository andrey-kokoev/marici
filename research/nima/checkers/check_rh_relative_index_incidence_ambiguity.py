import json
from pathlib import Path


charge = (-1, 1)
same_orientation_incidence = (1, 1)
opposite_orientation_incidence = (-1, 1)


def integer_multiple(vector, generator):
    candidates = []
    for entry, base in zip(vector, generator):
        if base == 0:
            if entry != 0:
                return None
        else:
            if entry % base != 0:
                return None
            candidates.append(entry // base)
    if not candidates:
        return 0
    return candidates[0] if all(value == candidates[0] for value in candidates) else None


same_coefficient = integer_multiple(charge, same_orientation_incidence)
opposite_coefficient = integer_multiple(charge, opposite_orientation_incidence)

assert same_coefficient is None
assert opposite_coefficient == 1

result = {
    "sector_charge": charge,
    "same_orientation_incidence": same_orientation_incidence,
    "charge_is_boundary_under_same_orientation": False,
    "opposite_orientation_incidence": opposite_orientation_incidence,
    "charge_is_boundary_under_opposite_orientation": True,
    "both_abstract_cokernels": "Z",
    "labelled_charge_verdict_depends_on_incidence": True,
    "fitted_incidence_can_kill_any_primitive_charge": True,
    "verdict": "relative index is undefined until both ordered seam incidence maps are source-derived",
}

output = Path(__file__).parents[1] / "results" / "rh-relative-index-incidence-ambiguity.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))

