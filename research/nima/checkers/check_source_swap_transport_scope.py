"""Finite source audit of the retained Boolean swap and its pointed scope.

Reads the existing Agda witness and image certificate; does not run Agda or
identify all carrier edges with that one witness.
"""
from itertools import permutations
from pathlib import Path
import hashlib
import json
import re

ROOT=Path(__file__).resolve().parents[3]
out=ROOT/'research/nima/results/source-swap-transport-scope.json'
out.unlink(missing_ok=True)
source=ROOT/'research/nima/agda/BoundaryGeneratedQuestions.agda'
series=ROOT/'research/nima/agda/RetainedComparisonSeries.agda'
s=source.read_text(encoding='utf-8'); t=series.read_text(encoding='utf-8')
assert 'Iso.fun swap-iso (x , y) = y , x' in s
assert 'Filler a b = Σ (El (retained a) ≃ El (retained b))' in s
assert '(λ e → equivFun e (value a) ≡ value b)' in s
assert 'swap-filler : Filler fourQ fourQ' in s
match=re.search(r'^swap-image-codes : .* ≡ \((\d+) , (\d+) , (\d+) , (\d+)\)$',t,re.M)
assert match
swap=tuple(map(int,match.groups()))
points=((False,False),(False,True),(True,False),(True,True))
assert swap==tuple(points.index((y,x)) for x,y in points)==(0,2,1,3)
G=tuple(permutations(range(4))); identity=tuple(range(4))

def compose(b,a): return tuple(b[a[i]] for i in range(4))
def inverse(a): return tuple(a.index(i) for i in range(4))
def conjugate(p,a): return compose(compose(p,a),inverse(p))
def transposition(i,j): return tuple(j if k==i else i if k==j else k for k in range(4))

pointed=tuple(g for g in G if g[0]==0)
assert len(pointed)==6 and swap in pointed
assert compose(swap,swap)==identity
flat_alternative=compose(swap,transposition(0,3))
assert flat_alternative not in pointed and flat_alternative[0]==3
orbit={conjugate(p,swap) for p in pointed}
assert orbit=={transposition(i,j) for i,j in ((1,2),(1,3),(2,3))}

# Reuse only conjugates of the actual involutive source witness. Its orbit
# supplies the spectator-preserving lift on the three unmarked states.
for i,j in permutations((1,2,3),2):
    candidates={conjugate(p,swap) for p in pointed if (p[1],p[2])==(i,j)}
    assert candidates=={transposition(i,j)}
    assert all(g[0]==0 for g in candidates)
    involutive={g for g in pointed if g[i]==j and compose(g,g)==identity}
    assert involutive==candidates
for i,j,k in permutations((1,2,3),3):
    loop=compose(transposition(k,i),compose(transposition(j,k),transposition(i,j)))
    assert loop==transposition(j,k)!=identity
    assert loop[0]==0 and loop[i]==i
    # Pointed value and truth-of-existence do not distinguish this from identity.
    assert tuple(loop[x] for x in range(4))!=identity

# Scope hostile: changing the boundary package's value changes admissibility.
# A filler Q_i->Q_j requires g(i)=j, not g(0)=0. Both unpointed lifts pass.
for i,j in permutations(range(4),2):
    spectators=[k for k in range(4) if k not in (i,j)]
    a=transposition(i,j)
    b=compose(a,transposition(*spectators))
    fillers=[g for g in G if g[i]==j]
    assert len(fillers)==6 and a in fillers and b in fillers
# Nor does the general fixed-package filler signature select an involution.
assert any(g in pointed and g!=identity and compose(g,g)!=identity for g in G)

result={
 'status':'passed',
 'classification':'source_swap_selects_spectator_preservation_only_in_its_pointed_involutive_sector',
 'obligation':'source-operation scope before identifying carrier edge transport',
 'source_images':list(swap),
 'source_hashes':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (source,series)},
 'checks':{'fixed_package_fillers':6,'source_swap_spectators_fixed':[0,3],
           'pointed_swap_conjugates':3,'nonidentity_unmarked_triangle_loops':6,
           'flat_double_swap_not_fixed_package_filler':True,
           'moving_boundary_packages_admit_both_lifts':True,
           'general_filler_signature_does_not_select_swap':True},
 'verdict':'An existing source witness supplies a nonflat pointed swap sector, but it does not select the transport of all carrier arrows or boundary-changing comparisons.',
 'unsupported':['carrier edges equal the chosen swap orbit','source transports of the distinguished point',
                'physical rung4 reference equals the Boolean distinguished value',
                'new Agda compilation or physical gauge interpretation'],
 'next_constructor':'Identify whether a carrier edge acts inside a fixed pointed package or compares packages with different distinguished values; specify its retained filler rather than only existence.'
}
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
