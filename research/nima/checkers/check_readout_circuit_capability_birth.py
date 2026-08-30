from fractions import Fraction
import json
from pathlib import Path


def rank_q(rows):
    a = [[Fraction(x) for x in row] for row in rows]
    if not a:
        return 0
    m, n = len(a), len(a[0])
    r = 0
    for c in range(n):
        p = next((i for i in range(r, m) if a[i][c]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        pivot = a[r][c]
        a[r] = [x / pivot for x in a[r]]
        for i in range(m):
            if i != r and a[i][c]:
                f = a[i][c]
                a[i] = [x - f * y for x, y in zip(a[i], a[r])]
        r += 1
    return r


def rank_f2(rows):
    a = [[x & 1 for x in row] for row in rows]
    if not a:
        return 0
    m, n = len(a), len(a[0])
    r = 0
    for c in range(n):
        p = next((i for i in range(r, m) if a[i][c]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        for i in range(m):
            if i != r and a[i][c]:
                a[i] = [x ^ y for x, y in zip(a[i], a[r])]
        r += 1
    return r


def matvec(rows, vector, modulus=None):
    out = [sum(x * y for x, y in zip(row, vector)) for row in rows]
    return [x % modulus for x in out] if modulus else out


def column_pairs_independent(rows, rank):
    n = len(rows[0])
    for i in range(n):
        for j in range(i + 1, n):
            sub = [[row[i], row[j]] for row in rows]
            if rank(sub) != 2:
                return False
    return True


def in_span_f2(vector, generators):
    if not generators:
        return not any(vector)
    rows = [list(col) for col in zip(*generators)]
    augmented = [row + [v] for row, v in zip(rows, vector)]
    return rank_f2(rows) == rank_f2(augmented)


def main():
    # A preferred Pluecker chart dies although the complete readout is injective.
    chart_full = [[1, 0, 0], [0, 1, 0], [1, 1, 0], [0, 0, 1]]
    chart_preferred = chart_full[:3]
    chart_alternate = [chart_full[i] for i in (0, 1, 3)]

    magnetic = [[-6, 0, 3], [-8, -2, 1]]
    magnetic_circuit = [1, -3, 2]

    syndrome = [[1, 1, 0], [0, 1, 1]]
    syndrome_circuit = [1, 1, 1]
    contractible_repairs = [[1, 1, 1]]
    noncontractible_repairs = [[1, 1, 0]]

    # E(t) = [[1,0,1],[0,t,t]].  The maximal minors generate (t).
    family_generic = [[1, 0, 1], [0, 1, 1]]  # evaluate at any t != 0
    family_special = [[1, 0, 1], [0, 0, 0]]
    generic_relation = [-1, -1, 1]
    special_new_relation = [0, 1, 0]
    generic_nullity = 3 - rank_q(family_generic)
    special_nullity = 3 - rank_q(family_special)

    route_loss = [0, 0]
    destructive_interference = [5, -5]
    ordinary_transport = [5, 2]
    sum_readout = lambda pair: pair[0] + pair[1]

    gates = {
        "chart_failure_is_not_kernel_birth": (
            rank_q(chart_preferred) == 2
            and rank_q(chart_alternate) == 3
            and rank_q(chart_full) == 3
        ),
        "magnetic_three_to_two_circuit": (
            rank_q(magnetic) == 2
            and column_pairs_independent(magnetic, rank_q)
            and matvec(magnetic, magnetic_circuit) == [0, 0]
        ),
        "syndrome_three_to_two_circuit": (
            rank_f2(syndrome) == 2
            and column_pairs_independent(syndrome, rank_f2)
            and matvec(syndrome, syndrome_circuit, 2) == [0, 0]
        ),
        "repair_membership_changes_capability_not_syndrome": (
            in_span_f2(syndrome_circuit, contractible_repairs)
            and not in_span_f2(syndrome_circuit, noncontractible_repairs)
        ),
        "fitting_stratum_has_one_excess_relation": (
            rank_q(family_generic) == 2
            and rank_q(family_special) == 1
            and matvec(family_generic, generic_relation) == [0, 0]
            and matvec(family_special, generic_relation) == [0, 0]
            and matvec(family_special, special_new_relation) == [0, 0]
            and special_nullity - generic_nullity == 1
        ),
        "route_loss_and_interference_have_same_result_different_lifts": (
            sum_readout(route_loss) == 0
            and sum_readout(destructive_interference) == 0
            and route_loss == [0, 0]
            and destructive_interference != [0, 0]
            and sum_readout(ordinary_transport) != 0
        ),
    }
    assert all(gates.values()), gates

    result = {
        "schema": "marici.readout-circuit-capability-birth.v1",
        "gates": gates,
        "magnetic": {
            "rank": rank_q(magnetic),
            "circuit": magnetic_circuit,
            "all_pairs_independent": True,
        },
        "kitaev": {
            "rank": rank_f2(syndrome),
            "circuit": syndrome_circuit,
            "repair_case_survives": False,
            "logical_case_survives": True,
        },
        "family_specialization": {
            "maximal_minor_ideal_generator": "t",
            "generic_nullity": generic_nullity,
            "special_nullity": special_nullity,
            "new_relation_dimension": special_nullity - generic_nullity,
        },
        "route_pairing": {
            "route_loss_lift": route_loss,
            "interference_lift": destructive_interference,
            "displayed_result_for_both": 0,
            "pairing_kernel_dimension": 1,
            "residue_type": "nonzero route lift in kernel of sum pairing",
        },
        "conclusion": "capability birth equals a Fitting-supported circuit surviving repairs and generic relations",
    }
    out = Path(__file__).parents[1] / "results" / "readout-circuit-capability-birth.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
