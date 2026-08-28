#!/usr/bin/env python3
"""Compute the complete order-two infinity endpoint packet at physical rank 26.

The source compactification has five marked linear factors and
  Kbar = F + s^2 G + O(s^4).
For numerator degree 5+n, n=0,1,2, this checker derives the logarithmic
finite-part coefficient from the s^n term of
  1/(D(s) sqrt(F+s^2 G))
and tests whether each completed endpoint functional descends through the
physical rank-26 exact presentation.  No endpoint values are fitted.
"""
from __future__ import annotations

import contextlib
import io
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BEN = ROOT / "research" / "benincasa"
sys.path.insert(0, str(BEN))

P = int(os.environ.get("MARICI_FIELD_PRIME", "32009"))
os.environ["MARICI_FIELD_PRIME"] = str(P)

with contextlib.redirect_stdout(io.StringIO()):
    import physical_four_mark_residue_twisted_derham as base
    import g12_g31_residue_chart_transition as charts

POINT = (2, 3, 4)
NAMES = ("g1", "g2", "g3", "g23", "g31")
charts.GAMMA = (-pow(2, P - 2, P)) % P
charts.AMBIENT = 14
charts.CUTOFF = 7
charts.K_DEPTH = 3
pres = charts.presentation(base.fiber_data, POINT, NAMES)
free = pres["free_low"]
free_pos = {column: index for index, column in enumerate(free)}
dimension = len(free)
low_count = len(pres["low_labels"])

# Derive the actual ten relations internal to the low simple-pole sector.
# Reducing in the ambient presentation and then dropping surviving ambient
# coordinates is not a quotient map.
def full_reduce(row, pivots):
    row = dict(row)
    while True:
        reducible = [column for column in row if column in pivots]
        if not reducible:
            return row
        pivot = max(reducible)
        coefficient = row[pivot]
        for column, value in pivots[pivot].items():
            base.add_value(row, column, -coefficient * value)


low_relation_pivots = {}
for pivot in sorted(p for p in pres["pivots"] if p < low_count):
    pivot_row = pres["pivots"][pivot]
    tail = {c: v for c, v in pivot_row.items() if c != pivot}
    other = {p: r for p, r in pres["pivots"].items() if p != pivot}
    reduced_tail = full_reduce(tail, other)
    relation = {pivot: 1, **reduced_tail}
    if any(c >= low_count for c in relation):
        raise RuntimeError("low relation retained ambient coordinates")
    base.add_pivot(relation, low_relation_pivots)

free = [column for column in range(low_count) if column not in low_relation_pivots]
free_pos = {column: index for index, column in enumerate(free)}
dimension = len(free)

LO, HI = -28, 28


def clean(a):
    return {k: v % P for k, v in a.items() if LO <= k <= HI and v % P}


def add(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = (out.get(k, 0) + v) % P
    return clean(out)


def scale(a, c):
    return clean({k: c * v for k, v in a.items()})


def mul(a, b):
    out = {}
    for i, x in a.items():
        for j, y in b.items():
            if LO <= i + j <= HI:
                out[i + j] = (out.get(i + j, 0) + x * y) % P
    return clean(out)


def power(a, n):
    out = {0: 1}
    for _ in range(n):
        out = mul(out, a)
    return out


def inv_series(a):
    a = clean(a)
    lead = min(a)
    c0 = a[lead]
    unit = {k - lead: v * pow(c0, P - 2, P) % P for k, v in a.items()}
    coeff = {0: 1}
    for n in range(1, HI - LO + 1):
        coeff[n] = -sum(unit.get(k, 0) * coeff.get(n - k, 0) for k in range(1, n + 1)) % P
    return clean({n - lead: v * pow(c0, P - 2, P) % P for n, v in coeff.items()})


def sqrt_unit(a, root):
    """Square root of an ordinary series with prescribed nonzero constant root."""
    assert min(a) >= 0 and a.get(0, 0) == root * root % P
    out = {0: root % P}
    inv2r = pow(2 * root % P, P - 2, P)
    for n in range(1, HI + 1):
        cross = sum(out.get(k, 0) * out.get(n - k, 0) for k in range(1, n))
        out[n] = (a.get(n, 0) - cross) * inv2r % P
    return clean(out)


def quotient_row(exponent):
    label = (0, 1, 1, 1, 1, 1, exponent)
    reduced = full_reduce(
        {pres["columns"][label]: 1},
        low_relation_pivots,
    )
    if any(column not in free_pos for column in reduced):
        raise RuntimeError("low quotient reduction did not land in free-low coordinates")
    return {
        free_pos[column]: value
        for column, value in reduced.items()
        if value
    }


def add_scaled(row, source, factor):
    for column, value in source.items():
        nv = (row.get(column, 0) + factor * value) % P
        if nv:
            row[column] = nv
        else:
            row.pop(column, None)


def solve_functional(equations):
    pivots = {}
    witness = None
    for coefficients, rhs, label in equations:
        row = dict(coefficients)
        provenance = {label: 1}
        if rhs % P:
            row[dimension] = rhs % P
        while row:
            candidates = [c for c in row if c < dimension]
            if not candidates:
                obstruction = row.get(dimension, 0)
                if obstruction and witness is None:
                    inverse = pow(obstruction, P - 2, P)
                    witness = {
                        key: value * inverse % P
                        for key, value in provenance.items()
                        if value % P
                    }
                break
            pivot = max(candidates)
            coefficient = row[pivot]
            if pivot not in pivots:
                inverse = pow(coefficient, P - 2, P)
                pivots[pivot] = (
                    {c: v * inverse % P for c, v in row.items()},
                    {k: v * inverse % P for k, v in provenance.items()},
                )
                break
            pivot_row, pivot_provenance = pivots[pivot]
            add_scaled(row, pivot_row, -coefficient)
            add_scaled(provenance, pivot_provenance, -coefficient)
    if witness is not None:
        return None, None, len(pivots), witness
    solution = [0] * dimension
    for pivot in sorted(pivots):
        row, _ = pivots[pivot]
        rhs = row.get(dimension, 0)
        tail = sum(v * solution[c] for c, v in row.items() if c != pivot and c < dimension)
        solution[pivot] = (rhs - tail) % P
    return solution, dimension - len(pivots), len(pivots), None


def endpoint_series(endpoint):
    x, y, z = POINT
    E = x + y + z
    h = x*x + y*y - z*z
    if endpoint == "t=0":
        t = {1: 1}
        root = y
        root_shift = 0
        differential_shift = 0
        differential_sign = 1
    elif endpoint == "t=-1":
        t = {0: -1, 1: 1}
        root = z
        root_shift = 0
        differential_shift = 0
        differential_sign = 1
    elif endpoint == "t=infinity":
        t = {-1: 1}
        root = x
        root_shift = -2
        differential_shift = -2
        differential_sign = -1
    else:
        raise ValueError(endpoint)

    one = {0: 1}
    t2, t4 = power(t, 2), power(t, 4)
    F = add(add(scale(t4, x*x), scale(t2, -h)), {0: y*y})
    c2 = -2*x*x*(y*y+E*E) + h*(x*x+E*E)
    c0 = h*(y*y+E*E) - 2*y*y*(x*x+E*E)
    G = add(scale(t2, c2), {0: c0})

    if endpoint == "t=infinity":
        # F = u^-4 Funit; sqrt(F) = u^-2 sqrt(Funit).
        Funit = {k + 4: v for k, v in F.items()}
        sqrtF = {k + root_shift: v for k, v in sqrt_unit(Funit, root).items()}
    else:
        sqrtF = sqrt_unit(F, root)
    invsqrtF = inv_series(sqrtF)
    invF = mul(invsqrtF, invsqrtF)

    factors = [
        (one, -(y+z)),
        (t, -(x+z)),
        (add(t, one), z),
        (one, -x),
        (t, -y),
    ]
    D = [{0: 1}, {}, {}]
    for linear, constant in factors:
        nxt = [{}, {}, {}]
        for n in range(3):
            nxt[n] = add(nxt[n], mul(D[n], linear))
            if n:
                nxt[n] = add(nxt[n], scale(D[n-1], constant))
        D = nxt
    invD0 = inv_series(D[0])
    invD1 = scale(mul(mul(invD0, invD0), D[1]), -1)
    invD2 = add(
        mul(mul(mul(invD0, invD0), invD0), mul(D[1], D[1])),
        scale(mul(mul(invD0, invD0), D[2]), -1),
    )
    coeff = [
        mul(invD0, invsqrtF),
        mul(invD1, invsqrtF),
        add(mul(invD2, invsqrtF), scale(mul(mul(mul(invD0, G), invF), invsqrtF), pow(2, P-2, P) * -1)),
    ]

    def residue(i, normal_order):
        form = mul(power(t, i), coeff[normal_order])
        target = -1 - differential_shift
        return differential_sign * form.get(target, 0) % P

    return residue


residue_functions = {
    endpoint: endpoint_series(endpoint)
    for endpoint in ("t=0", "t=-1", "t=infinity")
}
low_exponents = base.monomials_at_most(7)
quotient_rows = {e: quotient_row(e) for e in low_exponents}


def raw_endpoint_value(endpoint, exponent):
    i, j = exponent
    degree = i + j
    if degree < 5 or degree > 7:
        return 0
    return residue_functions[endpoint](i, degree - 5)


solutions = {}
witnesses = {}
solution_packets = {}
grade_nonzero_counts = {}
for endpoint in ("t=0", "t=-1", "t=infinity"):
    grade_nonzero_counts[endpoint] = {
        str(d): sum(raw_endpoint_value(endpoint, e) != 0 for e in low_exponents if sum(e) == d)
        for d in (5, 6, 7)
    }
    equations = [
        (quotient_rows[e], raw_endpoint_value(endpoint, e), e)
        for e in low_exponents
    ]
    solution, nullity, equation_rank, witness = solve_functional(equations)
    solutions[endpoint] = solution
    witnesses[endpoint] = witness
    solution_packets[endpoint] = {
        "consistent": solution is not None,
        "constraint_rank": equation_rank,
        "solution_nullity": nullity,
        "support": [
            {"free_coordinate": i, "coefficient": v if v <= P//2 else v-P}
            for i, v in enumerate(solution or []) if v
        ],
        "normalized_obstruction_relation": [
            {
                "monomial_exponent": list(e),
                "coefficient": v if v <= P//2 else v-P,
            }
            for e, v in sorted((witness or {}).items())
            if v
        ],
    }

x, y, z = POINT
known_degree5 = {
    "t=0": [(-pow(y, P-2, P)) % P, pow(y, P-2, P), 0, 0, 0, 0],
    "t=-1": [
        (pow(z, P-2, P) if i % 2 == 0 else -pow(z, P-2, P)) % P
        for i in range(6)
    ],
    "t=infinity": [0, 0, 0, 0, (-pow(x, P-2, P)) % P, pow(x, P-2, P)],
}
recovered_degree5 = {
    endpoint: [residue_functions[endpoint](i, 0) for i in range(6)]
    for endpoint in residue_functions
}

def witness_is_normalized(endpoint):
    witness = witnesses[endpoint]
    if not witness:
        return False
    quotient_sum = {}
    residue_sum = 0
    for exponent, coefficient in witness.items():
        add_scaled(quotient_sum, quotient_rows[exponent], coefficient)
        residue_sum += coefficient * raw_endpoint_value(endpoint, exponent)
    return not quotient_sum and residue_sum % P == 1


checks = {
    "physical_low_quotient_dimension_is_26": dimension == 26,
    "ten_internal_low_relations": len(low_relation_pivots) == 10,
    "degree_five_normalization_matches_direct_residues": recovered_degree5 == known_degree5,
    "all_three_completed_endpoint_functionals_descend": all(
        v is not None for v in solutions.values()
    ),
    "each_completed_endpoint_functional_is_unique": all(
        packet["constraint_rank"] == dimension and packet["solution_nullity"] == 0
        for packet in solution_packets.values()
    ),
    "no_obstruction_witness_survives_repaired_quotient": all(
        witness is None for witness in witnesses.values()
    ),
    "degree_six_or_seven_corrections_are_nonzero": all(
        grade_nonzero_counts[e]["6"] + grade_nonzero_counts[e]["7"] > 0
        for e in grade_nonzero_counts
    ),
}

packet = {
    "schema": "marici.rank26-infinity-order2-endpoint-descent.v2",
    "prime": P,
    "external_point": list(POINT),
    "gamma": "-1/2",
    "quotient_dimension": dimension,
    "quotient_construction": (
        "ten relations closed internally in the 36-dimensional low simple-pole "
        "sector; no ambient-coordinate truncation"
    ),
    "source_expansion": {
        "denominator": "D(s)=product_i(l_i(t)+s c_i), retained through s^2",
        "branch": "Kbar=F+s^2 G+O(s^4)",
        "normal_grades": {
            "degree5": "[s^0] 1/(D sqrt(Kbar))",
            "degree6": "[s^1] 1/(D sqrt(Kbar))",
            "degree7": "[s^2] 1/(D sqrt(Kbar))",
        },
    },
    "nonzero_raw_values_by_degree": grade_nonzero_counts,
    "endpoint_solutions": solution_packets,
    "checks": checks,
    "passed": all(checks.values()),
    "conclusion": (
        "The source-derived degree-six and degree-seven finite parts complete "
        "the endpoint packet sufficiently for descent."
        if all(v is not None for v in solutions.values())
        else
        "Even after source-derived normal orders zero through two, at least one "
        "separate endpoint functional does not descend. The next typed object "
        "must retain compact and endpoint ports jointly."
    ),
    "scope": (
        "One exact finite-field fiber. This tests separate endpoint functionals "
        "through source normal order two; it does not yet prove characteristic-"
        "zero descent, cyclic naturality, or identify the physical seven-plane."
    ),
}

out = ROOT / "research" / "benincasa" / "results" / f"rank26-infinity-order2-endpoint-descent-p{P}.json"
out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))
if not packet["passed"]:
    raise SystemExit(1)
