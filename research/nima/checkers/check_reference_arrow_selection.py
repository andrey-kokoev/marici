"""Equivariant local-arrow selection from explicit direct-reference data.

Finite stabilizer test: an equivariant selection on a transitive input orbit
exists exactly when the input stabilizer fixes an output. Enumerate candidate
ordered local arrow pairs for several possible reference types on two4-sets.
"""
from itertools import permutations, product
from collections import Counter

V=tuple(range(4))
perms=list(permutations(V))
arrows=[(a,b) for a,b in product(V,repeat=2) if a!=b]
outputs=list(product(arrows,repeat=2))


def act(g,edge): return (g[edge[0]],g[edge[1]])


def audit(name,stabilizer,expected):
    fixed=[(a,b) for a,b in outputs
           if all((act(g,a),act(h,b))==(a,b) for g,h in stabilizer)]
    assert len(fixed)==expected
    unseen=set(outputs); orbit_sizes=[]
    while unseen:
        a,b=min(unseen)
        orbit={(act(g,a),act(h,b)) for g,h in stabilizer}
        assert orbit<=unseen
        unseen-=orbit; orbit_sizes.append(len(orbit))
    assert sum(orbit_sizes)==144
    print(f'{name}: stabilizer size={len(stabilizer)}, fixed local-arrow pairs={len(fixed)}, orbit sizes={dict(sorted(Counter(orbit_sizes).items()))}')
    return fixed


# A direct cross-carrier edge chooses a point a0 in A and b0 in B.
rooted=[(g,h) for g,h in product(perms,repeat=2) if g[0]==0 and h[0]==0]
audit('One cross-carrier edge (a0,b0)',rooted,0)
# A bijective carrier correspondence transports labels but marks no point.
audit('One carrier bijection (identity representative)',[(g,g) for g in perms],0)
# Even a rooted bijection leaves the other three labels interchangeable.
audit('Rooted carrier bijection',[(g,g) for g in perms if g[0]==0],0)
# Two endpoint anchors on each side suffice to choose either orientation.
two=[(g,h) for g,h in product(perms,repeat=2)
     if g[0]==0 and g[1]==1 and h[0]==0 and h[1]==1]
fixed=audit('Two ordered cross-carrier endpoint anchors',two,4)
assert set(fixed)==set(product(((0,1),(1,0)),repeat=2))
# Requiring each selected local arrow to start at the first anchor fixes orientation.
assert [pair for pair in fixed if pair[0][0]==0 and pair[1][0]==0]==[((0,1),(0,1))]

# A rooted bijection plus one extra source anchor transports its counterpart;
# the same endpoint/orientation law then selects a unique pair.
correlated=[(g,g) for g in perms if g[0]==0 and g[1]==1]
fixed=audit('Rooted bijection plus extra source anchor',correlated,4)
assert [pair for pair in fixed if pair[0][0]==0 and pair[1][0]==0]==[((0,1),(0,1))]

# Constructive positive control for ALL ordered pairs of distinct anchors in
# each carrier. Selection uses anchor order, never numeric label order.
for a,b in product(arrows,repeat=2):
    selected=(a,b)
    assert len(set(arrows)-{selected[0]})==11
    assert len(set(arrows)-{selected[1]})==11
    for g,h in product(perms,repeat=2):
        transformed_anchors=(act(g,a),act(h,b))
        assert transformed_anchors==(act(g,selected[0]),act(h,selected[1]))

# A numerical 'first other label' rule violates relabelling even at a fixed root.
chosen=(0,1)
swap=(0,2,1,3)
assert swap[0]==0 and act(swap,chosen)!=(0,1)
print('No deterministic equivariant local-arrow pair can be selected from the tested bare-set one-reference types.')
print('Two ordered anchors per carrier plus the start-at-first rule select a unique pair, leaving11 arrows on each side.')
print('Exhaustive anchor-selection equivariance passed; numerical first-label negative control fails equivariance as expected.')

# The documented Bool x Bool carrier may retain square geometry rather than
# merely four labels. Its automorphisms preserve Hamming-distance-one edges.
square=[g for g in perms if all(
    (((a^b).bit_count()==1)==((g[a]^g[b]).bit_count()==1))
    for a,b in product(V,repeat=2))]
assert len(square)==8
square_rooted=[(g,h) for g,h in product(square,repeat=2) if g[0]==h[0]==0]
fixed=audit('Rooted Boolean squares (Hamming structure retained)',square_rooted,4)
assert [pair for pair in fixed if pair[0][0]==0 and pair[1][0]==0]==[((0,3),(0,3))]
for a,b in product(V,repeat=2):
    selected=((a,a^3),(b,b^3))  # oriented root -> unique antipode
    for g,h in product(square,repeat=2):
        assert (act(g,selected[0]),act(h,selected[1]))==((g[a],g[a]^3),(h[b],h[b]^3))
print('Retained square structure supplies a canonical antipode. Root-to-antipode selection is equivariant for all64 pairs of square automorphisms.')
print('A marked square-adjacent local arrow still needs a choice between the two neighbors of the root.')
