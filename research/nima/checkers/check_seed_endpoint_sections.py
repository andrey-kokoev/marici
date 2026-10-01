"""Enumerate seed endpoint sections; do not assume a promotion rule."""
from itertools import product, permutations

V = tuple('ABCD')
SEED = ('AB','BC','CA','AD','DB','BA')


def sections(edges, column):
    fibers = [[e for e in edges if e[column] == v] for v in V]
    return tuple(product(*fibers))


def audit(edges):
    outgoing = sections(edges,0)
    incoming = sections(edges,1)
    # A section is a witnessed choice per vertex, not an original edge.
    for choices in outgoing:
        assert tuple(e[0] for e in choices) == V
    for choices in incoming:
        assert tuple(e[1] for e in choices) == V
    # Simultaneous source and target section: a directed cycle cover.
    covers = tuple(s for s in outgoing if {e[1] for e in s} == set(V))
    return outgoing,incoming,covers


out,inc,covers = audit(SEED)
assert len(out) == len(inc) == 4
assert covers == (('AD','BC','CA','DB'),)
assert all(len(set(s)) == 4 for s in out+inc)
# Audit whether any source subset lacks enough distinct target neighbors.
def hall_defects(edges):
    result=[]
    for mask in range(1,16):
        subset={V[i] for i in range(4) if mask & (1<<i)}
        neighbors={e[1] for e in edges if e[0] in subset}
        if len(neighbors)<len(subset):
            result.append((''.join(sorted(subset)), ''.join(sorted(neighbors))))
    return result

assert not hall_defects(SEED)
# Pruning under the declared cycle-cover objective, not the full seed objective.
for e in SEED:
    remaining = tuple(x for x in SEED if x != e)
    _, _, reduced_covers = audit(remaining)
    assert bool(reduced_covers) == (e not in covers[0])
# Unique cover gives a reversible state permutation with period four.
forward = {e[0]:e[1] for e in covers[0]}
reverse = {v:u for u,v in forward.items()}
for v in V:
    assert reverse[forward[v]] == v
    w=v
    for _ in range(4):
        w=forward[w]
    assert w==v
assert any(reverse[v] != forward[v] for v in V)
# Its reverse edges are not all present in the original seed.
assert {v+u for u,v in forward.items()} - set(SEED) == {'DA','BD','AC','CB'}
# Uniqueness is natural under all state relabellings; no coordinate choice selects it.
for perm in permutations(V):
    relabel=dict(zip(V,perm))
    edges=tuple(relabel[e[0]]+relabel[e[1]] for e in SEED)
    _,_,cs=audit(edges)
    assert len(cs)==1
    assert set(cs[0]) == {relabel[e[0]]+relabel[e[1]] for e in covers[0]}
print('unique simultaneous section:', covers[0])
print('cycle-cover-only pruning removes AB and BA; four-cycle remains.')
full = tuple(a+b for a in V for b in V if a != b)
fout,finc,fcovers=audit(full)
assert len(fout)==len(finc)==81
assert len(fcovers)==9
assert not hall_defects(full)
print('seed: source sections',len(out),'target sections',len(inc),'cycle covers',len(covers))
print('source sections:',out)
print('target sections:',inc)
print('Hall defects:',hall_defects(SEED))
print('completed K4: source sections 81; target sections 81; cycle covers 9')
print('PASS: section counts and endpoint witnesses; no promotion or particle law assumed.')
