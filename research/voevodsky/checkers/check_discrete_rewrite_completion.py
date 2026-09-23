"""Finite graded proof-rewrite completion; proposed path cells, not historical authority."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
from functools import lru_cache
import json
H=Q(1,2);ONE=Q(1)
# A proof trace stores the ordered positive surplus consumptions. Valid trace
# has total <= initial c, checked separately from rewriting syntax.
def successors(w):
 out=[]
 for i in range(len(w)-1):
  a,b=w[i:i+2]
  if a==H and b==H:out.append((w[:i]+(ONE,)+w[i+2:],'merge-two-halves'))
  if a==H and b==ONE:out.append((w[:i]+(ONE,H)+w[i+2:],'sort-one-before-half'))
 return out
@lru_cache(None)
def normal_forms(w):
 children=successors(w)
 if not children:return frozenset((w,))
 return frozenset(n for child,_ in children for n in normal_forms(child))
def expected(w):
 total=sum(w,Q(0));n=int(total);return (ONE,)*n+((H,) if total-n==H else ())
checked=0;branching=0;steps_checked=0
for length in range(7):
 for w in product((H,ONE),repeat=length):
  terms=normal_forms(w);assert terms==frozenset((expected(w),))
  if len(successors(w))>1:branching+=1
  # Every elementary rewrite preserves total surplus consumption and
  # decreases lexicographic measure (length, inversion count).
  inv=lambda v:sum(v[i]==H and v[j]==ONE for i in range(len(v)) for j in range(i+1,len(v)))
  for child,_ in successors(w):
   assert sum(child,Q(0))==sum(w,Q(0))
   assert (len(child),inv(child))<(len(w),inv(w))
   steps_checked+=1
  checked+=1
assert checked==127 and branching>0
# The same endpoint proof may have distinguishable trace records.
p=(H,H);q=(ONE,);assert normal_forms(p)==normal_forms(q) and p!=q
# Consume only within an independently declared primitive surplus c.
assert sum((ONE,H),Q(0))<=Q(3,2)
assert sum((ONE,ONE),Q(0))>Q(3,2)
report={'passed':True,'traces_checked':checked,'branching_critical_sources':branching,'rewrite_steps_checked':steps_checked,'unique_normal_trace':'descending unit then optional half, determined by total consumption','termination_measure':'(trace length, half-before-one inversions) decreases','history_not_identified_without_declared_3_cells':True,'scope':'Finite source-rooted half-unit trace grammar, bounded length <=6. Merge/swap cells are proposed generated higher relations; no owner authority, arbitrary rational termination, or analytic functor.'}
out=Path(__file__).resolve().parents[1]/'results/discrete-rewrite-completion.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
