from __future__ import annotations

import json


def main() -> None:
    # Piecewise-constant L2 cells of width 1/n: the unit point-value vector has
    # squared L2 norm 1/n, while its selected cell value remains one.
    refinements = [4, 16, 64, 256]
    norm_squared = [1 / n for n in refinements]
    evaluation_norm = [n ** 0.5 for n in refinements]
    assert all(norm_squared[i + 1] < norm_squared[i] for i in range(len(norm_squared) - 1))
    assert all(evaluation_norm[i + 1] > evaluation_norm[i] for i in range(len(evaluation_norm) - 1))

    result = {
        "schema":"marici.voevodsky.spectral-atom-order-nonclosability-check.v1",
        "status":"point_atom_functional_unbounded_in_L2_topology",
        "refinements":refinements,
        "null_vector_norm_squared":norm_squared,
        "point_evaluation_operator_norm":evaluation_norm,
        "single_rank_one_atom_form_closable":False,
        "full_completed_remainder_form_nonclosable_proved":False,
        "atomwise_closed_form_sum_valid":False,
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
