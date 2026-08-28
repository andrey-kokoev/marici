#!/usr/bin/env python3
"""Exact finite-field reduction to the rank-five anti-invariant infinity target."""
from __future__ import annotations
import contextlib
import io
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CHECKERS = ROOT / "research" / "benincasa" / "checkers"
sys.path.insert(0, str(CHECKERS))
P = int(os.environ.get("MARICI_FIELD_PRIME", "32009"))
os.environ["MARICI_FIELD_PRIME"] = str(P)

with contextlib.redirect_stdout(io.StringIO()):
    import check_rank26_infinity_order2_endpoint_descent as src

inv2 = pow(2, P - 2, P)
x, y, z = src.POINT
E = x + y + z
h = x*x + y*y - z*z


def clean(a):
    return {k: v % P for k, v in a.items() if v % P}


def add(a, b, scale=1):
    out = dict(a)
    for k, v in b.items():
        nv = (out.get(k, 0) + scale*v) % P
        if nv:
            out[k] = nv
        else:
            out.pop(k, None)
    return out


def mul(a, b):
    out = {}
    for i, u in a.items():
        for j, v in b.items():
            out[i+j] = (out.get(i+j, 0) + u*v) % P
    return clean(out)


def power(a, n):
    out = {0: 1}
    for _ in range(n):
        out = mul(out, a)
    return out


def deriv(a):
    return {k-1: k*v % P for k, v in a.items() if k}


def shift(a, n):
    return {k+n: v for k, v in a.items()}


t = {1: 1}
u = {0: 1, 1: 1}
F = {4: x*x, 2: -h, 0: y*y}
Fp = deriv(F)
G = {
    2: -2*x*x*(y*y+E*E) + h*(x*x+E*E),
    0: h*(y*y+E*E) - 2*y*y*(x*x+E*E),
}
Q_T, Q_U, Q_F = 6, 4, 1


def ratvec(num, a=0, b=0, f=0):
    if not (0 <= a <= Q_T and 0 <= b <= Q_U and 0 <= f <= Q_F):
        raise ValueError((a,b,f))
    out = shift(num, Q_T-a)
    out = mul(out, power(u, Q_U-b))
    out = mul(out, power(F, Q_F-f))
    return clean(out)


def term_vec(coefficient, t_power, b, f, extra):
    a = max(0, -t_power)
    num = shift(extra, max(0, t_power))
    return {k: coefficient*v % P for k, v in ratvec(num, a, b, f).items()}


def exact_dSW(n, b, f):
    # S=t^n/((t+1)^b F^f), and d(SW)=L(S) dt/W.
    out = {}
    if n:
        out = add(out, term_vec(n, n-1, b, f, F))
    if b:
        out = add(out, term_vec(-b, n, b+1, f, F))
    coeff = (inv2 - f) % P
    if coeff:
        out = add(out, term_vec(coeff, n, b, f, Fp))
    return clean(out)


def add_pivot(row, pivots):
    row = reduce_vec(row, pivots)
    if not row:
        return False
    pivot = max(row)
    inv = pow(row[pivot], P-2, P)
    pivots[pivot] = {k: v*inv % P for k,v in row.items()}
    return True


def reduce_vec(row, pivots):
    row = dict(row)
    while True:
        reducible = [k for k in row if k in pivots]
        if not reducible:
            return row
        pivot = max(reducible)
        row = add(row, pivots[pivot], -row[pivot])


# A bounded exact-function packet large enough for all source pole orders.
exact_pivots = {}
exact_generator_count = 0
for f in range(2):
    for b in range(4):
        for n in range(-5, 13):
            row = exact_dSW(n, b, f)
            if row:
                exact_generator_count += 1
                add_pivot(row, exact_pivots)

coh_names = ["omega0", "omega2", "alpha0", "alpha_minus1", "alpha_infinity"]
coh_raw = [
    ratvec({0:1}),
    ratvec({2:1}),
    ratvec({0:y}, a=1),
    ratvec({0:z}, b=1),
    ratvec({1:x}),
]


def vec_scale(row, c):
    return {k: v*c % P for k,v in row.items() if v*c % P}


# Tagged row echelon basis of cohomology modulo exact forms.
coh_pivots = {}
for j, raw in enumerate(coh_raw):
    row = reduce_vec(raw, exact_pivots)
    expr = {j: 1}
    while True:
        reducible = [k for k in row if k in coh_pivots]
        if not reducible:
            break
        pivot = max(reducible)
        prow, pexpr = coh_pivots[pivot]
        c = row[pivot]
        row = add(row, prow, -c)
        expr = add(expr, pexpr, -c)
    if not row:
        raise RuntimeError(f"cohomology basis collapsed at {coh_names[j]}")
    pivot = max(row)
    inverse = pow(row[pivot], P-2, P)
    coh_pivots[pivot] = (vec_scale(row, inverse), vec_scale(expr, inverse))


# Denominator expansion D(s)=D0+sD1+s^2D2+...
factors = [
    ({0:1}, -(y+z)),
    (t, -(x+z)),
    (u, z),
    ({0:1}, -x),
    (t, -y),
]
D = [{0:1}, {}, {}]
for linear, constant in factors:
    nxt = [{}, {}, {}]
    for n in range(3):
        nxt[n] = add(nxt[n], mul(D[n], linear))
        if n:
            nxt[n] = add(nxt[n], D[n-1], constant)
    D = nxt
D0,D1,D2 = D


def source_form(i, degree):
    if degree < 5:
        return {}
    if degree == 5:
        return ratvec({i:1}, a=2, b=1)
    if degree == 6:
        return ratvec(vec_scale(shift(D1, i), -1), a=4, b=2)
    if degree == 7:
        first = add(mul(D1,D1), mul(D0,D2), -1)
        out = ratvec(shift(first, i), a=6, b=3)
        second = ratvec(vec_scale(shift(G,i), -inv2), a=2, b=1, f=1)
        return add(out, second)
    raise ValueError(degree)


def cohomology_coordinates(row):
    row = reduce_vec(row, exact_pivots)
    coords = {}
    while row:
        reducible = [k for k in row if k in coh_pivots]
        if not reducible:
            return None, row
        pivot = max(reducible)
        prow, expr = coh_pivots[pivot]
        c = row[pivot]
        row = add(row, prow, -c)
        coords = add(coords, expr, c)
    return [coords.get(i,0) for i in range(5)], {}


low_exponents = src.low_exponents
coordinates = {}
remainders = {}
for exponent in low_exponents:
    i,j = exponent
    coords, remainder = cohomology_coordinates(source_form(i, i+j))
    coordinates[exponent] = coords
    if remainder:
        remainders[exponent] = remainder

# Test all five coordinate functionals on the repaired rank-26 quotient.
coordinate_solutions = []
dual_rows_canonical = []
for j in range(5):
    equations = [
        (src.quotient_rows[e], coordinates[e][j], e)
        for e in low_exponents
    ]
    solution, nullity, constraint_rank, witness = src.solve_functional(equations)
    dual_rows_canonical.append(solution)
    coordinate_solutions.append({
        "coordinate": coh_names[j],
        "consistent": solution is not None,
        "constraint_rank": constraint_rank,
        "nullity": nullity,
        "witness": bool(witness),
    })

endpoint_agreement = True
for exponent in low_exponents:
    c = coordinates[exponent]
    endpoint_agreement &= c[2] == src.raw_endpoint_value("t=0", exponent)
    endpoint_agreement &= c[3] == src.raw_endpoint_value("t=-1", exponent)
    endpoint_agreement &= (-c[4]) % P == src.raw_endpoint_value("t=infinity", exponent)

# Transport the five covectors into Nima's original 26-coordinate convention.
old_free = src.pres["free_low"]
dual_rows_nima = []
for ell in dual_rows_canonical:
    row = []
    for column in old_free:
        exponent = src.pres["ordered_columns"][column][-1]
        qrow = src.quotient_rows[exponent]
        row.append(sum(ell[k] * v for k,v in qrow.items()) % P)
    dual_rows_nima.append(row)

ann_path = (
    ROOT / "research" / "nima" / "results"
    / f"rank26_physical_source_covariant_jet_census_k3_p{P}.json"
)
ann_packet = json.loads(ann_path.read_text(encoding="utf-8"))
ann_rows = []
for sparse in ann_packet["annihilator_reduced_dual_basis"]:
    row = [0] * 26
    for entry in sparse:
        row[int(entry["free_coordinate"])] = int(entry["coefficient"]) % P
    ann_rows.append(row)


def dense_rank(rows):
    pivots = {}
    for source in rows:
        row = {i:v for i,v in enumerate(source) if v}
        add_pivot(row, pivots)
    return len(pivots)


rank5 = dense_rank(dual_rows_nima)
rank7 = dense_rank(ann_rows)
joint_rank = dense_rank(dual_rows_nima + ann_rows)
intersection_rank = rank5 + rank7 - joint_rank

checks = {
    "exact_packet_nonempty": exact_generator_count > 0 and len(exact_pivots) > 0,
    "anti_invariant_cohomology_rank_is_five": len(coh_pivots) == 5,
    "all_source_forms_reduce_without_remainder": not remainders,
    "residue_coordinates_match_independent_endpoint_engine": endpoint_agreement,
    "all_five_coordinates_descend": all(x["consistent"] for x in coordinate_solutions),
    "all_five_descents_are_unique": all(
        x["constraint_rank"] == 26 and x["nullity"] == 0
        for x in coordinate_solutions
    ),
    "rank_five_dual_image_is_rank_five_in_nima_coordinates": rank5 == 5,
    "transported_annihilator_is_rank_seven": rank7 == 7,
}
packet = {
    "schema": "marici.rank26-anti-invariant-infinity-map.v1",
    "prime": P,
    "external_point": list(src.POINT),
    "common_denominator": "t^6(t+1)^4 F",
    "exact_generator_count": exact_generator_count,
    "exact_span_rank": len(exact_pivots),
    "cohomology_basis": coh_names,
    "coordinate_solutions": coordinate_solutions,
    "nonzero_compact_coordinates": {
        name: sum(coordinates[e][j] != 0 for e in low_exponents)
        for j,name in enumerate(coh_names[:2])
    },
    "remainder_count": len(remainders),
    "dual_image_comparison": {
        "rank5_image_rank": rank5,
        "transported_annihilator_rank": rank7,
        "joint_rank": joint_rank,
        "intersection_rank": intersection_rank,
        "rank5_excess_outside_seven_plane": rank5 - intersection_rank,
        "seven_plane_excess_outside_rank5": rank7 - intersection_rank,
    },
    "checks": checks,
    "passed": all(checks.values()),
    "conclusion": (
        "The complete source boundary forms reduce exactly to two compact and "
        "three anti-invariant logarithmic coordinates, and all five coordinate "
        "functionals descend uniquely on the repaired rank-26 quotient."
    ),
}
out = ROOT / "research" / "benincasa" / "results" / f"rank26-anti-invariant-infinity-map-p{P}.json"
out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))
if not packet["passed"]:
    raise SystemExit(1)
