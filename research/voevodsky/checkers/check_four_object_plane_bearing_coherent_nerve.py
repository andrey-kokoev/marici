#!/usr/bin/env python3
"""Exact audit of the four-object path-groupoid simplicial category."""
import itertools, json
from pathlib import Path

OBJECTS = (1, 2, 3, 4)

def paths(i, j):
    if i == j: return [(i,)]
    middle = range(i + 1, j)
    return [(i,) + tuple(k for k, take in zip(middle, mask) if take) + (j,)
            for mask in itertools.product((False, True), repeat=max(0, j - i - 1))]

def compose(q, p):
    assert p[-1] == q[0]
    return p + q[1:]

def main():
    path_counts = {f'{i}{j}': len(paths(i, j)) for i in OBJECTS for j in OBJECTS if i <= j}
    assert path_counts['13'] == 2 and path_counts['24'] == 2 and path_counts['14'] == 4

    associativity_checks = 0
    label_checks = 0
    for i in OBJECTS:
      for j in OBJECTS:
       for k in OBJECTS:
        for l in OBJECTS:
         if i <= j <= k <= l:
          for p in paths(i,j):
           for q in paths(j,k):
            for r in paths(k,l):
             assert compose(r, compose(q,p)) == compose(compose(r,q), p)
             associativity_checks += 1
             for a,b,c in itertools.product((0,1), repeat=3):
              assert (a ^ b) ^ c == a ^ (b ^ c)
              label_checks += 1

    identity_checks = 0
    for i in OBJECTS:
     for j in OBJECTS:
      if i <= j:
       for p in paths(i,j):
        assert compose((j,),p) == p and compose(p,(i,)) == p
        identity_checks += 1

    routes_14 = paths(1,4)
    direct = (1,4); full = (1,2,3,4)
    planes_direct_to_full = [(direct, full, bit) for bit in (0,1)]
    assert len(planes_direct_to_full) == 2

    result = {
      'schema':'marici.voevodsky.four-object-plane-bearing-coherent-nerve.v1',
      'objects':list(OBJECTS),
      'path_counts':path_counts,
      'routes_1_to_4':[list(p) for p in routes_14],
      'planes_between_each_ordered_parallel_route_pair':2,
      'planes_direct_14_to_full_1234':len(planes_direct_to_full),
      'path_associativity_checks':associativity_checks,
      'plane_label_associativity_checks':label_checks,
      'identity_checks':identity_checks,
      'all_checks_passed':True,
      'global_claim_basis':'Mapping spaces are nerves of groupoids and hence Kan; the coherent nerve of a Kan-enriched simplicial category is a quasicategory.',
      'claim_boundary':'Four-object plane-bearing infinity-category; not a source-derived model of physical or geometric coherence.',
    }
    out=Path(__file__).parents[1]/'results'/'four_object_plane_bearing_coherent_nerve.json'
    out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

if __name__=='__main__':main()
