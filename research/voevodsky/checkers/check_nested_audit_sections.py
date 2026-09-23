"""Test nested audit schemas using the owning conditional section implementation."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
import sys,json,hashlib
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/nima/checkers'))
from check_audited_tail_section import AuditedGenerator
OUT=ROOT/'research/voevodsky/results'
def observe(x):return sum(x),sum(h*Q(1,128**j) for j,h in enumerate(x))
def retract(x,A):
 g=AuditedGenerator(len(x),[(j,x[j]) for j in A]);s=g.section(observe(x))
 assert s['residual_membership']['admitted']
 y=tuple(g.coordinate(s,j) for j in range(len(x)))
 assert observe(y)==observe(x) and all(y[j]==x[j] for j in A)
 assert all(0<=h<=100+2*j for j,h in enumerate(y))
 return y
checks=0;failures=0;example=None
for m in (3,4,8,16):
 schemas=[(),(0,),tuple(sorted({0,m-1})),tuple(range(m))]
 for shift in range(3):
  x=tuple(Q((j+shift)%3) for j in range(m))
  for A,B in combinations(schemas,2):
   assert set(A)<=set(B)
   ra,rb=retract(x,A),retract(x,B)
   assert retract(rb,A)==ra # coarse observation is unchanged by finer contraction
   assert retract(ra,A)==ra and retract(rb,B)==rb
   reverse=retract(ra,B)
   if reverse!=rb:
    failures+=1
    if example is None:
     example={'m':m,'A':A,'B':B,'x':list(map(str,x)),
      'R_A_x':list(map(str,ra)),'R_B_x':list(map(str,rb)),
      'R_B_R_A_x':list(map(str,reverse))}
   for t in (Q(0),Q(1,2),Q(1)):
    hb=tuple((1-t)*a+t*b for a,b in zip(x,rb))
    assert retract(hb,A)==ra
    # Both selected lifts lie in the same coarse fiber, hence admit a coarse
    # straight-line comparison. This does not preserve the newly added audits.
    compare=tuple((1-t)*a+t*b for a,b in zip(ra,rb))
    assert observe(compare)==observe(x) and all(compare[j]==x[j] for j in A)
    checks+=1
assert example is not None
# Small explicit loss: finer schema fixes the entire fiber at x=(0,1,0).
x=(Q(0),Q(1),Q(0));A=();B=(0,)
a=retract(x,A);b=retract(x,B)
assert b==x and a[0]>0 and retract(a,B)==a
report={'passed':True,'nested_contraction_checks':checks,'noncommuting_retraction_cases':failures,
 'first_counterexample':example,
 'minimal_counterexample':{'x':list(map(str,x)),'A':A,'B':B,'coarse_center':list(map(str,a)),
 'fine_center':list(map(str,b)),'new_audit':'x_0=0','coarse_center_rejected_by_new_audit':True},
 'theorem':'For A subset B, R_A R_B=R_A and R_A H_B(-,t)=R_A. In general R_B R_A differs from R_B.',
 'interpretation':'R_B after R_A pins the changed representative values, not the original observed B values. Retaining original pins rejects an incompatible representative; it must not relabel its values as observations.',
 'coherence_scope':'Coarse-fiber straight-line comparison exists; preservation of newly added audits is not inferred.',
 'source_sha256':hashlib.sha256((ROOT/'research/nima/checkers/check_audited_tail_section.py').read_bytes()).hexdigest()}
(OUT/'nested-audit-sections.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
