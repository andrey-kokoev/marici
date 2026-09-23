"""Exhaustive finite public/fine-operation square; no authority or certificate transport."""
from itertools import combinations
from pathlib import Path
import json
P=frozenset(range(4)); L={0:0,1:0,2:1,3:1}; H=frozenset({0,2})
def subsets(xs):
 xs=list(xs)
 return [frozenset(k) for n in range(len(xs)+1) for k in combinations(xs,n)]
def image(C):return frozenset(L[x] for x in C)
def add(C,F):return frozenset(x for x in C if L[x] in F)
def fine(C):return C&H
states=subsets(P);frames=subsets({0,1});pairs=0
for C in states:
 for F in frames:
  assert image(add(C,F))==image(C)&F
  assert add(fine(C),F)==fine(add(C,F))
  pairs+=1
# Frozen two-fiber hostile: equal public image, opposite fine update admission.
C=frozenset({0});D=frozenset({1});assert image(C)==image(D)==frozenset({0})
assert image(fine(C))==frozenset({0}) and image(fine(D))==frozenset()
# Independent-image intersection would invent a shared witness.
assert image(D)&image(H)==frozenset({0}) and image(fine(D))==frozenset()
# Domain-relative qualification: if only public-saturated states are admitted,
# the effect is representative-independent, though H itself is not public.
saturated=[C for C in states if all((L[x]!=L[y] or (x in C)==(y in C)) for x in P for y in P)]
assert all(image(C)!=image(D) or image(fine(C))==image(fine(D)) for C in saturated for D in saturated)
assert any(fine(C) not in saturated for C in saturated)  # one-step descent is not closure under iterated fine updates
report={'passed':True,'source_points':len(P),'states':len(states),'public_square_cases':pairs,'two_fiber_fine_descent_fails':True,'restricted_saturated_domain_descends_one_step':True,'restricted_domain_not_closed_under_fine':True,'scope':'Finite set semantics only; no owner grant, session operation, certificate transport or universal representation theorem.'}
out=Path(__file__).resolve().parents[1]/'results/partial-operation-square.json'
out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
