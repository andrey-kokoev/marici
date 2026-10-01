"""Readout/return descent across the nine rooted reference contexts.

Distinguish covariance with transported data, invariance at fixed physical data,
and ambiguity among relabellings that implement the same context change.
"""
from fractions import Fraction as F
from itertools import permutations, product
from collections import Counter
from biclique_complex import rank

V=range(4)
arrows=frozenset((a,b) for a,b in product(V,repeat=2) if a!=b)
contexts=tuple(product((1,2,3),repeat=2))  # marks are (0,a),(0,b)
G=[(g,h) for g,h in product(permutations(V),repeat=2) if g[0]==h[0]==0]
base=(1,1)


def domain(context):
    a,b=context
    return frozenset([('arrow',e,f) for e,f in product(arrows-{(0,a)},arrows-{(0,b)})]
                     +[('state',s,t) for s,t in product(V,repeat=2)])


def move_slot(slot,g,h):
    kind,a,b=slot
    if kind=='state': return kind,g[a],h[b]
    return kind,(g[a[0]],g[a[1]]),(h[b[0]],h[b[1]])


def move(values,g,h): return {move_slot(slot,g,h):value for slot,value in values.items()}
def mean(values,context): return sum((values[s] for s in domain(context)),F(0))/137
def update(values,context,delta):
    members=domain(context)
    return {s:v+(delta if s in members else 0) for s,v in values.items()}


ambient=frozenset().union(*(domain(c) for c in contexts))
x={s:F((i*i+3*i)%29,7) for i,s in enumerate(sorted(ambient))}
delta=F(2,5)
checks=0
for context in contexts:
    for g,h in G:
        target=(g[context[0]],h[context[1]])
        transported=move(x,g,h)
        assert mean(transported,target)==mean(x,context)
        assert move(update(x,context,delta),g,h)==update(transported,target,delta)
        assert sum((update(x,context,delta)[s]-x[s])**2 for s in ambient)==137*delta**2
        checks+=1

# Same context, multiple witnesses: the stabilizer acts on the retained slots.
H=[(g,h) for g,h in G if g[1]==h[1]==1]
assert len(H)==4
unseen=set(domain(base)); orbits=[]
while unseen:
    slot=min(unseen)
    orbit=frozenset(move_slot(slot,g,h) for g,h in H)
    assert orbit<=unseen
    unseen-=orbit; orbits.append(orbit)
assert len(orbits)==45
local={s:x[s] for s in domain(base)}
assert any(move(local,g,h)!=local for g,h in H)
# Orbit-mean projection is the Reynolds average over the ambiguity group.
averaged={s:sum(local[t] for t in orbit)/len(orbit) for orbit in orbits for s in orbit}
reynolds={s:F(0) for s in local}
for g,h in H:
    for s,v in move(local,g,h).items(): reynolds[s]+=v/len(H)
assert reynolds==averaged
for context in contexts:
    witnesses=[(g,h) for g,h in G if (g[1],h[1])==context]
    assert len(witnesses)==4
    transported=[move(averaged,g,h) for g,h in witnesses]
    assert all(value==transported[0] for value in transported)
    # Return to an orbit mean uses its transported cardinality/cost.
    g,h=witnesses[0]
    for orbit in orbits:
        shifted={s:v+(delta if s in orbit else 0) for s,v in averaged.items()}
        image=frozenset(move_slot(s,g,h) for s in orbit)
        expected={s:v+(delta if s in image else 0) for s,v in transported[0].items()}
        assert move(shifted,g,h)==expected
        assert sum((shifted[s]-averaged[s])**2 for s in orbit)==len(orbit)*delta**2

# Changing a reference mask while holding the ambient state fixed is different.
spike={s:F(s==('arrow',(0,1),(0,1))) for s in ambient}
fixed_means=Counter(mean(spike,c) for c in contexts)
assert fixed_means==Counter({F(0):5,F(1,137):4})
# Exact coupling of mean-return actions between contexts follows overlap counts.
gains=set()
for source,target in product(contexts,repeat=2):
    overlap=len(domain(source)&domain(target))
    equal_axes=sum(a==b for a,b in zip(source,target))
    assert overlap=={0:116,1:126,2:137}[equal_axes]
    assert mean(update(x,source,1),target)-mean(x,target)==F(overlap,137)
    gains.add(F(overlap,137))
# Nine indicator states on root-outgoing pairs already give a full-rank
# 9-by9 restriction of the context mean map (J3-I3) tensor (J3-I3), scaled.
columns=[]
for a,b in product((1,2,3),repeat=2):
    slot=('arrow',(0,a),(0,b))
    columns.append({i:F(1,137) for i,c in enumerate(contexts) if slot in domain(c)})
assert rank(columns)==9
# On the FULL retained primitive sphere, a vertex permutation acts on H2 by
# its orientation sign. Compute it using the actual tetrahedron boundary.
def sphere_degree(g):
    evaluation=F(0)
    for omitted in V:
        face=[g[v] for v in V if v!=omitted]
        if sorted(face)==[0,1,2]:
            inversions=sum(face[i]>face[j] for i in range(3) for j in range(i+1,3))
            evaluation+=F((-1)**(omitted+inversions))
    return -evaluation  # identity evaluates to -1 on the chosen primitive cycle

sign_actions={(sphere_degree(g),sphere_degree(h)) for g,h in H}
assert sign_actions==set(product((F(-1),F(1)),repeat=2))
# Both independent sphere generators reverse under some context stabilizer.
constraints=[]
for a,b in sign_actions:
    constraints.extend(({0:a-1},{1:b-1}))
assert rank(constraints)==2
assert all((a*F(2))**2+(b*F(3))**2==13 for a,b in sign_actions)
print('Full-carrier H2 context loops realize independent sign reversals of both sphere classes; fixed subspace dimension0, class-space rank2.')
print(f'{checks} exact context/data transport tests preserve means, uniform returns and induced costs.')
print('Each context change has4 witnesses; generic member data is witness-dependent.')
print('45 stabilizer orbits give a witness-independent mean interface; orbit-weighted returns transport exactly.')
print('At fixed ambient data, a single-slot example gives5 zero context means and4 means of1/137.')
print(f'Cross-context return gains: {sorted(gains)}; the9 context mean functionals are linearly independent.')
print('Descent of invariant interfaces and transport of complete labelled records are separate contracts.')
