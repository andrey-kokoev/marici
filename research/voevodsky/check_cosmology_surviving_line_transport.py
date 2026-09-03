"""Extract exact scalar transport laws on the surviving grade-7/8 x2 line."""
from __future__ import annotations
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_surviving_line_transport.json'
def freeze(x):return tuple(freeze(y) for y in x) if isinstance(x,list) else x
def row(r):return {freeze(t['column_label']):Fraction(t['numerator'],t['denominator']) for t in r['residual_terms']}
def scalar(r,ref):
 c=next(iter(ref));q=r.get(c,Fraction())/ref[c]
 assert {k:v for k,v in r.items() if v}=={k:q*v for k,v in ref.items() if q*v};return q
def enc(q):return {'numerator':q.numerator,'denominator':q.denominator}
def main():
 a=json.loads((RES/'cosmology_filtered_classification_transport.json').read_text());b=json.loads((RES/'cosmology_filtered_A16_persistence_induction.json').read_text());A14=a['A14_transports'];A16=b['A16_classes'];l16={(x['target_id'],x['axis_square']):x for x in A16};groups=[];patterns=[]
 for g in (7,8):
  sx=sorted([x for x in A14 if x['grade']==g and x['axis_square']=='x2'],key=lambda x:x['target_id']);sy=sorted([x for x in A14 if x['grade']==g and x['axis_square']=='y2'],key=lambda x:x['target_id']);ref14=row(sx[0]);m14=[scalar(row(x),ref14) for x in sx]
  src=sorted(sx+sy,key=lambda x:(x['axis_square'],x['target_id']));imgs=[l16[(x['target_id'],{'x2':'xx','y2':'yx'}[x['axis_square']])] for x in src];ref16=row(imgs[0]);m16=[scalar(row(x),ref16) for x in imgs];x16=m16[:len(sx)];y16=m16[len(sx):]
  assert all(a1==a2 for a1,a2 in zip(m14,x16));patterns.append((tuple(m14),tuple(y16)));groups.append({'grade':g,'A12_to_A14_x2_multipliers':[{'target_id':x['target_id'],'scalar':enc(q)} for x,q in zip(sx,m14)],'A14_to_A16_x2_multipliers':[{'target_id':x['target_id'],'source_path':x['axis_square'],'scalar':enc(q)} for x,q in zip(src,m16)],'x_path_recurrence':'identical scalar functional after representative normalization','y_path_scalar_vector':[enc(q) for q in y16]})
 same=patterns[0]==patterns[1]
 out={'schema':'marici.voevodsky.cosmology-surviving-line-transport.v1','status':'exact_stepwise_line_functionals_through_A16','groups':groups,'grade_independent':same,'x_path_functional_recurs_exactly':True,'decision':'Within each grade, the normalized x2 image functional recurs exactly on x2-generated paths at the second step. Grade independence is decided by exact scalar-vector comparison rather than assumed.','claim_boundary':'Two finite steps do not establish an all-even recurrence or a sourced module presentation.','next_gate':('test-surviving-line-recurrence-at-A18' if same else 'classify-grade-dependent-line-functionals'),'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='groups'},indent=2));print('patterns',[[[str(q) for q in p] for p in pattern] for pattern in patterns])
if __name__=='__main__':main()
