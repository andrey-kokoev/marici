"""Test grade-six free-module prediction at A18 transport degree three."""
from __future__ import annotations
import json,sys
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research'/'voevodsky'))
import check_cosmology_filtered_quotient_colon_saturation as colon
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_grade_six_A18_degree_three.json'
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
 gate=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text());cols,inv,states=colon.build(18,tuple(gate['test_point_xyz']));z=json.loads((RES/'cosmology_filtered_A16_persistence_induction.json').read_text());a16=[x for x in z['A16_classes'] if x['grade']==6];lookup={(x['target_id'],x['axis_square']):x for x in a16};targets=sorted({x['target_id'] for x in a16})
 def shift(rec,axis):
  out={}
  for lab,v in row(rec).items():
   l=list(lab);e=list(l[-1]);e[axis]+=2;l[-1]=tuple(e);out[cols[tuple(l)]]=out.get(cols[tuple(l)],Fraction())+v
  return reduce(out,states[6]['basis'])
 canonical=[]
 for t in targets:
  xx,xy,yy=lookup[(t,'xx')],lookup[(t,'xy')],lookup[(t,'yy')];xxx=shift(xx,0);xxy=shift(xx,1);xyx=shift(xy,0);xyy=shift(xy,1);yyx=shift(yy,0);yyy=shift(yy,1);assert xxy==xyx and xyy==yyx;canonical += [xxx,xxy,xyy,yyy]
 r=rank(canonical);assert len(canonical)==16 and r==16
 out={'schema':'marici.voevodsky.cosmology-grade-six-A18-degree-three.v1','status':'free_commutative_orbit_through_degree_three','A18_canonical_orbit_count':16,'A18_span_rank':r,'mixed_path_coherence_checks':8,'additional_relations':0,'hilbert_ranks':[4,8,12,16],'decision':'The grade-six orbit matches a free rank-four Q[x2,y2]-module through transport degree three; A18 has sixteen independent canonical monomials and both mixed reorderings agree.','claim_boundary':'Finite degree-three evidence is not an all-degree freeness theorem.','next_gate':'derive-grade-six-freeness-induction-or-test-A20','passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
