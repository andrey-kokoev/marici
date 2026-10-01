"""Retain the full equivariant family of local reference choices.

Declared carrier symmetry is S4, with no retained square adjacency. Given a
cross-carrier endpoint pair, choose local arrows outward from each endpoint.
There are3*3 possible contexts. Each has137 counted slots. Keeping all contexts
is equivariant even though choosing a single context is not.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import permutations, product

V=tuple(range(4))
arrows=frozenset((a,b) for a,b in product(V,repeat=2) if a!=b)
states=frozenset(product(V,repeat=2))
perms=list(permutations(V))


def act(g,edge): return (g[edge[0]],g[edge[1]])


def contexts(a,b):
    return frozenset(((a,c),(b,d)) for c in V if c!=a for d in V if d!=b)


def slots(context):
    left,right=context
    result={('arrow',a,b) for a,b in product(arrows-{left},arrows-{right})}
    result.update(('state',a,b) for a,b in states)
    return frozenset(result)


root=(0,0)
family={context:slots(context) for context in contexts(*root)}
assert len(family)==9 and all(len(domain)==137 for domain in family.values())
counts=Counter(slot for domain in family.values() for slot in domain)
assert len(counts)==160 and sum(counts.values())==9*137
assert Counter(counts.values())==Counter({4:9,6:54,9:97})
# Shared fixed state tags are retained in every context. Primitive arrow pair
# retention probability depends on whether its legs start at the reference roots.
for (kind,a,b),multiplicity in counts.items():
    if kind=='state': assert multiplicity==9
    else:
        assert multiplicity==(2 if a[0]==0 else 3)*(2 if b[0]==0 else 3)
weights={slot:F(n,9*137) for slot,n in counts.items()}
assert sum(weights.values())==1
# Uniform context averaging is an explicit measure choice, not a selection.
assert sum(weight for (kind,_,_),weight in weights.items() if kind=='arrow')==F(121,137)
assert sum(weight for (kind,_,_),weight in weights.items() if kind=='state')==F(16,137)

# All rooted stabilizers act transitively on9 contexts and fix no single one.
stabilizer=[(g,h) for g,h in product(perms,repeat=2) if g[0]==h[0]==0]
first=min(family)
orbit={(act(g,first[0]),act(h,first[1])) for g,h in stabilizer}
assert orbit==set(family)
assert not [c for c in family if all((act(g,c[0]),act(h,c[1]))==c for g,h in stabilizer)]
# Whole-family covariance under all independent carrier relabellings, including
# reference-root movement. Every slot mask moves with its particular context.
for g,h in product(perms,repeat=2):
    transformed={}
    for context,domain in family.items():
        moved_context=(act(g,context[0]),act(h,context[1]))
        moved=frozenset((kind,act(g,a),act(h,b)) if kind=='arrow'
                        else (kind,g[a],h[b]) for kind,a,b in domain)
        assert moved==slots(moved_context)
        transformed[moved_context]=moved
    assert set(transformed)==contexts(g[0],h[0])

# Selecting a context is actual extra data: stabilizer reduces from36 to4.
chosen=min(family)
chosen_stabilizer=[(g,h) for g,h in stabilizer
                   if (act(g,chosen[0]),act(h,chosen[1]))==chosen]
assert len(chosen_stabilizer)==4
# Square-antipode rule fails the DECLARED S4 symmetry: exchange labels1 and3.
swap=(0,3,2,1)
assert swap[0]==0 and act(swap,(0,3))!=(0,3)
print('S4 carrier + endpoint reference:9 outward local-arrow contexts, no equivariant single choice.')
print('All9 contexts carry137 slots; the full choice family commutes with all576 independent relabellings.')
print('Retained contextual records=1233; underlying slot support=160, with multiplicities {4:9,6:54,9:97}.')
print('Uniform context mixing gives arrow-block mass121/137 and state-block mass16/137, with nonuniform underlying slot weights.')
print('Choosing one context reduces the reference stabilizer from36 to4; square-antipode selection fails S4 equivariance.')
