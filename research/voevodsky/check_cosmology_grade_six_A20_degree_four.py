"""Test grade-six free-module prediction at A20 transport degree four."""
from __future__ import annotations
import json,sys
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research'/'voevodsky'))
import check_cosmology_filtered_quotient_colon_saturation as colon
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_grade_six_A20_degree_four.json'
def freeze(x):return tuple(freeze(y) for y in x) if isinstance(x,list) else x
def row(r):return {freeze(t['column_label']):Fraction(t['numerator'],t['denominator']) for t in r['residual_terms']}
def add(r,b,a):
 for c,v in b.items():
  z=r.get(c,Fraction())+a*v
  if z:r[c]=z
  else:r.pop(c,None)
def reduce(r,b):
 r=dict(r)
 while r and min(r) in b:add(r,b[min(r)],-r[min(r)])
 return r
def rank(rows):
 b={}
 for raw in rows:
  r=dict(raw)
  while r:
   p=min(r)
   if p not in b:
    q=1/r[p];b[p]={c:v*q for c,v in r.items()};break
   add(r,b[p],-r[p])
 return len(b)
def main():
 gate=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text());cols,inv,states=colon.build(20,tuple(gate['test_point_xyz']));z=json.loads((RES/'cosmology_filtered_A16_persistence_induction.json').read_text());a16=[x for x in z['A16_classes'] if x['grade']==6];lookup={(x['target_id'],x['axis_square']):x for x in a16};targets=sorted({x['target_id'] for x in a16})
 def shift(rec,nx,ny):
  out={}
  for lab,v in row(rec).items():
   l=list(lab);e=list(l[-1]);e[0]+=2*nx;e[1]+=2*ny;l[-1]=tuple(e);out[cols[tuple(l)]]=out.get(cols[tuple(l)],Fraction())+v
  return reduce(out,states[6]['basis'])
 canonical=[];coherence=0
 for t in targets:
  xx,xy,yy=lookup[(t,'xx')],lookup[(t,'xy')],lookup[(t,'yy')];x4=shift(xx,2,0);x3y=shift(xx,1,1);x2y2=shift(xx,0,2);xy3=shift(yy,1,1);y4=shift(yy,0,2);assert x3y==shift(xy,2,0);assert x2y2==shift(xy,1,1)==shift(yy,2,0);assert xy3==shift(xy,0,2);coherence+=4;canonical += [x4,x3y,x2y2,xy3,y4]
 r=rank(canonical);assert len(canonical)==20 and r==20
 out={'schema':'marici.voevodsky.cosmology-grade-six-A20-degree-four.v1','status':'free_commutative_orbit_through_degree_four','A20_canonical_orbit_count':20,'A20_span_rank':r,'mixed_path_coherence_checks':coherence,'additional_relations':0,'hilbert_ranks':[4,8,12,16,20],'decision':'The grade-six orbit matches a free rank-four Q[x2,y2]-module through transport degree four; A20 has twenty independent canonical monomials.','claim_boundary':'Finite degree-four evidence is not an all-degree freeness theorem.','next_gate':'derive-grade-six-normal-form-induction','passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
