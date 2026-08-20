#!/usr/bin/env python3
"""Reusable multiprime projective Krylov/exactness ladder through order six."""

import json
from math import comb, factorial
from pathlib import Path

import check_five_site_projective_krylov_order_one as base

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "research/nima/results/five-site-projective-krylov-ladder.json"
MAX_ORDER = 6
MAX_DEGREE = 3
SAMPLE_COUNT = 120


def omega_jets(t, ys, p, max_order):
    totals = [0]*(max_order+1)
    for selected in base.trace.terms:
        labels = base.trace.common + selected
        denominator = 1
        power_sums = [0]*max_order
        for label in labels:
            value = base.trace.q_value(label, t, ys, p)
            if value == 0:
                return None
            denominator = denominator*value % p
            a = sum(int(x) for x in base.trace.facets[label]["x"]) % p
            ratio = a*base.trace.inv(value, p) % p
            power = 1
            for k in range(max_order):
                power = power*ratio % p
                power_sums[k] = (power_sums[k]+power) % p
        logarithmic_jets = [0]+[
            ((-1 if order % 2 else 1)*factorial(order-1)*power_sums[order-1]) % p
            for order in range(1, max_order+1)
        ]
        normalized = [1]
        for order in range(1, max_order+1):
            value = sum(
                comb(order-1, k-1)*normalized[order-k]*logarithmic_jets[k]
                for k in range(1, order+1)
            ) % p
            normalized.append(value)
        summand = base.trace.inv(denominator, p)
        totals = [(x+summand*y) % p for x, y in zip(totals, normalized)]
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
        jets = [0]*(MAX_ORDER+1)
        for mask in range(32):
            ys = [(-y if mask & (1 << i) else y) % prime for i, y in enumerate(ys0)]
            values = omega_jets(t, ys, prime, MAX_ORDER)
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
                    "u": u, "t": t, "jets": jets, "D": dprod,
                    "dlog": dlog, "volume": volume,
                }
    raise RuntimeError("sample exhaustion")


def prior_rows(order):
    path = ROOT / f"research/nima/results/five-site-projective-krylov-order-{['zero','one','two','three'][order]}.json"
    packet = json.loads(path.read_text())
    key = f"dt{'' if order == 1 else order}_relation_dimension"
    return {
        (row["prime"], row["primitive_degree"], row["scalar_degree"]):
        (row["rank_primitive"],
         row["rank_without_dt" if order == 1 else f"rank_without_dt{order}"],
         row["rank_full"], row[key])
        for row in packet["results"]
    }


def main():
    results = []
    regressions = []
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
            if len(samples) == SAMPLE_COUNT:
                break
        assert len(samples) == SAMPLE_COUNT
        for order in range(1, MAX_ORDER+1):
            for primitive_degree in range(MAX_DEGREE+1):
                primitive_columns = 3*len(base.monomials(primitive_degree))
                for scalar_degree in range(MAX_DEGREE+1):
                    scalar_columns = scalar_degree+1
                    used = samples[:primitive_columns+(order+1)*scalar_columns+12]
                    primitive = [
                        base.primitive_row(s, primitive_degree, order+1, prime)
                        for s in used
                    ]
                    blocks = [
                        [[s["jets"][jet]*pow(s["t"], k, prime) % prime
                          for k in range(scalar_columns)] for s in used]
                        for jet in range(order+1)
                    ]
                    without_highest = [
                        a+sum((block[i] for block in blocks[:-1]), [])
                        for i, a in enumerate(primitive)
                    ]
                    full = [
                        a+sum((block[i] for block in blocks), [])
                        for i, a in enumerate(primitive)
                    ]
                    rank_primitive = base.rank(primitive, prime)
                    rank_without_highest = base.rank(without_highest, prime)
                    rank_full = base.rank(full, prime)
                    relation_dimension = scalar_columns-(rank_full-rank_without_highest)
                    results.append({
                        "prime": prime,
                        "order": order,
                        "primitive_degree": primitive_degree,
                        "primitive_pole_order": order+1,
                        "scalar_degree": scalar_degree,
                        "samples": len(used),
                        "rank_primitive": rank_primitive,
                        "rank_without_highest": rank_without_highest,
                        "rank_full": rank_full,
                        "highest_jet_relation_dimension": relation_dimension,
                        "genuine_relation_exists": relation_dimension > 0,
                    })
    for order in range(1, 4):
        expected = prior_rows(order)
        actual = {
            (row["prime"], row["primitive_degree"], row["scalar_degree"]):
            (row["rank_primitive"], row["rank_without_highest"],
             row["rank_full"], row["highest_jet_relation_dimension"])
            for row in results if row["order"] == order
        }
        regressions.append({"order": order, "matches_prior_packet": actual == expected})
    assert all(row["matches_prior_packet"] for row in regressions)
    output = {
        "schema": "marici.five_site.projective_krylov_ladder.v1",
        "max_order": MAX_ORDER,
        "max_degree": MAX_DEGREE,
        "primes": [1009, 1013],
        "regressions": regressions,
        "results": results,
        "scope": "Sampled closure modulo pole-order-(order+1) exact forms; degrees 0..3 only.",
        "interpretation": "Negative rows are replicated finite bounds, not a Gauss-Manin rank theorem.",
        "passed": True,
    }
    OUTPUT.write_text(json.dumps(output, indent=2)+"\n")
    print(json.dumps({
        "passed": True,
        "regressions": regressions,
        "positive_rows": sum(row["genuine_relation_exists"] for row in results),
        "row_count": len(results),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
