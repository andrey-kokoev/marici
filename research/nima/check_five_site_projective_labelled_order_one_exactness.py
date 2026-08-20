#!/usr/bin/env python3
"""Order-one exactness test in the source-labelled pole filtration."""

import json
from pathlib import Path

import numpy as np

import check_five_site_projective_krylov_order_one as base

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "research/nima/results/five-site-projective-labelled-order-one-exactness.json"
TERM_LABELS = [base.trace.common + term for term in base.trace.terms]
PRIMITIVE_COLUMNS = 3*len(TERM_LABELS)
SAMPLE_COUNT = PRIMITIVE_COLUMNS + 8 + 20


def sample_row(prime, seed):
    roots = {x*x % prime: x for x in range(prime)}
    inv2 = base.trace.inv(2, prime)
    for off in range(20000):
        u = [(seed+3*off+2) % prime, (2*seed+5*off+3) % prime,
             (3*seed+7*off+5) % prime]
        t = (11*seed+17*off+13) % prime
        radicands, dr = base.r_data(u, prime)
        if any(value == 0 or value not in roots for value in radicands):
            continue
        ys0 = [roots[value] for value in radicands]
        target = target_dt = 0
        primitive = [0]*PRIMITIVE_COLUMNS
        complete = True
        for mask in range(32):
            ys = [(-y if mask & (1 << i) else y) % prime for i, y in enumerate(ys0)]
            sign = -1 if mask.bit_count() & 1 else 1
            dy = [
                [dr[i][j]*inv2*base.trace.inv(ys[i], prime) % prime for i in range(5)]
                for j in range(3)
            ]
            for term_index, labels in enumerate(TERM_LABELS):
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
                    a = sum(int(x) for x in facet["x"]) % prime
                    log_dt = (log_dt+a*inverse) % prime
                    for j in range(3):
                        q_du = sum(int(b)*dy[j][i] for i, b in enumerate(facet["y"])) % prime
                        log_du[j] = (log_du[j]+q_du*inverse) % prime
                if not complete:
                    break
                value = base.trace.inv(denominator, prime)
                target = (target+sign*value) % prime
                target_dt = (target_dt-sign*value*log_dt) % prime
                for j in range(3):
                    index = 3*term_index+j
                    primitive[index] = (primitive[index]-sign*value*log_du[j]) % prime
            if not complete:
                break
        if not complete:
            continue
        y_product = 1
        for y in ys0:
            y_product = y_product*y % prime
        scale = base.trace.inv(32*y_product, prime)
        return {
            "u": u,
            "t": t,
            "target": target*scale % prime,
            "target_dt": target_dt*scale % prime,
            "primitive": [value*scale % prime for value in primitive],
        }
    raise RuntimeError("sample exhaustion")


def modular_rank(rows, prime):
    matrix = np.asarray(rows, dtype=np.int64) % prime
    row_count, column_count = matrix.shape
    pivot_row = 0
    for column in range(column_count):
        candidates = np.flatnonzero(matrix[pivot_row:, column])
        if candidates.size == 0:
            continue
        pivot = pivot_row+int(candidates[0])
        if pivot != pivot_row:
            matrix[[pivot_row, pivot]] = matrix[[pivot, pivot_row]]
        matrix[pivot_row] = matrix[pivot_row]*pow(int(matrix[pivot_row, column]), prime-2, prime) % prime
        factors = matrix[:, column].copy()
        factors[pivot_row] = 0
        nonzero = np.flatnonzero(factors)
        if nonzero.size:
            matrix[nonzero] = (
                matrix[nonzero]-factors[nonzero, None]*matrix[pivot_row][None, :]
            ) % prime
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def main():
    results = []
    for prime in (1009, 1013):
        samples = []
        keys = set()
        for seed in range(1, 20000):
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
        rank_primitive = modular_rank(primitive_rows, prime)
        for scalar_degree in range(4):
            scalar_columns = scalar_degree+1
            p0 = [
                [sample["target"]*pow(sample["t"], k, prime) % prime
                 for k in range(scalar_columns)] for sample in samples
            ]
            p1 = [
                [sample["target_dt"]*pow(sample["t"], k, prime) % prime
                 for k in range(scalar_columns)] for sample in samples
            ]
            without_dt = [a+b for a, b in zip(primitive_rows, p0)]
            full = [a+b+c for a, b, c in zip(primitive_rows, p0, p1)]
            rank_without_dt = modular_rank(without_dt, prime)
            rank_full = modular_rank(full, prime)
            relation_dimension = scalar_columns-(rank_full-rank_without_dt)
            results.append({
                "prime": prime,
                "scalar_degree": scalar_degree,
                "samples": len(samples),
                "primitive_columns": PRIMITIVE_COLUMNS,
                "rank_primitive": rank_primitive,
                "rank_without_dt": rank_without_dt,
                "rank_full": rank_full,
                "dt_relation_dimension": relation_dimension,
                "genuine_order_one_relation_exists": relation_dimension > 0,
            })
    output = {
        "schema": "marici.five_site.projective_labelled_order_one_exactness.v1",
        "source_term_count": len(TERM_LABELS),
        "primitive_directions_per_term": 3,
        "primitive_columns": PRIMITIVE_COLUMNS,
        "construction": (
            "Cover-level divergence of one primitive per source term and fiber direction; "
            "weight-five Fourier trace and y-product descent applied afterward."
        ),
        "results": results,
        "scope": "Constant-numerator labelled primitives; scalar coefficient degrees 0..3.",
        "passed": True,
    }
    OUTPUT.write_text(json.dumps(output, indent=2)+"\n")
    print(json.dumps(output, sort_keys=True))


if __name__ == "__main__":
    main()
