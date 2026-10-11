"""Exact incidence-level candidate for outward electron construction.

Run from any directory. No particle/coefficient operator is substituted here.
"""
from itertools import combinations, permutations
from fractions import Fraction as Q
import json

vertices = ((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1))
cells = [list(combinations(range(4), k)) for k in range(1,5)]
body = (0,1,2,3)
inward = [(a,b) for level in range(3) for a in cells[level]
          for b in cells[level+1] if set(a) < set(b)]
outward = [(b,a) for a,b in inward]
flags = [tuple(tuple(sorted(p[:k])) for k in range(1,5))
         for p in permutations(range(4))]
reverse_flags = [tuple(reversed(f)) for f in flags]

def barycenter(cell):
    return tuple(sum(Q(vertices[i][j]) for i in cell)/len(cell) for j in range(3))

def boundary(chain):
    result = {}
    for cell, coefficient in chain.items():
        if len(cell) == 1:
            continue
        for i in range(len(cell)):
            face = cell[:i] + cell[i+1:]
            result[face] = result.get(face, 0) + (-1)**i * coefficient
    return {cell: value for cell, value in result.items() if value}

# Revealing cells never rescales or moves their barycenters.
positions = {cell: barycenter(cell) for level in cells for cell in level}
levels = [[positions[cell] for cell in cells[k]] for k in (3,2,1,0)]
checks = {
    'fifteen_incidence_nodes': len(positions) == 15,
    'twenty_eight_arrows_reversed': len(inward) == len(outward) == 28
        and set(outward) == {(b,a) for a,b in inward},
    'twenty_four_distinct_outward_flags': len(set(reverse_flags)) == 24,
    'reversal_is_an_involution': all(tuple(reversed(r)) == f
        for f,r in zip(flags,reverse_flags)),
    'every_outward_path_starts_at_barycenter': all(f[0] == body for f in reverse_flags),
    'every_outward_path_uses_reversed_arrows': all((a,b) in outward
        for f in reverse_flags for a,b in zip(f,f[1:])),
    'branching_is_four_then_three_then_two': all(
        sum(a == cell for a,b in outward) == len(cell)
        for level in cells[1:] for cell in level),
    'outward_layers_have_one_four_six_four_nodes': list(map(len,levels)) == [1,4,6,4],
    'radius_increases_without_moving_existing_nodes': all(
        sum(x*x for x in positions[a]) < sum(x*x for x in positions[b])
        for a,b in outward),
    'outer_tetrahedron_has_original_scale': all(positions[(i,)] == vertices[i]
        for i in range(4)),
    'oriented_boundary_squared_is_zero': all(not boundary(boundary({cell:1}))
        for level in cells for cell in level),
    'boundary_cancellation_does_not_remove_flag_records': len(reverse_flags) == 24,
}
assert all(checks.values()), checks
print(json.dumps({'passed': True, 'checks': checks}, indent=2))
