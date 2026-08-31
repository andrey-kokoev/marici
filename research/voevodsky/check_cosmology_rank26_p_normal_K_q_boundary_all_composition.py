"""Verify direct-versus-composite source-word coherence for all A12 boundary coordinates."""
from __future__ import annotations
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
import check_cosmology_rank26_p_normal_lower_quartile_source_dag as dag
import check_cosmology_rank26_p_normal_K_q_boundary_correction_source_words as words
import check_cosmology_rank26_p_normal_K_q_correction_word_ambient_compatibility as compat
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/f'cosmology_rank26_p_normal_K_q_boundary_all_composition_p{base.PRIME}.json'
def add(d,k,v):
 v=(d.get(k,0)+v)%base.PRIME
 if v:d[k]=v
 else:d.pop(k,None)
def evaluate(coeff,T,SK):
 row={}
 for (kind,index),a in coeff.items():
  for c,v in (T[index] if kind=='T' else SK[index]).items():add(row,c,a*v)
 return row
def main():
 assert rees.AMBIENT==16 and base.PRIME in (32003,32009)
 q12=json.loads((RES/f'cosmology_rank26_p_normal_K_q_boundary_signatures_p{base.PRIME}_a12.json').read_text());q16=json.loads((RES/f'cosmology_rank26_p_normal_K_q_boundary_signatures_p{base.PRIME}_a16.json').read_text());w14=json.loads((RES/f'cosmology_rank26_p_normal_K_q_boundary_all_words_p{base.PRIME}_A12_to_A14.json').read_text());w16=json.loads((RES/f'cosmology_rank26_p_normal_K_q_boundary_all_words_p{base.PRIME}_A14_to_A16.json').read_text());L14={(r['k_pole'],*r['source_exponent']):r for r in w14['records']};L16={(r['k_pole'],*r['source_exponent']):r for r in w16['records']};d14,sk14=compat.descriptors(14);d16,sk16=compat.descriptors(16);Ti={d:i for i,d in enumerate(d16)};SKi={d:i for i,d in enumerate(sk16)}
 protocol=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(protocol['test_point_xyz']);td=tuple(protocol['integral_unit_normals']['p_tangent_difference']);_,columns=rees.column_packet();special=list(rees.raw_relations(point,columns));T,_=adapter.derivative_rows(columns,point,td);nI=4*len(base.monomials_at_most(16));nK=64*len(base.monomials_at_most(12));SK=special[nI:nI+nK];qrows=special[nI+nK:];qd=words.qdesc();qkey={d:i for i,d in enumerate(qd)}
 pivots={};nodes={};creation=[]
 for i,row in enumerate(T):dag.add_pivot(row,pivots,nodes,creation,('T',i))
 for i,row in enumerate(SK):dag.add_pivot(row,pivots,nodes,creation,('S_K',i))
 t16={(r['k_pole'],*r['exponent']):r for r in q16['records']};failures=[];strict=0;direct_sizes=[]
 for s in q12['records']:
  kp=s['k_pole'];i,j=s['exponent'];target=t16[(kp,i,j+4)];row={}
  for term in s['terms']:
   qi=qkey[(term['mark'],term['q_pole'],tuple(term['levels']),(term['exponent'][0],term['exponent'][1]+4))]
   for c,v in qrows[qi].items():add(row,c,term['coefficient']*v)
  for term in target['terms']:
   qi=qkey[(term['mark'],term['q_pole'],tuple(term['levels']),tuple(term['exponent']))]
   for c,v in qrows[qi].items():add(row,c,-term['coefficient']*v)
  direct,_=words.expand(row,pivots,nodes,creation);composite={}
  for item in L14[(kp,i,j)]['coefficients']:
   d=(d14 if item['kind']=='T' else sk14)[item['row_index']];f,qk,l,ax,m,e=d;sd=(f,qk,l,ax,m,(e[0],e[1]+2));idx=(Ti if item['kind']=='T' else SKi)[sd];add(composite,(item['kind'],idx),item['coefficient'])
  for item in L16[(kp,i,j+2)]['coefficients']:add(composite,(item['kind'],item['row_index']),item['coefficient'])
  assert evaluate(direct,T,SK)==row and evaluate(composite,T,SK)==row
  if direct==composite:strict+=1
  else:failures.append({'k_pole':kp,'exponent':[i,j],'coefficient_difference_terms':len(set(direct)|set(composite))})
  direct_sizes.append(len(direct))
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-K-q-boundary-all-composition.v1','status':'all_boundary_corrections_compose_strictly' if not failures else 'some_boundary_corrections_only_cohere_by_syzygy','rows_tested':len(q12['records']),'strict_coefficient_matches':strict,'failures':failures,'direct_source_rows_min':min(direct_sizes),'direct_source_rows_max':max(direct_sizes),'decision':'All direct and composite original-source coefficient words are identical.' if not failures else 'All boundaries reconstruct, but some direct/composite words differ by source syzygies.','limitations':['single prime','degrees 12,14,16','deterministic pivot words'],'passed':not failures}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
