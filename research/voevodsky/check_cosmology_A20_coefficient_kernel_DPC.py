"""DPC falsification test for coefficient-kernel recurrence at A20."""
import json,sys
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research'/'voevodsky'))
import check_cosmology_raw_q_collapse_certificates as c
s=c.s;RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_A20_coefficient_kernel_DPC.json'
def q(x):return Fraction(x['numerator'],x['denominator'])
def enc(x):return {'numerator':x.numerator,'denominator':x.denominator}
def main():
 oldA=s.rees.AMBIENT;oldp=s.base.PRIME;s.rees.AMBIENT=20
 try:
  _,cols=s.rees.column_packet();ibp,K,qr=s.tr.descs(20);alls=ibp+K+qr;nA=len(alls);nK=len(K);descs=alls+K+qr;grades=[s.clf.grade(d) for d in descs];point=tuple(json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text())['test_point_xyz']);pack={}
  for p in s.ex.PS:
   s.base.PRIME=p;raw=list(s.rees.raw_relations(point,cols));T,_=s.adapter.derivative_rows(cols,point,(1,-1,0));D2,_=s.adapter.derivative_rows(cols,point,(3,0,-1));pack[p]={'source':T+raw[len(ibp):len(ibp)+nK]+raw[len(ibp)+nK:],'target':D2}
  s.base.PRIME=oldp;exact=[s.ex.exact_row([pack[p]['source'][i] for p in s.ex.PS]) for i in range(len(descs))];basis={}
  for i in range(len(descs)):
   if grades[i]<=8:s.insert(exact[i],basis)
  z=json.loads((RES/'cosmology_filtered_A16_persistence_induction.json').read_text());base=[x for x in z['A16_classes'] if x['grade']==8 and x['axis_square']=='xx'];records=[]
  for x in base:
   d=tuple([x['descriptor'][0],x['descriptor'][1],x['descriptor'][2],tuple(x['descriptor'][3]),tuple(x['descriptor'][4])]);records.append({'target_id':x['target_id'],'descriptor':s.tr.shift(s.tr.shift(d,0),0)})
  idx={d:i for i,d in enumerate(alls)};reduced=[]
  for rec in records:
   t=s.ex.exact_row([pack[p]['target'][idx[rec['descriptor']]] for p in s.ex.PS]);reduced.append(s.reduce(t,basis))
  deps=c.relations(reduced);assert len(deps)==3;K20=[[dep.get(i,Fraction()) for i in range(4)] for dep in deps];a18=json.loads((RES/'cosmology_A18_raw_q_detector.json').read_text());K18=[[q(x) for x in row] for row in a18['relation_basis']];same=K20==K18
  out={'schema':'marici.voevodsky.cosmology-A20-coefficient-kernel-DPC.v1','status':('recurrence_corroborated_at_A20' if same else 'recurrence_falsified_at_A20'),'conjecture':'The normalized three-dimensional coefficient kernel remains unchanged at every even x-shift.','attempted_construction':'Build the exact A20 grade-eight quotient and reduce four x4 target rows.','A20_relation_basis':[[enc(x) for x in row] for row in K20],'same_as_A18':same,'DPC_disposition':('corroborated_through_A20; all-even theorem not established' if same else 'falsified by changed exact A20 relation basis'),'falsifier_witness':None if same else 'A20 normalized relation-basis coefficient mismatch','surviving_alternatives':['eventual change after A20','finite interpolation stabilization','true all-even kernel recurrence'],'next_gate':('derive-symbolic-kernel-recurrence' if same else 'classify-first-kernel-change-A20'),'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='A20_relation_basis'},indent=2))
 finally:s.base.PRIME=oldp;s.rees.AMBIENT=oldA
if __name__=='__main__':main()
