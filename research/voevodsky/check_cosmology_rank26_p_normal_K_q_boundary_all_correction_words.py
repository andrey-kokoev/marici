"""Back-substitute every adjacent boundary correction to original T and S_K rows."""
from __future__ import annotations
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
import check_cosmology_rank26_p_normal_lower_quartile_source_dag as dag
import check_cosmology_rank26_p_normal_K_q_boundary_correction_source_words as words
RES=ROOT/'research'/'voevodsky'/'results';A=rees.AMBIENT;OUT=RES/f'cosmology_rank26_p_normal_K_q_boundary_all_words_p{base.PRIME}_A{A-2}_to_A{A}.json'
def add(d,k,v):
 v=(d.get(k,0)+v)%base.PRIME
 if v:d[k]=v
 else:d.pop(k,None)
def main():
 assert A in (14,16) and base.PRIME in (32003,32009)
 sp=json.loads((RES/f'cosmology_rank26_p_normal_K_q_boundary_signatures_p{base.PRIME}_a{A-2}.json').read_text());tp=json.loads((RES/f'cosmology_rank26_p_normal_K_q_boundary_signatures_p{base.PRIME}_a{A}.json').read_text());tl={(r['k_pole'],*r['exponent']):r for r in tp['records']}
 protocol=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(protocol['test_point_xyz']);td=tuple(protocol['integral_unit_normals']['p_tangent_difference']);_,columns=rees.column_packet();special=list(rees.raw_relations(point,columns));tangent,_=adapter.derivative_rows(columns,point,td);nI=4*len(base.monomials_at_most(A));nK=64*len(base.monomials_at_most(A-4));SK=special[nI:nI+nK];qrows=special[nI+nK:];qd=words.qdesc();qkey={d:i for i,d in enumerate(qd)}
 pivots={};nodes={};creation=[]
 for i,row in enumerate(tangent):dag.add_pivot(row,pivots,nodes,creation,('T',i))
 for i,row in enumerate(SK):dag.add_pivot(row,pivots,nodes,creation,('S_K',i))
 records=[]
 for s in sp['records']:
  kp=s['k_pole'];i,j=s['exponent'];t=tl[(kp,i,j+2)];row={}
  for term in s['terms']:
   qi=qkey[(term['mark'],term['q_pole'],tuple(term['levels']),(term['exponent'][0],term['exponent'][1]+2))]
   for c,v in qrows[qi].items():add(row,c,term['coefficient']*v)
  for term in t['terms']:
   qi=qkey[(term['mark'],term['q_pole'],tuple(term['levels']),tuple(term['exponent']))]
   for c,v in qrows[qi].items():add(row,c,-term['coefficient']*v)
  coeff,trace=words.expand(row,pivots,nodes,creation);recon={}
  for (kind,index),a in coeff.items():
   for c,v in (tangent[index] if kind=='T' else SK[index]).items():add(recon,c,a*v)
  assert recon==row
  records.append({'k_pole':kp,'source_exponent':[i,j],'target_exponent':[i,j+2],'trace_length':trace,'source_rows':len(coeff),'coefficients':[{'kind':k[0],'row_index':k[1],'coefficient':a} for k,a in sorted(coeff.items())]})
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-K-q-boundary-all-correction-words.v1','status':'all_adjacent_boundary_correction_words_reconstructed','from_ambient':A-2,'to_ambient':A,'records':records,'record_count':len(records),'passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({**out,'records':'omitted'},indent=2))
if __name__=='__main__':main()
