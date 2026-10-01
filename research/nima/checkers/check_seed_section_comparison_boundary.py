"""Compare actual seed sections under declared filler policies.
Finite set analogue of pointed fillers, not a new Agda or physical theorem.
"""
from itertools import permutations, product

V=tuple('ABCD')
E=('AB','BC','CA','AD','DB','BA')
sections=tuple(product(*[tuple(e for e in E if e[0]==v) for v in V]))
cycle=('AD','BC','CA','DB')
other=('AB','BC','CA','DB')
assert len(sections)==4
# Generic pointed equivalences of the four-value source-section carrier.
i,j=sections.index(cycle),sections.index(other)
fillers=[p for p in permutations(range(4)) if p[i]==j]
assert len(fillers)==6
# Candidate stricter policy: comparisons induced by automorphisms of the seed.
autos=[]
for values in permutations(V):
    p=dict(zip(V,values))
    if {p[e[0]]+p[e[1]] for e in E}==set(E):
        autos.append(p)
assert len(autos)==2

def transport(section,p):
    moved={p[e[0]]:p[e[0]]+p[e[1]] for e in section}
    return tuple(moved[v] for v in V)

assert all(transport(cycle,p)==cycle for p in autos)
assert not any(transport(cycle,p)==other for p in autos)
# A named structural observation: number of distinct targets of a section.
def target_count(section):
    return len({e[1] for e in section})
assert target_count(cycle)==4 and target_count(other)==3
assert all(target_count(transport(s,p))==target_count(s) for s in sections for p in autos)
# No full-domain reader-preserving pointed bijection can identify these two.
observed=[p for p in fillers if all(target_count(sections[p[k]])==target_count(s)
                                  for k,s in enumerate(sections))]
assert not observed
# Distinction is not dynamics: shared witness overlap and discrepancy are explicit.
assert set(cycle)&set(other)=={'BC','CA','DB'}
assert set(cycle)-set(other)=={'AD'}
assert set(other)-set(cycle)=={'AB'}
print('PASS: four source sections; six unrestricted pointed comparison fillers.')
print('PASS: two seed automorphisms; zero induced fillers between the chosen sections.')
print('PASS: target-image reader distinguishes 4 versus 3; no reader-preserving filler.')
print('Shared arrows BC,CA,DB; replacement AD -> AB is not a seed symmetry.')
print('Scope: declared comparison policies; neither rejection nor overlap supplies an interaction law.')
