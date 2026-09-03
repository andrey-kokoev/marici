"""Canonical A14 source-DAG closures for unresolved A12 transport squares."""
from __future__ import annotations
import json,os,sys
from pathlib import Path
os.environ['MARICI_AMBIENT']='12'
ROOT=Path(__file__).resolve().parents[2];sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
import check_cosmology_rank26_p_normal_K_q_seed_exact_rational_minor as exact
import cosmology_exact_source_certificate as certificate
import check_cosmology_source_word_axis_square_transport as naive
import check_cosmology_owned_IBP_q_source_certificates as owned
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_transported_source_dag_closure.json'
def main():
 old=rees.AMBIENT;rees.AMBIENT=14
 try:
  protocol=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(protocol['test_point_xyz']);nx=tuple(protocol['integral_unit_normals']['nx']);td=tuple(protocol['integral_unit_normals']['p_tangent_difference']);_,columns=rees.column_packet();packets={};orig=base.PRIME
  i14,k14,q14=naive.descs(14);all14=i14+k14+q14;nI=len(i14);nK=len(k14)
  for p in exact.PS:
   base.PRIME=p;raw=list(rees.raw_relations(point,columns));T,_=adapter.derivative_rows(columns,point,td);dx,_=adapter.derivative_rows(columns,point,nx);packets[p]={'T':T,'S_K':raw[nI:nI+nK],'Q':raw[nI+nK:],'dx':dx}
  base.PRIME=orig
 finally:rees.AMBIENT=old
 i12,k12,q12=naive.descs(12);all12=i12+k12+q12;decode={'T':all12,'S_K':k12,'Q':q12};index={'T':{d:i for i,d in enumerate(all14)},'S_K':{d:i for i,d in enumerate(k14)},'Q':{d:i for i,d in enumerate(q14)}}
 unresolved=json.loads((RES/'cosmology_corrected_source_word_transport.json').read_text())['unsolved_records'];wanted={(r['source_target_id'],r['family'],r['axis_square']) for r in unresolved};assert len(wanted)==len(unresolved)
 families=[('IBP','cosmology_IBP_exact_source_certificates_a12.json',('T',)),('K','cosmology_nonmarked_K_exact_seeds_a12.json',('T','S_K')),('q','cosmology_q_exact_source_certificates_a12.json',('T','Q'))];closures={};records=[];added_total=0
 for family,name,kinds in families:
  piv,nodes,creation=owned.origin_rows(kinds,packets);cache={}
  for record in json.loads((RES/name).read_text())['records']:
   c=record['source_certificate'];td=naive.target_desc(family,record)
   for axis,label in ((0,'x2'),(1,'y2')):
    if (c['canonical_target_id'],family,label) not in wanted:continue
    targetd=naive.shift(td,axis);ti=index['T'][targetd];origins,rows,target,cols,coef,rank=owned.exact_solve(ti,kinds,packets,piv,nodes,creation,cache)
    shifted={(k,index[k][naive.shift(decode[k][i],axis)]) for k,i in c['source_basis']};added=[list(o) for o in origins if o not in shifted];added_total+=len(added)
    cert=certificate.make({'family':family,'transport_of':c['canonical_target_id'],'axis_square':label,'target_descriptor':targetd},origins,rows,target,cols,coef,Path(__file__))
    records.append({'source_target_id':c['canonical_target_id'],'family':family,'axis_square':label,'transported_target_descriptor':targetd,'shifted_basis_size':len(shifted),'dag_basis_size':len(origins),'added_origins':added,'rank':rank,'source_certificate':cert})
 assert len(records)==len(wanted)
 out={'schema':'marici.voevodsky.cosmology-transported-source-dag-closure.v1','status':'all_unresolved_squares_closed_exactly_by_canonical_A14_DAG','records':records,'closure_count':len(records),'total_added_origin_occurrences':added_total,'selection_rule':'F_32003 pivot-ordered source DAG using family basis T; T+S_K; or T+Q, followed by four-prime exact lifting and rational solve','zero_residuals':len(records),'scope':'A12-to-A14 algebraic closures; pivot-order canonical relative to declared prime/order, not geometric support or a source differential','next_gate':'verify-transport-composition-A12-A14-A16','passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))
if __name__=='__main__':main()
