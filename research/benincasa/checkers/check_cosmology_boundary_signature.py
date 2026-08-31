"""Extract normalized boundary q-lift signatures at one ambient degree."""
from __future__ import annotations
import argparse,hashlib,json,os,sys
from itertools import product
from pathlib import Path
ap=argparse.ArgumentParser();ap.add_argument('--prime',type=int,required=True,choices=(32003,32009));ap.add_argument('--ambient',type=int,required=True,choices=(12,14,16));args=ap.parse_args();os.environ['MARICI_FIELD_PRIME']=str(args.prime);os.environ['MARICI_AMBIENT']=str(args.ambient)
ROOT=Path(__file__).resolve().parents[3]; sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import g12_g31_residue_chart_transition as charts
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
import check_cosmology_rank26_p_normal_K_canonical_q_lifts as lifts
RES=ROOT/'research'/'voevodsky'/'results'; A=rees.AMBIENT; OUT=ROOT/'research'/'benincasa'/'results'/f'cosmology_boundary_signatures_p{base.PRIME}_a{A}.json'
def count(n):return len(base.monomials_at_most(n))
def add(d,k,v):
 v=(d.get(k,0)+v)%base.PRIME
 if v:d[k]=v
 else:d.pop(k,None)
def qdesc():
 out=[]
 for qi,name in enumerate(rees.NAMES):
  for kp in range(charts.K_DEPTH+1):
   for levels in product(range(1,charts.Q_DEPTH+1),repeat=len(rees.NAMES)):
    if levels[qi]==charts.Q_DEPTH:continue
    for exp in base.monomials_at_most(A-1):out.append((name,kp,levels,exp))
 return out
def main():
 assert A in (12,14,16) and base.PRIME in (32003,32009)
 protocol=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text()); point=tuple(protocol['test_point_xyz']); nx=tuple(protocol['integral_unit_normals']['nx']); td=tuple(protocol['integral_unit_normals']['p_tangent_difference'])
 _,columns=rees.column_packet(); special=list(rees.raw_relations(point,columns)); tangent,_=adapter.derivative_rows(columns,point,td); dx,_=adapter.derivative_rows(columns,point,nx)
 nI=4*count(A);nK=64*count(A-4);targets=dx[nI:nI+nK];qrows=special[nI+nK:];qd=qdesc()
 pivots={}
 for row in tangent+special[nI:nI+nK]:lifts.insert(row,pivots)
 base_pivots={p:(dict(r),{}) for p,(r,_c) in pivots.items()}
 for qi,row in enumerate(qrows):lifts.insert(row,pivots,{qi:1})
 Kdesc=[]
 for kp in range(charts.K_DEPTH):
  for levels in product(range(1,charts.Q_DEPTH+1),repeat=len(rees.NAMES)):
   for exp in base.monomials_at_most(A-4):Kdesc.append((kp,levels,exp))
 Ki={d:i for i,d in enumerate(Kdesc)}; levels=(1,1,2,1,1);records=[]
 for kp in (0,1):
  for exp in [e for e in base.monomials_at_most(A-4) if sum(e)>=A-6]:
   ti=Ki[(kp,levels,exp)];prov=lifts.reduce_with_prov(targets[ti],pivots);check=dict(targets[ti]);signature=[]
   for qi,a in prov.items():
    for c,v in qrows[qi].items():add(check,c,a*v)
    mark,qkp,ql,qexp=qd[qi];signature.append((mark,qkp,ql,qexp[0]-exp[0],qexp[1]-exp[1],a))
   assert not base.reduce_row(check,{p:dict(r) for p,(r,_c) in base_pivots.items()})
   signature=tuple(sorted(signature));digest=hashlib.sha256(repr(signature).encode()).hexdigest();terms=[]
   for qi,a in sorted(prov.items()):
    mark,qkp,ql,qexp=qd[qi];terms.append({'mark':mark,'q_pole':qkp,'levels':list(ql),'exponent':list(qexp),'coefficient':a})
   records.append({'k_pole':kp,'exponent':list(exp),'relative_total_degree':sum(exp)-(A-6),'signature_sha256':digest,'q_rows':len(prov),'terms':terms})
 out={'schema':'marici.benincasa.cosmology-boundary-signatures.v1','status':'boundary_signatures_extracted','field':base.PRIME,'ambient_relation_degree':A,'boundary_degrees':[A-6,A-5,A-4],'records':records,'passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({**out,'records_count':len(records),'records':'omitted'},indent=2))
if __name__=='__main__':main()
