"""Test the grade-six orbit against a free Q[x2,y2]-module through degree two."""
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_grade_six_truncated_free_module.json'
def freeze(x):return tuple(freeze(y) for y in x) if isinstance(x,list) else x
def row(r):return {freeze(t['column_label']):Fraction(t['numerator'],t['denominator']) for t in r['residual_terms']}
def add(r,b,a):
 for c,v in b.items():
  z=r.get(c,Fraction())+a*v
  if z:r[c]=z
  else:r.pop(c,None)
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
 a=json.loads((RES/'cosmology_filtered_classification_transport.json').read_text());z=json.loads((RES/'cosmology_filtered_A16_persistence_induction.json').read_text());d0=[x for x in a['A12_classes'] if x['grade']==6];d1=[x for x in a['A14_transports'] if x['grade']==6];d2=[x for x in z['A16_classes'] if x['grade']==6];ranks=[rank(map(row,x)) for x in (d0,d1,d2)];assert [len(d0),len(d1),len(d2)]==[4,8,16] and ranks==[4,8,12]
 lookup={(x['target_id'],x['axis_square']):row(x) for x in d2};assert all(lookup[(t,'xy')]==lookup[(t,'yx')] for t in {x['target_id'] for x in d2})
 canonical=[x for x in d2 if x['axis_square']!='yx'];assert len(canonical)==12 and rank(map(row,canonical))==12
 out={'schema':'marici.voevodsky.cosmology-grade-six-truncated-free-module.v1','status':'free_commutative_orbit_through_degree_two','raw_orbit_counts':[4,8,16],'quotient_span_ranks':ranks,'mixed_commutativity_relations':4,'additional_relations':0,'decision':'The grade-six orbit agrees exactly with a free rank-four Q[x2,y2]-module in transport degrees 0,1,2: dimensions 4,8,12, with only xy=yx relations at degree two.','claim_boundary':'A degree-two Hilbert-function match is finite evidence, not an all-degree freeness theorem.','next_gate':'test-grade-six-free-module-at-A18-degree-three','passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
