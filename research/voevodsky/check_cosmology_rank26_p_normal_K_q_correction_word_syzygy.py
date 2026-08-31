"""Test whether vertically transported A12->A14 correction words differ from A14->A16 words by exact source syzygies."""
from __future__ import annotations
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
import check_cosmology_rank26_p_normal_K_q_correction_word_ambient_compatibility as compat
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_rank26_p_normal_K_q_correction_word_syzygy.json'
def add(d,k,v):
 v=(d.get(k,0)+v)%base.PRIME
 if v:d[k]=v
 else:d.pop(k,None)
def shifted_descriptor(d):
 family,kp,levels,axis,mark,exp=d;return (family,kp,levels,axis,mark,(exp[0],exp[1]+2))
def main():
 assert rees.AMBIENT==16 and base.PRIME==32003
 earlier=json.loads((RES/'cosmology_rank26_p_normal_K_q_boundary_correction_words_A12_to_A14.json').read_text());later=json.loads((RES/'cosmology_rank26_p_normal_K_q_boundary_correction_words_A14_to_A16.json').read_text());d14,sk14=compat.descriptors(14);d16,sk16=compat.descriptors(16);Ti={d:i for i,d in enumerate(d16)};SKi={d:i for i,d in enumerate(sk16)}
 protocol=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(protocol['test_point_xyz']);td=tuple(protocol['integral_unit_normals']['p_tangent_difference']);_,columns=rees.column_packet();special=list(rees.raw_relations(point,columns));tangent,_=adapter.derivative_rows(columns,point,td);nI=4*len(base.monomials_at_most(16));nK=64*len(base.monomials_at_most(12));SK=special[nI:nI+nK]
 results={}
 for kp in (0,1):
  row={};mapped=0
  for item in earlier['results'][f'k{kp}']['coefficients']:
   desc=(d14 if item['kind']=='T' else sk14)[item['row_index']];sd=shifted_descriptor(desc);index=(Ti if item['kind']=='T' else SKi)[sd];source=(tangent if item['kind']=='T' else SK)[index]
   for c,v in source.items():add(row,c,item['coefficient']*v)
   mapped+=1
  for item in later['results'][f'k{kp}']['coefficients']:
   source=(tangent if item['kind']=='T' else SK)[item['row_index']]
   for c,v in source.items():add(row,c,-item['coefficient']*v)
  results[f'k{kp}']={'translated_source_terms':mapped,'target_source_terms':len(later['results'][f'k{kp}']['coefficients']),'difference_support':len(row),'syzygy_verified':not row}
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-K-q-correction-word-syzygy.v1','status':'higher_coherence_syzygies_verified' if all(x['syzygy_verified'] for x in results.values()) else 'higher_coherence_syzygy_fails','map':'translate every source-row monomial exponent by (0,2), then subtract the next-inclusion correction word','results':results,'decision':'Correction source words are unequal representatives of the same transported source relation and differ by exact source syzygies.' if all(x['syzygy_verified'] for x in results.values()) else 'Correction-word differences are not zero source relations.','limitations':['lower-edge representatives only','single prime','one composable pair of inclusions','zero relation verified in finite ambient module'],'passed':all(x['syzygy_verified'] for x in results.values())}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
