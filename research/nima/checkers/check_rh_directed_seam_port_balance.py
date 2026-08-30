import json
from pathlib import Path


cutoffs = [1, 2, 3, 5, 8, 13]
records = []
for forcing_dimension in cutoffs:
    raw_input_dimension = forcing_dimension + 1
    raw_output_dimension = forcing_dimension
    dimension_lower_bound = raw_input_dimension - raw_output_dimension
    rank_one_augmented_output = raw_output_dimension + 1
    full_rank_augmented_output = raw_output_dimension + raw_input_dimension

    assert dimension_lower_bound == 1
    assert rank_one_augmented_output == raw_input_dimension
    assert full_rank_augmented_output > raw_input_dimension

    records.append(
        {
            "forcing_dimension": forcing_dimension,
            "raw_input_dimension": raw_input_dimension,
            "raw_output_dimension": raw_output_dimension,
            "defect_dimension_lower_bound": dimension_lower_bound,
            "rank_one_augmented_output": rank_one_augmented_output,
            "full_rank_augmented_output": full_rank_augmented_output,
        }
    )

result = {
    "cutoffs_checked": len(cutoffs),
    "records": records,
    "raw_tail_node_has_square_port_signature": False,
    "dimension_deficit_lower_bound": 1,
    "dimension_deficit_determines_defect_rank": False,
    "defect_rank_may_grow_with_cutoff": True,
    "port_dimension_count_derives_seam_multiplicity": False,
    "tail_state_already_factors_passive_defect": True,
    "source_seam_trace_map_constructed": False,
    "verdict": "port squareness cannot derive the seam carrier; its trace map and Gramian require an independent source construction",
}

out = Path(__file__).parents[1] / "results" / "rh-directed-seam-port-balance.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
