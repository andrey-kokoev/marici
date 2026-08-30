"""Exact minimal-rank portal sewing and selector-torsor calculation."""
from fractions import Fraction
from pathlib import Path
import itertools
import json
import math

def rf(value, count):
    result = Fraction(1)
    for offset in range(count):
        result *= value + offset
    return result

def source(g, a, j):
    return (math.comb(g, j) * (-1)**j
            * rf(a, g-j) * rf(4-a, j))

def path(g, a, m, j):
    if j == 0:
        return m * source(g, a, 0)
    return ((m+j)*source(g, a, j)
            + (m+j-1-g)*source(g, a, j-1))

def odd_core(g, d):
    F = rf(4, g)
    m_minus = 1-2*g-d
    return [
        [m_minus*F, -path(g, d-1, 2, 0), -path(g, d+1, 0, 2)],
        [0, -path(g, d-1, 2, 1), -path(g, d+1, 0, 3)],
        [(1-g-d)*F, 0, -path(g, d+1, 0, 1)],
    ]

def full_column(g, a, m):
    values = [
        math.comb(g, j) * (-1)**(g-j)
        * rf(a, g-j) * rf(4-a, j)
        for j in range(g+1)
    ]
    output = [m*values[0]]
    output += [
        (m+j)*values[j] + (m+j-1-g)*values[j-1]
        for j in range(1, g+1)
    ]
    output.append(m*values[g])
    delta = 1-g-(a+m)
    shift = -a-g if delta > 0 else -a-g+abs(delta)
    sign = 1 if delta > 0 else -1
    return {shift+j: sign*value for j, value in enumerate(output) if value}

def matvec(matrix, vector):
    return [
        sum(Fraction(value)*Fraction(coefficient)
            for value, coefficient in zip(row, vector))
        for row in matrix
    ]

def rank(matrix):
    if not matrix:
        return 0
    work = [[Fraction(value) for value in row] for row in matrix]
    row = 0
    for column in range(len(work[0])):
        pivot = next((index for index in range(row, len(work))
                      if work[index][column]), None)
        if pivot is None:
            continue
        work[row], work[pivot] = work[pivot], work[row]
        scale = work[row][column]
        work[row] = [value/scale for value in work[row]]
        for index in range(len(work)):
            if index == row:
                continue
            factor = work[index][column]
            if factor:
                work[index] = [
                    left-factor*right
                    for left, right in zip(work[index], work[row])
                ]
        row += 1
    return row

def primitive(vector):
    denominators = [value.denominator for value in vector]
    common = 1
    for value in denominators:
        common = math.lcm(common, value)
    integers = [int(value*common) for value in vector]
    divisor = 0
    for value in integers:
        divisor = math.gcd(divisor, abs(value))
    integers = [value//divisor for value in integers]
    first = next(value for value in integers if value)
    if first < 0:
        integers = [-value for value in integers]
    return tuple(integers)

def cross(left, right):
    return [
        left[1]*right[2]-left[2]*right[1],
        left[2]*right[0]-left[0]*right[2],
        left[0]*right[1]-left[1]*right[0],
    ]

checks = []

def record(cid, statement, condition, detail):
    checks.append({
        "id": cid,
        "statement": statement,
        "status": "pass" if condition else "FAIL",
        "detail": str(detail),
    })

g, d = 6, Fraction(17, 3)
E = odd_core(g, d)
v = primitive([Fraction(value) for value in cross(E[0], E[1])])
record("CORE.rank", "the continued odd collision core has rank two", rank(E) == 2, E)
record("CORE.null", "the primitive residual direction spans the core kernel",
       matvec(E, v) == [0, 0, 0], v)

labels = [(0, 1-2*g-d), (d-1, 2), (d+1, 0)]
columns = [full_column(g, a, m) for a, m in labels]
rows = sorted(set().union(*(set(column) for column in columns)))
F = [[column.get(row, 0) for column in columns] for row in rows]
w = matvec(F, v)
record("FULL.rank", "the full path map is injective on the three candidates",
       rank(F) == 3, f"rows={len(rows)}")
record("FULL.obstruction", "the residual core direction has nonzero full-path image",
       any(w), f"support={sum(value != 0 for value in w)}")

nonzero_coordinates = [index for index, value in enumerate(v) if value]
gauges = []
for index in nonzero_coordinates:
    phi = [Fraction(0), Fraction(0), Fraction(0)]
    phi[index] = Fraction(1, v[index])
    K = [[-value*coefficient for coefficient in phi] for value in w]
    adapted = [
        [F[row][column] + K[row][column] for column in range(3)]
        for row in range(len(F))
    ]
    gauges.append((index, phi, K, adapted))
record("SEWING.gauges", "every nonzero residual coordinate defines a rank-one sewing gauge",
       len(gauges) == len(nonzero_coordinates), nonzero_coordinates)
record("SEWING.activates", "each rank-one gauge makes the residual direction a full kernel",
       all(matvec(adapted, v) == [0]*len(F)
           for _, _, _, adapted in gauges),
       f"gauges={len(gauges)}")
record("SEWING.rank_one", "every nonzero correction matrix has rank one",
       all(rank(K) == 1 for _, _, K, _ in gauges), "K=-w tensor phi")
record("SEWING.minimum", "rank zero cannot cancel a nonzero obstruction",
       any(w), "Kv=-w requires K nonzero, hence rank at least one")

# The affine selector space {phi : phi(v)=1} has dimension 2.
difference_annihilates = []
for (_, phi_a, _, _), (_, phi_b, _, _) in itertools.combinations(gauges, 2):
    difference = [a-b for a, b in zip(phi_a, phi_b)]
    difference_annihilates.append(sum(a*b for a, b in zip(difference, v)) == 0)
record("SELECTOR.affine_plane",
       "rank-one sewing choices form an affine plane over covectors annihilating v",
       all(difference_annihilates) and len(v)-1 == 2,
       "phi(v)=1; translation space Ann(v) has dimension two")
record("SELECTOR.noncanonical",
       "the residual null direction does not choose one sewing gauge",
       len(gauges) > 1 and all(difference_annihilates),
       f"coordinate gauges={nonzero_coordinates}")

# Different gauges agree on v but differ on generic protected source directions.
protected_witnesses = []
for first, second in itertools.combinations(gauges, 2):
    K1, K2 = first[2], second[2]
    for basis_index in range(3):
        basis = [Fraction(0)]*3
        basis[basis_index] = 1
        delta = [a-b for a, b in zip(matvec(K1, basis), matvec(K2, basis))]
        if any(delta):
            protected_witnesses.append((first[0], second[0], basis_index))
            break
record("SELECTOR.protected_difference",
       "distinct sewing gauges are distinguishable on a protected successor direction",
       len(protected_witnesses) == math.comb(len(gauges), 2),
       protected_witnesses)

failed = [item for item in checks if item["status"] != "pass"]
payload = {
    "schema": "marici.strominger.magnetic_rank_one_portal_sewing.v1",
    "status": "passed" if not failed else "failed",
    "gate_count": len(checks),
    "passed_gate_count": len(checks)-len(failed),
    "primitive_core_null_vector": list(v),
    "full_obstruction": {
        "row_labels": [str(row) for row in rows],
        "values": [str(value) for value in w],
        "support_size": sum(value != 0 for value in w),
    },
    "selector": {
        "dimension": 2,
        "coordinate_gauges": nonzero_coordinates,
        "law": "K=-w tensor phi with phi(v)=1",
    },
    "checks": checks,
    "verdict": (
        "A rank-one off-diagonal correction is algebraically necessary and "
        "sufficient to promote the continued core null direction to a full magnetic "
        "kernel. Such corrections form a two-dimensional affine selector torsor. "
        "The desired kernel fixes only K(v), not K on complementary source directions; "
        "choosing a portal therefore still requires an independent source constructor."
    ),
}
out = Path(__file__).resolve().parents[1] / "results" / "magnetic_rank_one_portal_sewing.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(1 if failed else 0)
