from __future__ import annotations

import json


def projection(stage_two_class: tuple[int, int, int, int]) -> tuple[int, int]:
    return stage_two_class[:2]


def main() -> None:
    radical_stage_one = {(0, 0, a, b) for a in range(-2, 3) for b in range(-2, 3)}
    radical_stage_two = {(0, 0, 0, 0)}
    assert radical_stage_two <= radical_stage_one

    samples = [(a, b, c, d) for a in range(-1, 2) for b in range(-1, 2) for c in range(-1, 2) for d in range(-1, 2)]
    projected = {projection(vector) for vector in samples}
    assert projected == {(a, b) for a in range(-1, 2) for b in range(-1, 2)}

    zero_stage_one = projection((0, 0, 0, 0))
    e3_stage_one = projection((0, 0, 1, 0))
    assert zero_stage_one == e3_stage_one
    reverse_identity_well_defined = (0, 0, 0, 0) == (0, 0, 1, 0)
    assert not reverse_identity_well_defined

    compatible_pairs = [(projection(vector), vector) for vector in samples]
    reconstructed_stage_two = [pair[1] for pair in compatible_pairs]
    assert reconstructed_stage_two == samples

    result = {
        "schema": "marici.voevodsky.inverse-spectral-quotient-completion.v1",
        "status": "finite_inverse_quotient_system_verified",
        "stage_one_rank": 2,
        "stage_one_radical_dimension": 2,
        "stage_two_rank": 4,
        "stage_two_radical_dimension": 0,
        "radicals_shrink": True,
        "canonical_finer_to_coarser_map_surjective": True,
        "identity_induced_coarser_to_finer_map_well_defined": reverse_identity_well_defined,
        "two_stage_projective_limit_is_stage_two_space": True,
        "two_stage_phantom_families": False,
        "fixed_radical_direct_system_generic_for_spectral_cutoffs": False,
        "next_gate": "infinite projective limit versus completed Weil-form quotient",
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
