"""Verify marked-q sufficiency and canonical shift cutoff law at ambient degree 12 or 16."""
from __future__ import annotations
import json,sys
from itertools import product
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import g12_g31_residue_chart_transition as charts
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
import check_cosmology_rank26_p_normal_K_canonical_q_lifts as lifts
RES=ROOT/'research'/'voevodsky'/'results'; A=rees.AMBIENT; OUT=RES/f'cosmology_rank26_p_normal_K_q_ambient_a{A}.json'
def count(n):return len(base.monomials_at_most(n))
def add(d,k,v):
 v=(d.get(k,0)+v)%base.PRIME
 if v:d[k]=v
 else:d.pop(k,None)
def q_descriptors():
 out=[]
 for qi,name in enumerate(rees.NAMES):
  for kp in range(charts.K_DEPTH+1):
   for levels in product(range(1,charts.Q_DEPTH+1),repeat=len(rees.NAMES)):
    if levels[qi]==charts.Q_DEPTH:continue
    for exp in base.monomials_at_most(A-1):out.append({'mark':name,'k_pole':kp,'levels':levels,'exponent':exp})
 return out
def main():
 assert A in (12,16) and base.PRIME==32003
 protocol=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text()); point=tuple(protocol['test_point_xyz']); nx=tuple(protocol['integral_unit_normals']['nx']); td=tuple(protocol['integral_unit_normals']['p_tangent_difference'])
 _,columns=rees.column_packet(); special=list(rees.raw_relations(point,columns)); tangent,_=adapter.derivative_rows(columns,point,td); dx,_=adapter.derivative_rows(columns,point,nx)
 nI=4*count(A); nK=64*count(A-4); Kslice=slice(nI,nI+nK); qrows=special[nI+nK:]; targets=dx[Kslice]; qdesc=q_descriptors(); assert len(qdesc)==len(qrows)
 pivots={}
 for row in tangent+special[Kslice]:lifts.insert(row,pivots)
 base_pivots={p:(dict(r),{}) for p,(r,_c) in pivots.items()}
 for qi,row in enumerate(qrows):lifts.insert(row,pivots,{qi:1})
 # Full marked-q sufficiency.
 assert all(not base.reduce_row(row,{p:dict(r) for p,(r,_c) in pivots.items()}) for row in targets)
 Kdesc=[]
 for kp in range(charts.K_DEPTH):
  for levels in product(range(1,charts.Q_DEPTH+1),repeat=len(rees.NAMES)):
   for exp in base.monomials_at_most(A-4):Kdesc.append((kp,levels,exp))
 Kindex={d:i for i,d in enumerate(Kdesc)}; qkey={(d['mark'],d['k_pole'],tuple(d['levels']),tuple(d['exponent'])):i for i,d in enumerate(qdesc)}; levels=(1,1,2,1,1); poles={}
 for kp in (0,1):
  canonical_i=Kindex[(kp,levels,(0,0))]; prov=lifts.reduce_with_prov(targets[canonical_i],pivots); template=[(qdesc[i],a) for i,a in prov.items()]; interior=0; boundary=0; bad=0
  for shift in base.monomials_at_most(A-4):
   shifted=[]
   for d,a in template:
    exp=(d['exponent'][0]+shift[0],d['exponent'][1]+shift[1]); key=(d['mark'],d['k_pole'],tuple(d['levels']),exp)
    if key not in qkey:shifted=[];break
    shifted.append((qkey[key],a))
   predicted=sum(shift)<=A-7
   assert bool(shifted)==predicted
   if shifted:
    row=dict(targets[Kindex[(kp,levels,shift)]])
    for qi,a in shifted:
     for c,v in qrows[qi].items():add(row,c,a*v)
    if base.reduce_row(row,{p:dict(r) for p,(r,_c) in base_pivots.items()}):bad+=1
    interior+=1
   else:boundary+=1
  assert bad==0
  poles[f'k{kp}']={'canonical_q_rows':len(prov),'interior_shifts_verified':interior,'boundary_shifts_missing':boundary,'interior_max_degree':A-7,'boundary_degrees':[A-6,A-5,A-4]}
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-K-q-ambient-transport.v1','status':'marked_q_sufficiency_and_three_degree_boundary_verified','field':base.PRIME,'ambient_relation_degree':A,'all_nx_K_rows_absorbed_by_T_plus_S_K_plus_S_q':True,'poles':poles,'decision':'The degree-14 marked-q mechanism and cutoff law transport to this ambient degree.','limitations':['single prime','pivot-order-dependent canonical provenance','finite ambient degree','not an unbounded homotopy'],'passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
