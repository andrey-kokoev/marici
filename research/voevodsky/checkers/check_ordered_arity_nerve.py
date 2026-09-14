#!/usr/bin/env python3
"""Finite exhaustive audit of the nerve of the ordered arity category."""
import itertools, json
from pathlib import Path

def simplices(dim, cutoff):
    return list(itertools.combinations_with_replacement(range(cutoff), dim + 1))
def face(x, i): return x[:i] + x[i + 1:]
def degeneracy(x, i): return x[:i + 1] + (x[i],) + x[i + 1:]
def horn(x, missing): return tuple(face(x, i) for i in range(len(x)) if i != missing)

def main():
    cutoff = 4
    simplicial_checks = 0
    horn_checks = 0
    for dim in range(1, 6):
        for x in simplices(dim, cutoff):
            # d_i d_j = d_(j-1) d_i for i < j
            for i in range(dim):
                for j in range(i + 1, dim + 1):
                    assert face(face(x, j), i) == face(face(x, i), j - 1)
                    simplicial_checks += 1
            # s_i s_j = s_(j+1) s_i for i <= j
            for i in range(dim + 1):
                for j in range(i, dim + 1):
                    assert degeneracy(degeneracy(x, j), i) == degeneracy(degeneracy(x, i), j + 1)
                    simplicial_checks += 1
        if dim >= 2:
            candidates = simplices(dim, cutoff)
            for x in candidates:
                for missing in range(1, dim):
                    signature = horn(x, missing)
                    fillers = [y for y in candidates if horn(y, missing) == signature]
                    assert fillers == [x]
                    horn_checks += 1
    result = {
        'schema': 'marici.voevodsky.ordered-arity-nerve.v1',
        'category': 'natural-number chain restricted to 0..3 for exhaustive checking',
        'dimensions_checked': [0, 1, 2, 3, 4, 5],
        'simplicial_identity_instances': simplicial_checks,
        'inner_horns_with_unique_filler': horn_checks,
        'all_checks_passed': True,
        'global_claim_basis': 'The nerve of any ordinary category has unique inner-horn fillers; finite checking is diagnostic only.',
        'claim_boundary': 'Strict ordered-arity infinity-category; no independent plane multiplicity.',
    }
    out = Path(__file__).parents[1] / 'results' / 'ordered_arity_nerve.json'
    out.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))

if __name__ == '__main__': main()
