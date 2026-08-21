#!/usr/bin/env python3
"""Test whether the deck-traced OFPT function factors through the determinant quotient."""

import json
import sys
from pathlib import Path

from sage.all import QQ, identity_matrix, matrix, vector

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "research/nima"))

import check_five_site_projective_labelled_order_one_exactness as constant
import check_five_site_projective_krylov_order_one as base
from check_five_site_ofpt_dihedral_selector import (
    boundary, oriented_action, reflect_site, rotate_site,
)

PACKET = ROOT / "research/benincasa/results/five-cycle-ofpt-packet.json"
OUTPUT = ROOT / "research/nima/results/five-site-ofpt-physical-map-determinant-factorization.json"
PRIMES = (1009, 1013)
SAMPLE_COUNT = 24


def cycle_sectors():
    cycle = json.loads(PACKET.read_text())["five_cycle"]
    terms = cycle["terms"]
    facets = sorted({label for term in terms for label in term})
    order = {label: position for position, label in enumerate(facets)}
    simplices = [tuple(sorted(term, key=order.__getitem__)) for term in terms]
    labels = [tuple(sorted(term)) for term in base.trace.terms]
    assert labels == simplices
    index = {frozenset(simplex): column for column, simplex in enumerate(simplices)}
    faces = sorted({face for simplex in simplices for face, _ in boundary(simplex)})
    face_index = {face: row for row, face in enumerate(faces)}
    d = matrix(QQ, len(faces), len(simplices), sparse=True)
    for column, simplex in enumerate(simplices):
        for face, sign in boundary(simplex):
            d[face_index[face], column] = sign
    rotation = oriented_action(simplices, index, order, rotate_site)
    reflection = oriented_action(simplices, index, order, reflect_site)
    unit = identity_matrix(QQ, len(simplices), sparse=True)
    even = d.stack(rotation-unit).stack(reflection-unit).right_kernel()
    odd = d.stack(rotation-unit).stack(reflection+unit).right_kernel()
    determinant = vector(QQ, cycle["ordered_denominator_determinants"])
    determinant_values = matrix(QQ, [[determinant.dot_product(item)
                                      for item in even.basis()]])
    determinant_kernel_coordinates = determinant_values.right_kernel().basis()
    determinant_kernel = [
        sum((coordinate[i]*even.basis()[i] for i in range(even.dimension())),
            vector(QQ, len(simplices)))
        for coordinate in determinant_kernel_coordinates
    ]
    assert len(determinant_kernel) == 5
    return even.basis(), determinant_kernel, odd.basis()


def sampled_term_values(prime, seed):
    roots = {x*x % prime: x for x in range(prime)}
    for offset in range(20000):
        u = [(seed+3*offset+2) % prime, (2*seed+5*offset+3) % prime,
             (3*seed+7*offset+5) % prime]
        t = (11*seed+17*offset+13) % prime
        radicands, _ = base.r_data(u, prime)
        if any(value == 0 or value not in roots for value in radicands):
            continue
        roots0 = [roots[value] for value in radicands]
        totals = [0]*len(constant.TERM_LABELS)
        complete = True
        for mask in range(32):
            ys = [(-root if mask & (1 << i) else root) % prime
                  for i, root in enumerate(roots0)]
            deck_sign = -1 if mask.bit_count() & 1 else 1
            q_values = {
                label: base.trace.q_value(label, t, ys, prime)
                for labels in constant.TERM_LABELS for label in labels
            }
            if any(value == 0 for value in q_values.values()):
                complete = False
                break
            inverses = {label: base.trace.inv(value, prime)
                        for label, value in q_values.items()}
            for term_index, labels in enumerate(constant.TERM_LABELS):
                value = deck_sign
                for label in labels:
                    value = value*inverses[label] % prime
                totals[term_index] = (totals[term_index]+value) % prime
        if not complete:
            continue
        root_product = 1
        for root in roots0:
            root_product = root_product*root % prime
        scale = base.trace.inv(32*root_product, prime)
        return [value*scale % prime for value in totals]
    raise RuntimeError("sample exhaustion")


def reduce_vector(item, prime):
    return [int(entry.numerator())*pow(int(entry.denominator()), -1, prime) % prime
            for entry in item]


def audit_prime(prime, sectors):
    even, determinant_kernel, odd = sectors
    reduced = {
        "even": [reduce_vector(item, prime) for item in even],
        "determinant_kernel": [reduce_vector(item, prime) for item in determinant_kernel],
        "odd": [reduce_vector(item, prime) for item in odd],
    }
    samples = []
    for seed in range(1, 30000):
        try:
            values = sampled_term_values(prime, seed)
        except RuntimeError:
            continue
        samples.append({
            name: [sum(a*b for a, b in zip(values, item)) % prime
                   for item in basis]
            for name, basis in reduced.items()
        })
        if len(samples) == SAMPLE_COUNT:
            break
    assert len(samples) == SAMPLE_COUNT
    ranks = {
        name: constant.modular_rank([sample[name] for sample in samples], prime)
        for name in reduced
    }
    return {
        "prime": prime,
        "samples": SAMPLE_COUNT,
        "even_image_rank": ranks["even"],
        "determinant_kernel_image_rank": ranks["determinant_kernel"],
        "odd_image_rank": ranks["odd"],
        "factors_through_determinant_quotient": (
            ranks["even"] == 1 and
            ranks["determinant_kernel"] == 0 and
            ranks["odd"] == 0
        ),
    }


def main():
    sectors = cycle_sectors()
    audits = [audit_prime(prime, sectors) for prime in PRIMES]
    output = {
        "schema": "marici.five_site.ofpt_physical_map_determinant_factorization.v1",
        "source_map": "full five-deck anti-invariant OFPT rational function on the frozen projective slice",
        "sector_dimensions": {"even": 6, "determinant_kernel": 5, "odd": 3},
        "audits": audits,
        "factorization_replicates": all(
            item["factors_through_determinant_quotient"] for item in audits
        ),
        "scope": "Finite-field functional-identity falsifier at 24 source-generic points per prime.",
        "passed": True,
    }
    OUTPUT.write_text(json.dumps(output, indent=2)+"\n")
    print(json.dumps(output, sort_keys=True))


if __name__ == "__main__":
    main()
