"""Decode and compare normalized correction source-word coefficients across adjacent inclusions."""
from __future__ import annotations
import hashlib,json,sys
from itertools import product
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path[:0]=[str(ROOT/'research'/'benincasa')]
import physical_four_mark_residue_twisted_derham as base
import g12_g31_residue_chart_transition as charts
import check_rank26_total_energy_triple_relation_module as rees
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_rank26_p_normal_K_q_correction_word_ambient_compatibility.json'
def descriptors(A):
 out=[]
 for kp in range(charts.K_DEPTH):
  for levels in product(range(1,charts.Q_DEPTH+1),repeat=len(rees.NAMES)):
   if any(x==charts.Q_DEPTH for x in levels):continue
   for axis in range(2):
    for exp in base.monomials_at_most(A):out.append(('IBP',kp,levels,axis,None,exp))
 for kp in range(charts.K_DEPTH):
  for levels in product(range(1,charts.Q_DEPTH+1),repeat=len(rees.NAMES)):
   for exp in base.monomials_at_most(A-4):out.append(('K',kp,levels,None,None,exp))
 for qi,mark in enumerate(rees.NAMES):
  for kp in range(charts.K_DEPTH+1):
   for levels in product(range(1,charts.Q_DEPTH+1),repeat=len(rees.NAMES)):
    if levels[qi]==charts.Q_DEPTH:continue
    for exp in base.monomials_at_most(A-1):out.append(('q',kp,levels,None,mark,exp))
 sk=[d for d in out if d[0]=='K'];return out,sk
def normalized(packet,A,kp):
 td,sk=descriptors(A);terms=[];target=(0,A-6)
 for item in packet['results'][f'k{kp}']['coefficients']:
  d=td[item['row_index']] if item['kind']=='T' else sk[item['row_index']];family,qkp,levels,axis,mark,exp=d
  terms.append((item['kind'],family,qkp,levels,axis,mark,exp[0]-target[0],exp[1]-target[1],item['coefficient']))
 terms=tuple(sorted(terms,key=repr));return hashlib.sha256(repr(terms).encode()).hexdigest(),terms

def main():
 packets={14:json.loads((RES/'cosmology_rank26_p_normal_K_q_boundary_correction_words_A12_to_A14.json').read_text()),16:json.loads((RES/'cosmology_rank26_p_normal_K_q_boundary_correction_words_A14_to_A16.json').read_text())};results={};all_match=True
 for kp in (0,1):
  h14,t14=normalized(packets[14],14,kp);h16,t16=normalized(packets[16],16,kp);match=t14==t16;all_match&=match;results[f'k{kp}']={'A12_to_A14_hash':h14,'A14_to_A16_hash':h16,'normalized_descriptor_coefficients_identical':match,'terms':len(t14)}
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-K-q-correction-word-ambient-compatibility.v1','status':'correction_source_words_transport_exactly' if all_match else 'correction_source_words_not_identical','results':results,'decision':'Normalized original-row correction words are coefficient-identical across both ambient inclusions.' if all_match else 'Invariant source-row counts do not upgrade to identical normalized correction words.','limitations':['single prime','lower-edge representative only','two adjacent inclusions','deterministic pivot representative'],'passed':all_match}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
