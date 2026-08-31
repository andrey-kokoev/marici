"""Compare direct A12->A16 correction words with composition of adjacent correction words."""
from __future__ import annotations
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
import check_cosmology_rank26_p_normal_lower_quartile_source_dag as dag
import check_cosmology_rank26_p_normal_K_q_correction_word_ambient_compatibility as compat
import check_cosmology_rank26_p_normal_K_q_boundary_correction_source_words as words
RES=ROOT/'research'/'voevodsky'/'results';OUT=ROOT/'research'/'benincasa'/'results'/'cosmology_boundary_correction_composition_audit.json'
def add(d,k,v):
 v=(d.get(k,0)+v)%base.PRIME
 if v:d[k]=v
 else:d.pop(k,None)
def evaluate(coeff,tangent,SK):
 row={}
 for (kind,index),a in coeff.items():
  for c,v in (tangent[index] if kind=='T' else SK[index]).items():add(row,c,a*v)
 return row
def main():
 assert rees.AMBIENT==16 and base.PRIME==32003
 q12=json.loads((RES/'cosmology_rank26_p_normal_K_q_boundary_signatures_a12.json').read_text());q16=json.loads((RES/'cosmology_rank26_p_normal_K_q_boundary_signatures_a16.json').read_text());p14=json.loads((RES/'cosmology_rank26_p_normal_K_q_boundary_correction_words_A12_to_A14.json').read_text());p16=json.loads((RES/'cosmology_rank26_p_normal_K_q_boundary_correction_words_A14_to_A16.json').read_text());d14,sk14=compat.descriptors(14);d16,sk16=compat.descriptors(16);Ti={d:i for i,d in enumerate(d16)};SKi={d:i for i,d in enumerate(sk16)}
 protocol=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(protocol['test_point_xyz']);td=tuple(protocol['integral_unit_normals']['p_tangent_difference']);_,columns=rees.column_packet();special=list(rees.raw_relations(point,columns));tangent,_=adapter.derivative_rows(columns,point,td);nI=4*len(base.monomials_at_most(16));nK=64*len(base.monomials_at_most(12));SK=special[nI:nI+nK];qrows=special[nI+nK:];qd=words.qdesc();qkey={d:i for i,d in enumerate(qd)}
 pivots={};nodes={};creation=[]
 for i,row in enumerate(tangent):dag.add_pivot(row,pivots,nodes,creation,('T',i))
 for i,row in enumerate(SK):dag.add_pivot(row,pivots,nodes,creation,('S_K',i))
 slookup={(r['k_pole'],*r['exponent']):r for r in q12['records']};tlookup={(r['k_pole'],*r['exponent']):r for r in q16['records']};results={}
 for kp in (0,1):
  s=slookup[(kp,0,6)];t=tlookup[(kp,0,10)];direct_row={}
  for term in s['terms']:
   qi=qkey[(term['mark'],term['q_pole'],tuple(term['levels']),(term['exponent'][0],term['exponent'][1]+4))]
   for c,v in qrows[qi].items():add(direct_row,c,term['coefficient']*v)
  for term in t['terms']:
   qi=qkey[(term['mark'],term['q_pole'],tuple(term['levels']),tuple(term['exponent']))]
   for c,v in qrows[qi].items():add(direct_row,c,-term['coefficient']*v)
  direct,_trace=words.expand(direct_row,pivots,nodes,creation);assert evaluate(direct,tangent,SK)==direct_row
  composite={}
  for item in p14['results'][f'k{kp}']['coefficients']:
   d=(d14 if item['kind']=='T' else sk14)[item['row_index']];family,qkp,lev,axis,mark,exp=d;sd=(family,qkp,lev,axis,mark,(exp[0],exp[1]+2));idx=(Ti if item['kind']=='T' else SKi)[sd];add(composite,(item['kind'],idx),item['coefficient'])
  for item in p16['results'][f'k{kp}']['coefficients']:add(composite,(item['kind'],item['row_index']),item['coefficient'])
  assert evaluate(composite,tangent,SK)==direct_row
  syzygy=dict(composite)
  for k,a in direct.items():add(syzygy,k,-a)
  assert not evaluate(syzygy,tangent,SK)
  results[f'k{kp}']={'direct_source_rows':len(direct),'composite_source_rows':len(composite),'syzygy_nonzero_coefficients':len(syzygy),'direct_reconstruction':True,'composite_reconstruction':True,'higher_coherence_syzygy_verified':True}
 out={'schema':'marici.benincasa.cosmology-boundary-correction-composition-audit.v1','status':'direct_and_composite_corrections_coherent_by_source_syzygy','results':results,'decision':'The direct A12->A16 correction and composite adjacent corrections have identical boundary and differ by an exact original-source syzygy.','limitations':['lower-edge representatives','single prime','finite degrees 12,14,16','syzygy coefficients not retained'],'passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
