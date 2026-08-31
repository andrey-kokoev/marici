#!/usr/bin/env python3
"""Exact finite-field sparse reduction carrying source-row provenance witnesses."""
import json
from pathlib import Path

PRIME = 32003
ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/aspect/results/sparse_provenance_reducer.json"

def clean(row): return {k: v % PRIME for k, v in row.items() if v % PRIME}
def add_scaled(dst, src, scale):
    out = dict(dst)
    for k, v in src.items(): out[k] = (out.get(k, 0) + scale * v) % PRIME
    return clean(out)
def inv(x): return pow(x % PRIME, PRIME - 2, PRIME)
def normalize(row, provenance):
    pivot = max(row); scale = inv(row[pivot])
    return add_scaled({}, row, scale), add_scaled({}, provenance, scale)
def reduce_pair(row, provenance, pivots):
    row, provenance = clean(row), clean(provenance)
    while row and max(row) in pivots:
        pivot = max(row); coefficient = row[pivot]
        prow, pprov = pivots[pivot]
        row = add_scaled(row, prow, -coefficient)
        provenance = add_scaled(provenance, pprov, -coefficient)
    return row, provenance
def reduce_rows(rows):
    pivots = {}; dependencies = []
    for source_id, source_row in enumerate(rows):
        row, provenance = reduce_pair(source_row, {source_id: 1}, pivots)
        if not row: dependencies.append(provenance); continue
        row, provenance = normalize(row, provenance)
        pivots[max(row)] = (row, provenance)
    return pivots, dependencies
def replay(rows, provenance):
    result = {}
    for source_id, coefficient in provenance.items(): result = add_scaled(result, rows[source_id], coefficient)
    return result

def reduce_against(rows, candidate):
    pivots, _ = reduce_rows(rows)
    return reduce_pair(candidate, {}, pivots)[0]

def shifted(row, width, block):
    return {column + block * width: value for column, value in row.items()}

def length_one_certificate(special_rows, dual_rows, triple_rows, generator, width):
    special_residual = reduce_against(special_rows, generator)
    t_generator = shifted(generator, width, 1)
    annihilation_residual = reduce_against(dual_rows, t_generator)
    t2_generator = shifted(generator, width, 2)
    triple_residual = reduce_against(triple_rows, t2_generator)
    return {
        "generator": generator,
        "nontrivial_mod_special": bool(special_residual),
        "special_residual": special_residual,
        "t_generator": t_generator,
        "annihilation_residual": annihilation_residual,
        "t2_generator": t2_generator,
        "triple_residual": triple_residual,
        "length_one_certified": bool(special_residual) and not annihilation_residual and not triple_residual,
    }

def main():
    rows = [{0: 1, 2: 1}, {0: 2, 2: 2}, {1: 1, 2: 1}, {0: 1, 1: -1}]
    pivots, dependencies = reduce_rows(rows)
    residuals = [replay(rows, witness) for witness in dependencies]
    assert dependencies and all(not residual for residual in residuals)
    corrupted = dict(dependencies[0]); corrupted[0] = (corrupted.get(0, 0) + 1) % PRIME
    deliberate_failure_residual = replay(rows, corrupted)
    assert deliberate_failure_residual
    # Toy Rees module: e1 survives the special quotient, while t*e1 is a
    # declared dual relation.  e0 is rejected because it is already special.
    width = 2; e0 = {0: 1}; e1 = {1: 1}
    special_rows = [e0]
    dual_rows = [shifted(e0, width, 0), shifted(e0, width, 1), shifted(e1, width, 1)]
    triple_rows = [shifted(e0, width, block) for block in range(3)] + [shifted(e1, width, 1), shifted(e1, width, 2)]
    incoherent_triple_rows = [row for row in triple_rows if row != shifted(e1, width, 2)]
    length_one = length_one_certificate(special_rows, dual_rows, triple_rows, e1, width)
    false_candidate = length_one_certificate(special_rows, dual_rows, triple_rows, e0, width)
    incoherent_candidate = length_one_certificate(special_rows, dual_rows, incoherent_triple_rows, e1, width)
    assert length_one["length_one_certified"]
    assert not false_candidate["length_one_certified"]
    assert not incoherent_candidate["length_one_certified"] and incoherent_candidate["triple_residual"]
    result = {
        "schema": "marici.aspect.sparse-provenance-reducer.result.v1",
        "prime": PRIME,
        "input_rows": rows,
        "pivot_count": len(pivots),
        "dependency_witnesses": dependencies,
        "replay_residuals": residuals,
        "deliberate_failure_residual": deliberate_failure_residual,
        "pair_operations_verified": True,
        "toy_length_one_certificate": length_one,
        "toy_false_candidate": false_candidate,
        "toy_incoherent_triple_candidate": incoherent_candidate,
        "length_one_selector_verified": True,
        "triple_filtration_coherence_verified": True,
        "production_rank26_extraction_completed": False,
        "next_gate": "port paired reduction and the special-nontrivial/dual-t-annihilated selector to the bounded Rust stream",
        "passed": True
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "passed", "dependencies": len(dependencies), "pivot_count": len(pivots)}))
if __name__ == "__main__": main()
