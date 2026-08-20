#!/usr/bin/env python3
"""Bounded multiprime order-one projective Krylov/exactness test.

This tests whether p0(t) F + p1(t) d_t F is represented by a low-degree
exact three-form.  It is a sampled finite bound, not a Gauss--Manin rank
certificate.
"""

import json
from pathlib import Path

import check_five_site_weight_five_rational_trace as trace

ROOT = Path(__file__).resolve().parents[2]
CANON = json.loads((ROOT / "research/benincasa/results/five-site-asymmetric-canonical-sum.json").read_text())
LABELS = CANON["denominator_labels"]
OUTPUT = ROOT / "research/nima/results/five-site-projective-krylov-order-one.json"


def r_data(u, p):
    u1, u2, u3 = u
    r = trace.radicands(u1, u2, u3, p)
    dr = [[(4*u1-2*u2) % p, (4*u2-2*u1-2*u3) % p, (2*u3-2*u2) % p]]
    dr += [[(dr[0][j]+v[j]) % p for j in range(3)] for v in
           [(-2, 0, 0), (0, -2, 0), (0, 0, -2), (2, 2, -8)]]
    return r, dr


def norm_and_derivatives(label, t, r, dr, p):
    q = trace.facets[label]
    a = sum(int(x) for x in q["x"]) * t % p
    support = [(i, int(b)) for i, b in enumerate(q["y"]) if int(b)]
    if not support:
        return a, [0, 0, 0]
    if len(support) == 1:
        i, b = support[0]
        b2 = b*b % p
        return (a*a-b2*r[i]) % p, [(-b2*dr[i][j]) % p for j in range(3)]
    (i, b), (k, c) = support
    b2, c2 = b*b % p, c*c % p
    z = (a*a-b2*r[i]-c2*r[k]) % p
    n = (z*z-4*b2*c2*r[i]*r[k]) % p
    dn = []
    for j in range(3):
        dz = (-b2*dr[i][j]-c2*dr[k][j]) % p
        dn.append((2*z*dz-4*b2*c2*(dr[i][j]*r[k]+r[i]*dr[k][j])) % p)
    return n, dn


def omega_and_dt(t, ys, p):
    labels_common = trace.common
    total = 0
    total_dt = 0
    for selected in trace.terms:
        labels = labels_common + selected
        denominator = 1
        logarithmic_dt = 0
        for label in labels:
            value = trace.q_value(label, t, ys, p)
            if value == 0:
                return None
            denominator = denominator * value % p
            a = sum(int(x) for x in trace.facets[label]["x"]) % p
            logarithmic_dt = (logarithmic_dt + a*trace.inv(value, p)) % p
        summand = trace.inv(denominator, p)
        total = (total + summand) % p
        total_dt = (total_dt - summand*logarithmic_dt) % p
    return total, total_dt


def oracle_sample(prime, seed):
    roots = {x*x % prime: x for x in range(prime)}
    for off in range(20000):
        u = [(seed+3*off+2) % prime, (2*seed+5*off+3) % prime,
             (3*seed+7*off+5) % prime]
        t = (11*seed+17*off+13) % prime
        r, dr = r_data(u, prime)
        if any(x == 0 or x not in roots for x in r):
            continue
        ys0 = [roots[x] for x in r]
        value = value_dt = 0
        for mask in range(32):
            ys = [(-y if mask & (1 << i) else y) % prime for i, y in enumerate(ys0)]
            pair = omega_and_dt(t, ys, prime)
            if pair is None:
                break
            sign = -1 if mask.bit_count() & 1 else 1
            value = (value + sign*pair[0]) % prime
            value_dt = (value_dt + sign*pair[1]) % prime
        else:
            y_product = 1
            for y in ys0:
                y_product = y_product*y % prime
            scale = trace.inv(32*y_product, prime)
            target = value*scale % prime
            target_dt = value_dt*scale % prime
            dprod = 1
            dlog = [0, 0, 0]
            for label in LABELS:
                n, dn = norm_and_derivatives(label, t, r, dr, prime)
                if n == 0:
                    break
                dprod = dprod*n % prime
                ni = trace.inv(n, prime)
                for j in range(3):
                    dlog[j] = (dlog[j]+dn[j]*ni) % prime
            else:
                inv2 = trace.inv(2, prime)
                volume = [sum(dr[i][j]*trace.inv(r[i], prime) for i in range(5))*inv2 % prime
                          for j in range(3)]
                return {"u": u, "t": t, "target": target, "target_dt": target_dt,
                        "D": dprod, "dlog": dlog, "volume": volume}
    raise RuntimeError("sample exhaustion")


def monomials(d):
    return [(a, b, c) for a in range(d+1) for b in range(d+1-a)
            for c in range(d+1-a-b)]


def primitive_row(sample, degree, pole_order, p):
    u = sample["u"]
    denominator = pow(trace.inv(sample["D"], p), pole_order, p)
    out = []
    for j in range(3):
        for exponents in monomials(degree):
            monomial = 1
            for x, exponent in zip(u, exponents):
                monomial = monomial*pow(x, exponent, p) % p
            derivative = 0
            if exponents[j]:
                derivative = exponents[j]
                for k, (x, exponent) in enumerate(zip(u, exponents)):
                    derivative = derivative*pow(x, exponent-(1 if k == j else 0), p) % p
            coefficient = (sample["volume"][j]-pole_order*sample["dlog"][j]) % p
            out.append((derivative+monomial*coefficient)*denominator % p)
    return out


def rank(matrix, p):
    a = [row[:] for row in matrix]
    rows, cols, pivot_row = len(a), len(a[0]), 0
    for col in range(cols):
        pivot = next((i for i in range(pivot_row, rows) if a[i][col] % p), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        scale = trace.inv(a[pivot_row][col], p)
        a[pivot_row] = [x*scale % p for x in a[pivot_row]]
        for i in range(rows):
            if i != pivot_row and a[i][col] % p:
                scale = a[i][col] % p
                a[i] = [(x-scale*y) % p for x, y in zip(a[i], a[pivot_row])]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


results = []
for prime in (1009, 1013):
    samples = []
    keys = set()
    for seed in range(1, 4001):
        try:
            sample = oracle_sample(prime, seed)
        except RuntimeError:
            continue
        key = (sample["t"], *sample["u"])
        if key not in keys:
            keys.add(key)
            samples.append(sample)
        if len(samples) == 96:
            break
    assert len(samples) == 96
    for primitive_degree in range(4):
        primitive_columns = 3*len(monomials(primitive_degree))
        for scalar_degree in range(4):
            scalar_columns = scalar_degree+1
            used = samples[:primitive_columns+2*scalar_columns+12]
            primitive = [primitive_row(s, primitive_degree, 2, prime) for s in used]
            p0 = [[s["target"]*pow(s["t"], k, prime) % prime for k in range(scalar_columns)]
                  for s in used]
            p1 = [[s["target_dt"]*pow(s["t"], k, prime) % prime for k in range(scalar_columns)]
                  for s in used]
            rank_primitive = rank(primitive, prime)
            without_p1 = [a+b for a, b in zip(primitive, p0)]
            full = [a+b+c for a, b, c in zip(primitive, p0, p1)]
            rank_without_p1 = rank(without_p1, prime)
            rank_full = rank(full, prime)
            p1_kernel_excess = scalar_columns-(rank_full-rank_without_p1)
            results.append({
                "prime": prime,
                "primitive_degree": primitive_degree,
                "primitive_pole_order": 2,
                "scalar_degree": scalar_degree,
                "samples": len(used),
                "rank_primitive": rank_primitive,
                "rank_without_dt": rank_without_p1,
                "rank_full": rank_full,
                "dt_relation_dimension": p1_kernel_excess,
                "order_one_relation_exists": p1_kernel_excess > 0,
            })

output = {
    "schema": "marici.five_site.projective_krylov_order_one.v1",
    "results": results,
    "scope": "Sampled order-one closure modulo pole-order-two exact forms; degrees 0..3 only.",
    "interpretation": "A negative result is a replicated finite bound, not a Gauss-Manin rank theorem.",
    "passed": True,
}
OUTPUT.write_text(json.dumps(output, indent=2)+"\n")
print(json.dumps(output, sort_keys=True))
