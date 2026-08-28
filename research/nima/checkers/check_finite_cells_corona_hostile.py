import json


cutoffs = [1, 2, 4, 8]
inspection_width = 16
constant = [1] * inspection_width
records = []

for cutoff in cutoffs:
    prefix = [1 if index < cutoff else 0 for index in range(inspection_width)]
    finite_support = all(value == 0 for value in prefix[cutoff:])
    sup_distance_on_tail = max(abs(a - b) for a, b in zip(constant, prefix))

    assert finite_support
    assert sup_distance_on_tail == 1

    records.append(
        {
            "cutoff": cutoff,
            "prefix": prefix,
            "finite_stage_corona_class": 0,
            "sup_distance_to_constant_limit": sup_distance_on_tail,
        }
    )

# Every fixed coordinate is eventually one as cutoff increases without bound.
tested_coordinates = [0, 1, 3, 7]
eventual_thresholds = [coordinate + 1 for coordinate in tested_coordinates]
assert all(threshold <= 8 for threshold in eventual_thresholds)

result = {
    "schema": "marici.nima.finite-cells-corona-hostile.v1",
    "records": records,
    "each_finite_stage_corona_class_zero": True,
    "coordinatewise_limit_is_constant_one": True,
    "completed_limit_corona_norm": 1,
    "uniform_convergence": False,
    "finite_comparison_cells_determine_completed_cell": False,
    "required_gate": "uniform_beck_chevalley_at_completion",
}
print(json.dumps(result, indent=2, sort_keys=True))

