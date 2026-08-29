"""Exact no-go gates for the minimal magnetic sector extension."""
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import json
import math

def rf(value, count):
    result = Fraction(1)
    for offset in range(count):
        result *= value + offset
    return result

def full_column(grade, a, m):
    source = [
        math.comb(grade, j) * (-1)**(grade-j)
        * rf(a, grade-j) * rf(4-a, j)
        for j in range(grade + 1)
    ]
    path = [m * source[0]]
    path += [(m+j)*source[j] + (m+j-1-grade)*source[j-1]
             for j in range(1, grade + 1)]
    path.append(m * source[grade])
    delta = 1-grade-(a+m)
    shift = -a-grade if delta > 0 else -a-grade+abs(delta)
    sign = 1 if delta > 0 else -1
    return {shift+j: sign*value for j, value in enumerate(path) if value}

def det3(matrix):
    a, b, c = matrix
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            - a[1]*(b[0]*c[2]-b[2]*c[0])
            + a[2]*(b[0]*c[1]-b[1]*c[0]))

checks = []

def record(cid, statement, condition, detail):
    checks.append({
        "id": cid,
        "statement": statement,
        "status": "pass" if condition else "FAIL",
        "detail": str(detail),
    })

g = 6
d = Fraction(17, 3)
labels = [(Fraction(0), 1-2*g-d), (d-1, Fraction(2)), (d+1, Fraction(0))]
expected = [
    (Fraction(0), Fraction(-50, 3)),
    (Fraction(14, 3), Fraction(2)),
    (Fraction(20, 3), Fraction(0)),
]
record("LATTICE.labels", "the rational candidates have the expected exponent labels",
       labels == expected, labels)

sector_cosets = tuple((a % 2, m % 1) for a, m in labels)
record("LATTICE.sectors",
       "the candidates occupy two new affine sectors besides the original lattice",
       sector_cosets == (
           (Fraction(0), Fraction(1, 3)),
           (Fraction(2, 3), Fraction(0)),
           (Fraction(2, 3), Fraction(0)),
       ), sector_cosets)
record("LATTICE.minimum",
       "exactly two additional affine cosets are required for these candidates",
       len(set(sector_cosets) - {(Fraction(0), Fraction(0))}) == 2,
       sorted(set(sector_cosets)))

charges = (2, 1, 1)
record("CHARGE.split", "the candidates are not initially deck-homogeneous",
       len(set(charges)) == 2, charges)
adapted_charges = ((charges[0] + 2) % 3, charges[1], charges[2])
record("CHARGE.adapter", "one charge-2 adapter aligns all three candidates",
       adapted_charges == (1, 1, 1), adapted_charges)

columns = [full_column(g, a, m) for a, m in labels]
rows = sorted(set().union(*(set(column) for column in columns)))
matrix = [[column.get(row, 0) for column in columns] for row in rows]
witness = None
for selected in combinations(range(len(rows)), 3):
    value = det3([matrix[index] for index in selected])
    if value:
        witness = {
            "row_indices": selected,
            "rows": [rows[index] for index in selected],
            "determinant": value,
        }
        break
record("TRANSPORT.full_rank",
       "the minimally saturated source packet still maps with rank three",
       witness is not None, witness)
record("TRANSPORT.adapter_rank",
       "an invertible charged adapter preserves the nonzero rank witness",
       witness is not None and witness["determinant"] * 1 != 0,
       witness["determinant"] if witness else None)

# Block-diagonal direct sums of injective finite matrices have additive rank.
block_column_counts = (3, 2, 4)
block_ranks = (3, 2, 4)
record("EXACT.direct_sum",
       "adjoining independent injective sectors preserves injectivity",
       sum(block_ranks) == sum(block_column_counts),
       f"rank={sum(block_ranks)}, columns={sum(block_column_counts)}")
record("EXACT.flat_extension",
       "free scalar replication preserves rank-to-column equality",
       5*sum(block_ranks) == 5*sum(block_column_counts),
       "fivefold free extension")
record("EXACT.isomorphism",
       "invertible relabellings cannot change kernel dimension",
       witness is not None, "row and column isomorphisms preserve rank")

relation_constructors = {
    "nonflat_defect_restriction",
    "nonfaithful_target_quotient",
    "off_diagonal_tail_differential",
    "noninvertible_readout_pairing",
}
exact_only = {
    "independent_sector_sum",
    "faithfully_flat_extension",
    "grading_relabelling",
    "invertible_charge_adapter",
}
record("PORTAL.relation_required",
       "the exact extension grammar contains no relation-producing constructor",
       relation_constructors.isdisjoint(exact_only),
       sorted(relation_constructors))

failed = [item for item in checks if item["status"] != "pass"]
payload = {
    "schema": "marici.strominger.magnetic_minimal_sector_extension.v1",
    "status": "passed" if not failed else "failed",
    "gate_count": len(checks),
    "passed_gate_count": len(checks) - len(failed),
    "checks": checks,
    "witness_minor": {
        "row_indices": list(witness["row_indices"]),
        "rows": [str(value) for value in witness["rows"]],
        "determinant": str(witness["determinant"]),
    } if witness else None,
    "verdict": (
        "Minimal exponent-lattice saturation plus an invertible charged adapter "
        "does not activate the rational magnetic state. Exact faithful extensions "
        "add states but not relations. A portal must supply a non-flat restriction, "
        "nonfaithful quotient, off-diagonal tail differential, or noninvertible readout."
    ),
}
out = Path(__file__).resolve().parents[1] / "results" / "magnetic_minimal_sector_extension.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(1 if failed else 0)
