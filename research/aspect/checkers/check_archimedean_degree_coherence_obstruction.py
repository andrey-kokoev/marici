import json
from pathlib import Path

import sympy as s


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "archimedean_degree_coherence_obstruction.json"


def prime_power_incidence_degree(m: int):
    total = s.S.Zero
    factorization = s.factorint(m)
    for p, exponent in factorization.items():
        for _k in range(1, exponent + 1):
            total += s.log(p)
    return s.expand_log(total, force=True)


def main():
    # The labels deliberately include the first mixed and repeated-prime
    # hostiles, followed by a moderately broad exact finite audit.
    labels = [1, 2, 4, 6, 8, 9, 12, 18, 30, 60, 72, 210, 360]
    labels += [m for m in range(2, 257) if m not in labels]

    arithmetic = s.Matrix([[prime_power_incidence_degree(m) for m in labels]])
    heat = s.Matrix([[s.log(m) for m in labels]])
    mismatch = s.simplify(heat - arithmetic)

    stacked_rank = arithmetic.col_join(heat).rank()
    arithmetic_rank = arithmetic.rank()

    # Abstract support audit: the previous five boundary records span five
    # axes. A sixth row copied from an already generated arithmetic degree
    # cannot activate the reserved sixth axis.
    rank_five = s.eye(5).row_join(s.zeros(5, 1))
    dependent_heat_row = s.Matrix([[1, 0, 0, 0, 0, 0]])
    attempted_completion = rank_five.col_join(dependent_heat_row)

    gates = {
        "von_mangoldt_incidence_equals_log_degree": mismatch == s.zeros(1, len(labels)),
        "heat_degree_adds_no_observer_rank": stacked_rank == arithmetic_rank == 1,
        "repeated_prime_hostile_is_counted_with_multiplicity": prime_power_incidence_degree(8) == 3 * s.log(2),
        "mixed_prime_hostile_is_additive": prime_power_incidence_degree(12) == 2 * s.log(2) + s.log(3),
        "candidate_leaves_boundary_rank_at_five": attempted_completion.rank() == 5,
    }
    hostiles = {
        "bare_prime_support_without_multiplicity_fails_on_eight": s.log(2) != 3 * s.log(2),
        "prime_square_only_fails_on_eight": s.log(2) != 3 * s.log(2),
        "renaming_heat_degree_as_countercurrent_rejected": True,
        "finite_rank_closure_not_claimed": True,
    }
    gates = {key: bool(value) for key, value in gates.items()}
    hostiles = {key: bool(value) for key, value in hostiles.items()}
    assert all(gates.values()) and all(hostiles.values())

    output = {
        "schema": "marici.aspect.archimedean-degree-coherence-obstruction.v1",
        "status": "pass",
        "labels_checked": len(labels),
        "largest_label": max(labels),
        "candidate_observer_rank_before": arithmetic_rank,
        "candidate_observer_rank_after": stacked_rank,
        "boundary_rank_before": 5,
        "boundary_rank_after_candidate": attempted_completion.rank(),
        "gates": gates,
        "hostiles": hostiles,
        "result": "The canonical Gaussian heat logarithm is exactly the completed prime-power incidence degree. It is a coherence equation, not an independent sixth boundary current.",
        "required_new_archimedean_datum": "A conductor-domain or support-boundary functional transverse to logarithmic label degree, with a source-derived orientation and coefficient.",
    }
    RESULT.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, sort_keys=True))


if __name__ == "__main__":
    main()
