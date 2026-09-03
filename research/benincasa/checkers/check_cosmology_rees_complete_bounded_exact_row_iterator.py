#!/usr/bin/env python3
"""Complete bounded exact Rees raw-row iterator and three-prime projection test."""
import hashlib,importlib,itertools,json,os,sys
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/benincasa';R=B/'results';sys.path.insert(0,str(B));assert json.loads((R/'cosmology_rees_exact_row_family_coverage.json').read_text())['passed']
POINT=(3,6,-3);A=4;NAMES=('g1','g2','g3','g23','g31')
def exact_fiber(x,y,z):
 e=x+y+z;x2,y2,z2,c2=x*x,y*y,z*z,e*e
 k={(4,0):x2,(2,2):-(x2+y2-z2),(0,4):y2,(2,0):x2*(x2-y2-z2)+c2*(y2-x2-z2),(0,2):y2*(y2-x2-z2)+c2*(x2-y2-z2),(0,0):z2*c2*c2+c2*z2*(z2-x2-y2)+z2*x2*y2}
 q=[{(0,1):1,(0,0):-y-z},{(1,0):1,(0,0):-x-z},{(1,0):1,(0,1):1,(0,0):z},{(0,1):1,(0,0):-x},{(1,0):1,(0,0):-y}];return k,q
def deriv(poly,axis):return {tuple(v-1 if i==axis else v for i,v in enumerate(t)):F(t[axis]*c) for t,c in poly.items() if t[axis]}
def shift(a,b):return tuple(x+y for x,y in zip(a,b))
def add(r,k,v):r[k]=r.get(k,F(0))+v
k,q=exact_fiber(*POINT);kd=[deriv(k,a) for a in range(2)];qd=[[deriv(poly,a) for a in range(2)] for poly in q]
def configure(p):
 os.environ.update(MARICI_FIELD_PRIME=str(p),MARICI_AMBIENT=str(A),MARICI_POINT='2,3,-5')
 for n in ['check_rank26_total_energy_triple_relation_module','g12_g31_residue_chart_transition','physical_four_mark_residue_twisted_derham']:sys.modules.pop(n,None)
 m=importlib.import_module('check_rank26_total_energy_triple_relation_module');m.charts.GAMMA=-(pow(2,-1,p))%p;return m
m0=configure(101);mons=m0.base.monomials_at_most;KD=m0.charts.K_DEPTH;QD=m0.charts.Q_DEPTH
def exact_rows():
 for kp in range(KD):
  for lev in itertools.product(range(1,QD+1),repeat=len(NAMES)):
   if any(v==QD for v in lev):continue
   for axis in range(2):
    for exp in mons(A):
     r={};
     if exp[axis]:d=list(exp);d[axis]-=1;add(r,(kp,*lev,tuple(d)),F(exp[axis]))
     for term,c in kd[axis].items():add(r,(kp+1,*lev,shift(exp,term)),(F(-1,2)-kp)*c)
     for qi,pole in enumerate(lev):
      raised=list(lev);raised[qi]+=1
      for term,c in qd[qi][axis].items():add(r,(kp,*raised,shift(exp,term)),F(-pole)*c)
     yield ('twisted_derivative',kp,lev,axis,exp),{x:v for x,v in r.items() if v}
 for kp in range(KD):
  for lev in itertools.product(range(1,QD+1),repeat=len(NAMES)):
   for exp in mons(A-4):
    r={(kp,*lev,exp):F(1)}
    for term,c in k.items():add(r,(kp+1,*lev,shift(exp,term)),F(-c))
    yield ('K_multiplication',kp,lev,exp),{x:v for x,v in r.items() if v}
 for qi,poly in enumerate(q):
  for kp in range(KD+1):
   for lev in itertools.product(range(1,QD+1),repeat=len(NAMES)):
    if lev[qi]==QD:continue
    raised=list(lev);raised[qi]+=1
    for exp in mons(A-1):
     r={(kp,*lev,exp):F(1)}
     for term,c in poly.items():add(r,(kp,*raised,shift(exp,term)),F(-c))
     yield ('q_multiplication',qi,kp,lev,exp),{x:v for x,v in r.items() if v}
rows=list(exact_rows());labels=[x[0] for x in rows];digest=hashlib.sha256('\n'.join(map(repr,labels)).encode()).hexdigest()
def proj(v,p):return v.numerator*pow(v.denominator,-1,p)%p
def compare(p):
 m=configure(p);_,cols=m.column_packet();actual=m.raw_relations(POINT,cols);mismatch=[];count=0
 for count,((label,row),got) in enumerate(itertools.zip_longest(rows,actual),1):
  if label is None or got is None:mismatch.append({'index':count-1,'kind':'length'});break
  want={cols[k]:proj(v,p) for k,v in row.items() if proj(v,p)}
  if want!=got:
   mismatch.append({'index':count-1,'label':repr(label),'residual_nnz':sum((got.get(c,0)-want.get(c,0))%p!=0 for c in set(got)|set(want))});break
 return {'prime':p,'rows_compared':count,'expected_rows':len(rows),'mismatch':mismatch,'matches':not mismatch and count==len(rows)}
comparisons=[compare(p) for p in [101,103,107]];assert all(c['matches'] for c in comparisons)
from collections import Counter
out={'schema':'marici.benincasa.cosmology-rees-complete-bounded-exact-row-iterator.v1','problem':'compare a complete labelled rational raw-row stream with the modular implementation','bold_conjecture':'one prime-independent exact iterator reproduces every bounded ambient-four raw_relations row in stable order','rivals':['representative-only compatibility','order or coefficient divergence in untested rows','complete rational stream'],'risky_consequences':'every row must have the same position and every projected sparse coefficient must match at three primes','strongest_falsification_attempt':{'ambient':A,'point':POINT,'row_count':len(rows),'family_counts':dict(Counter(x[0] for x in labels)),'label_digest':digest,'comparisons':comparisons},'exact_residual':'no length, order, or coefficient mismatch at 101, 103, or 107','conjecture_disposition':'retained for the complete ambient-four raw-row stream','exact_iterator_constructed':True,'modular_projection_verified':True,'integral_normalization':'multiply all rows by two clears the only half-twist denominator in this backend','scope':'raw source relations only; no complete exact row-reduction certificate or physical generator lift','next_conjecture':'the complete exact row stream supports an exact checkpointed elimination certificate whose modular reductions recover a stable target relation','next_falsifier':'run exact fraction-free elimination with labelled pivots and compare checkpoint projections against modular certificates','passed':True};(R/'cosmology_rees_complete_bounded_exact_row_iterator.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
