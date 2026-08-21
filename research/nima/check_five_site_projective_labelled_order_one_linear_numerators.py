#!/usr/bin/env python3
"""Pilot the first source-coordinate numerator grade of labelled primitives."""

import json
import os
import hashlib
from pathlib import Path

import numpy as np

import check_five_site_projective_labelled_order_one_exactness as constant
import check_five_site_projective_krylov_order_one as base

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "research/nima/results/five-site-projective-labelled-order-one-linear-numerators.json"
LABELS = constant.TERM_LABELS
NUMERATOR_BASIS = ("1", "u1", "u2", "u3")
PRIMITIVE_COLUMNS = len(LABELS)*3*len(NUMERATOR_BASIS)
SAMPLE_COUNT = int(os.environ.get("MARICI_LINEAR_NUMERATOR_SAMPLES", "700"))
SCALAR_DEGREES = tuple(
    int(value) for value in os.environ.get("MARICI_LINEAR_NUMERATOR_DEGREES", "0,1,2,3").split(",")
)
ROOTS_CACHE = {}


def sample_row(prime, seed):
    roots = ROOTS_CACHE.setdefault(prime, {x*x % prime: x for x in range(prime)})
    inv2 = base.trace.inv(2, prime)
    for off in range(20000):
        # A linear seed modulo p has at most p distinct states, which made
        # SAMPLE_COUNT > p impossible despite the four-dimensional sample
        # space.  Expand (prime, seed, offset) deterministically into four
        # independent field coordinates instead.
        digest = hashlib.blake2b(
            f"{prime}:{seed}:{off}".encode(), digest_size=32
        ).digest()
        coordinates = [
            int.from_bytes(digest[8*i:8*(i+1)], "little") % prime
            for i in range(4)
        ]
        u = coordinates[:3]
        t = coordinates[3]
        radicands, dr = base.r_data(u, prime)
        if any(value == 0 or value not in roots for value in radicands):
            continue
        ys0 = [roots[value] for value in radicands]
        term_value = [0]*len(LABELS)
        term_dt = [0]*len(LABELS)
        term_div = [[0, 0, 0] for _ in LABELS]
        complete = True
        for mask in range(32):
            ys = [(-y if mask & (1 << i) else y) % prime for i, y in enumerate(ys0)]
            sign = -1 if mask.bit_count() & 1 else 1
            dy = [[dr[i][j]*inv2*base.trace.inv(ys[i], prime) % prime
                   for i in range(5)] for j in range(3)]
            for term_index, labels in enumerate(LABELS):
                denominator = 1
                log_dt = 0
                log_du = [0, 0, 0]
                for label in labels:
                    value = base.trace.q_value(label, t, ys, prime)
                    if value == 0:
                        complete = False
                        break
                    denominator = denominator*value % prime
                    inverse = base.trace.inv(value, prime)
                    facet = base.trace.facets[label]
                    log_dt = (log_dt+sum(int(x) for x in facet["x"])*inverse) % prime
                    for j in range(3):
                        q_du = sum(int(b)*dy[j][i]
                                   for i, b in enumerate(facet["y"])) % prime
                        log_du[j] = (log_du[j]+q_du*inverse) % prime
                if not complete:
                    break
                value = base.trace.inv(denominator, prime)
                term_value[term_index] = (term_value[term_index]+sign*value) % prime
                term_dt[term_index] = (term_dt[term_index]-sign*value*log_dt) % prime
                for j in range(3):
                    term_div[term_index][j] = (
                        term_div[term_index][j]-sign*value*log_du[j]
                    ) % prime
            if not complete:
                break
        if not complete:
            continue
        y_product = 1
        for y in ys0:
            y_product = y_product*y % prime
        scale = base.trace.inv(32*y_product, prime)
        primitive = []
        for term_index in range(len(LABELS)):
            value = term_value[term_index]
            for j in range(3):
                div = term_div[term_index][j]
                primitive.append(div*scale % prime)
                for k in range(3):
                    # d_j(u_k R) = delta_jk R + u_k d_j R.
                    primitive.append(((value if j == k else 0)+u[k]*div)*scale % prime)
        return {
            "u": u,
            "t": t,
            "target": sum(term_value)*scale % prime,
            "target_dt": sum(term_dt)*scale % prime,
            "primitive": primitive,
        }
    raise RuntimeError("sample exhaustion")


def main():
    results = []
    for prime in (1009, 1013):
        samples = []
        keys = set()
        for seed in range(1, max(30000, 50*SAMPLE_COUNT)):
            try:
                sample = sample_row(prime, seed)
            except RuntimeError:
                continue
            key = (sample["t"], *sample["u"])
            if key not in keys:
                keys.add(key)
                samples.append(sample)
            if len(samples) == SAMPLE_COUNT:
                break
        assert len(samples) == SAMPLE_COUNT
        primitive_rows = [sample["primitive"] for sample in samples]
        rank_primitive = constant.modular_rank(primitive_rows, prime)
        conclusive = rank_primitive < SAMPLE_COUNT
        for scalar_degree in SCALAR_DEGREES:
            width = scalar_degree+1
            p0 = [[sample["target"]*pow(sample["t"], k, prime) % prime
                   for k in range(width)] for sample in samples]
            p1 = [[sample["target_dt"]*pow(sample["t"], k, prime) % prime
                   for k in range(width)] for sample in samples]
            without_dt = [a+b for a, b in zip(primitive_rows, p0)]
            full = [a+b+c for a, b, c in zip(primitive_rows, p0, p1)]
            rank_without_dt = constant.modular_rank(without_dt, prime)
            rank_full = constant.modular_rank(full, prime)
            relation_dimension = width-(rank_full-rank_without_dt)
            results.append({
                "prime": prime,
                "scalar_degree": scalar_degree,
                "samples": SAMPLE_COUNT,
                "primitive_columns": PRIMITIVE_COLUMNS,
                "rank_primitive": rank_primitive,
                "rank_without_dt": rank_without_dt,
                "rank_full": rank_full,
                "sample_rank_conclusive": conclusive,
                "dt_relation_dimension": relation_dimension,
                "genuine_order_one_relation_exists": conclusive and relation_dimension > 0,
            })
    output = {
        "schema": "marici.five_site.projective_labelled_order_one_linear_numerators.v1",
        "source_term_count": len(LABELS),
        "fiber_numerator_basis": list(NUMERATOR_BASIS),
        "primitive_columns": PRIMITIVE_COLUMNS,
        "requested_sample_count": SAMPLE_COUNT,
        "tested_scalar_degrees": list(SCALAR_DEGREES),
        "results": results,
        "scope": "First fiber-coordinate numerator grade; scalar coefficient degrees 0..3.",
        "passed": all(item["sample_rank_conclusive"] for item in results),
    }
    OUTPUT.write_text(json.dumps(output, indent=2)+"\n")
    print(json.dumps(output, sort_keys=True))


if __name__ == "__main__":
    main()
