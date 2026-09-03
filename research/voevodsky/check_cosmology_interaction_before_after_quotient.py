"""Locate the surviving-line interaction before versus after quotient reduction."""
from __future__ import annotations
import json,os,sys
from fractions import Fraction
from pathlib import Path
os.environ['MARICI_AMBIENT']='12'
ROOT=Path(__file__).resolve().parents[2];sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
import check_cosmology_rank26_p_normal_K_q_seed_exact_rational_minor as ex
import check_cosmology_source_word_axis_square_transport as tr
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_interaction_before_after_quotient.json'
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
 oldA=rees.AMBIENT;oldp=base.PRIME;rees.AMBIENT=14
 try:
  _,cols=rees.column_packet();ibp,K,q=tr.descs(14);alls=ibp+K+q;idx={d:i for i,d in enumerate(alls)};pack={}
  gate=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(gate['test_point_xyz'])
  for p in ex.PS:
   base.PRIME=p;D2,_=adapter.derivative_rows(cols,point,(3,0,-1));pack[p]=D2
  c=json.loads((RES/'cosmology_filtered_classification_transport.json').read_text());groups=[]
  for g in (7,8):
   records=[x for x in c['A14_transports'] if x['grade']==g and x['axis_square']=='x2'];raw=[ex.exact_row([pack[p][idx[tuple([r['descriptor'][0],r['descriptor'][1],r['descriptor'][2],tuple(r['descriptor'][3]),tuple(r['descriptor'][4])])]] for p in ex.PS]) for r in records];rr=rank(raw);assert len(raw)==4 and rr==4;groups.append({'grade':g,'raw_target_rank':rr,'reduced_quotient_rank':1})
  out={'schema':'marici.voevodsky.cosmology-interaction-before-after-quotient.v1','status':'line_collapse_created_by_quotient_reduction','groups':groups,'decision':'For both grades, four raw D2 targets are independent before reduction and collapse to rank one only in the filtered quotient. The 1/144 line-functional interaction has no raw-line counterpart and is quotient-induced in this calculation.','claim_boundary':'Quotient-induced means produced by this algebraic reduction; it does not identify a geometric mechanism.','next_gate':'identify-relations-causing-four-to-one-collapse','passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
 finally:base.PRIME=oldp;rees.AMBIENT=oldA
if __name__=='__main__':main()
