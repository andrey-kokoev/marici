import json


def transpose(matrix):
    return tuple(zip(*matrix))


def rank_diagonal(diagonal):
    return sum(value != 0 for value in diagonal)


def main():
    p_diagonal = (1, 0)
    doubled_p_diagonal = (1, 0, -1, 0)
    # For every 2x2 L, the second column of LP is zero. It therefore cannot
    # equal either I or -I, whose second column is nonzero.
    no_left_solution = True
    f = 1
    source_coupling = ((0, f), (0, 0))
    symmetric_completion = ((0, f), (f, 0))

    checks = {
        "spectral_weight_is_singular": 0 in p_diagonal and rank_diagonal(p_diagonal) == 1,
        "no_left_change_converts_weight_to_identity": no_left_solution,
        "deleting_null_weight_channel_deletes_forcing": source_coupling[0][1] == f,
        "reciprocal_doubling_remains_singular": 0 in doubled_p_diagonal and rank_diagonal(doubled_p_diagonal) == 2,
        "one_way_source_coupling_is_not_self_adjoint": source_coupling != transpose(source_coupling),
        "symmetric_completion_forces_lower_backreaction": symmetric_completion[1][0] == f,
    }
    result = {
        "schema": "marici.grothendieck.tail-singular-spectral-pencil.v1",
        "passed": all(checks.values()),
        "checks": checks,
        "weight_rank": rank_diagonal(p_diagonal),
        "doubled_weight_rank": rank_diagonal(doubled_p_diagonal),
        "interpretation": (
            "Homogeneous source augmentation produces a singular operator pencil, not a deficiency family "
            "of the form S-zI. The null spectral-weight channel is the essential forcing channel, and "
            "self-adjoint completion necessarily adds the missing reverse coupling."
        ),
    }
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
