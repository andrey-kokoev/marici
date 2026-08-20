#!/usr/bin/env python3
"""Bounded multiprime order-three projective Krylov/exactness test."""

import json
from pathlib import Path

import check_five_site_projective_krylov_order_one as base

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "research/nima/results/five-site-projective-krylov-order-three.json"


def omega_jets_three(t, ys, p):
    totals = [0, 0, 0, 0]
    for selected in base.trace.terms:
        labels = base.trace.common + selected
        denominator = 1
        power_sums = [0, 0, 0]
        for label in labels:
            value = base.trace.q_value(label, t, ys, p)
            if value == 0:
                return None
            denominator = denominator*value % p
            a = sum(int(x) for x in base.trace.facets[label]["x"]) % p
            ratio = a*base.trace.inv(value, p) % p
            for k in range(3):
                power_sums[k] = (power_sums[k]+pow(ratio, k+1, p)) % p
        summand = base.trace.inv(denominator, p)
        s1, s2, s3 = power_sums
        jets = [
            summand,
            -summand*s1,
            summand*(s1*s1+s2),
            -summand*(s1*s1*s1+3*s1*s2+2*s3),
        ]
        totals = [(x+y) % p for x, y in zip(totals, jets)]
    return totals


def oracle_sample(prime, seed):
    roots = {x*x % prime: x for x in range(prime)}
    for off in range(20000):
        u = [(seed+3*off+2) % prime, (2*seed+5*off+3) % prime,
             (3*seed+7*off+5) % prime]
        t = (11*seed+17*off+13) % prime
        r, dr = base.r_data(u, prime)
        if any(x == 0 or x not in roots for x in r):
            continue
        ys0 = [roots[x] for x in r]
        jets = [0, 0, 0, 0]
        for mask in range(32):
            ys = [(-y if mask & (1 << i) else y) % prime for i, y in enumerate(ys0)]
            values = omega_jets_three(t, ys, prime)
            if values is None:
                break
            sign = -1 if mask.bit_count() & 1 else 1
            jets = [(x+sign*y) % prime for x, y in zip(jets, values)]
        else:
            y_product = 1
            for y in ys0:
                y_product = y_product*y % prime
            scale = base.trace.inv(32*y_product, prime)
            jets = [x*scale % prime for x in jets]
            dprod = 1
            dlog = [0, 0, 0]
            for label in base.LABELS:
                n, dn = base.norm_and_derivatives(label, t, r, dr, prime)
                if n == 0:
                    break
                dprod = dprod*n % prime
                inverse = base.trace.inv(n, prime)
                for j in range(3):
                    dlog[j] = (dlog[j]+dn[j]*inverse) % prime
            else:
                inv2 = base.trace.inv(2, prime)
                volume = [
                    sum(dr[i][j]*base.trace.inv(r[i], prime) for i in range(5))*inv2 % prime
                    for j in range(3)
                ]
                return {
                    "u": u,
                    "t": t,
                    "target": jets[0],
                    "target_dt": jets[1],
                    "target_dt2": jets[2],
                    "target_dt3": jets[3],
                    "D": dprod,
                    "dlog": dlog,
                    "volume": volume,
                }
    raise RuntimeError("sample exhaustion")


def main():
    results = []
    for prime in (1009, 1013):
        samples = []
        keys = set()
        for seed in range(1, 5001):
            try:
                sample = oracle_sample(prime, seed)
            except RuntimeError:
                continue
            key = (sample["t"], *sample["u"])
            if key not in keys:
                keys.add(key)
                samples.append(sample)
            if len(samples) == 120:
                break
        assert len(samples) == 120
        for primitive_degree in range(4):
            primitive_columns = 3*len(base.monomials(primitive_degree))
            for scalar_degree in range(4):
                scalar_columns = scalar_degree+1
                used = samples[:primitive_columns+4*scalar_columns+12]
                primitive = [base.primitive_row(s, primitive_degree, 4, prime) for s in used]
                blocks = []
                for field in ("target", "target_dt", "target_dt2", "target_dt3"):
                    blocks.append([
                        [s[field]*pow(s["t"], k, prime) % prime
                         for k in range(scalar_columns)] for s in used
                    ])
                without_dt3 = [
                    a+b+c+d for a, b, c, d in
                    zip(primitive, blocks[0], blocks[1], blocks[2])
                ]
                full = [
                    a+b+c+d+e for a, b, c, d, e in
                    zip(primitive, blocks[0], blocks[1], blocks[2], blocks[3])
                ]
                rank_primitive = base.rank(primitive, prime)
                rank_without_dt3 = base.rank(without_dt3, prime)
                rank_full = base.rank(full, prime)
                dt3_relation_dimension = scalar_columns-(rank_full-rank_without_dt3)
                results.append({
                    "prime": prime,
                    "primitive_degree": primitive_degree,
                    "primitive_pole_order": 4,
                    "scalar_degree": scalar_degree,
                    "samples": len(used),
                    "rank_primitive": rank_primitive,
                    "rank_without_dt3": rank_without_dt3,
                    "rank_full": rank_full,
                    "dt3_relation_dimension": dt3_relation_dimension,
                    "genuine_order_three_relation_exists": dt3_relation_dimension > 0,
                })
    output = {
        "schema": "marici.five_site.projective_krylov_order_three.v1",
        "results": results,
        "scope": "Sampled order-three closure modulo pole-order-four exact forms; degrees 0..3 only.",
        "interpretation": "A negative result is a replicated finite bound, not a Gauss-Manin rank theorem.",
        "passed": True,
    }
    OUTPUT.write_text(json.dumps(output, indent=2)+"\n")
    print(json.dumps(output, sort_keys=True))


if __name__ == "__main__":
    main()
