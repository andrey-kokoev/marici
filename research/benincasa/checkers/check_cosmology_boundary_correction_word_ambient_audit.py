#!/usr/bin/env python3
"""Independently compare normalized lower-edge correction words across inclusions."""
import hashlib,json,sys
from itertools import product
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research'/'benincasa'))
import physical_four_mark_residue_twisted_derham as base
import g12_g31_residue_chart_transition as charts
import check_rank26_total_energy_triple_relation_module as rees
V=ROOT/'research'/'voevodsky'/'results';R=ROOT/'research'/'benincasa'/'results'
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
 return out,[d for d in out if d[0]=='K']
def normalized(packet,A,kp):
 td,sk=descriptors(A);target=(0,A-6);m={}
 for item in packet['results'][f'k{kp}']['coefficients']:
  d=td[item['row_index']] if item['kind']=='T' else sk[item['row_index']];family,qkp,levels,axis,mark,exp=d;key=(item['kind'],family,qkp,levels,axis,mark,exp[0]-target[0],exp[1]-target[1]);m[key]=item['coefficient']
 return m
pack={14:json.loads((V/'cosmology_rank26_p_normal_K_q_boundary_correction_words_A12_to_A14.json').read_text()),16:json.loads((V/'cosmology_rank26_p_normal_K_q_boundary_correction_words_A14_to_A16.json').read_text())};results={}
for kp in (0,1):
 a,b=normalized(pack[14],14,kp),normalized(pack[16],16,kp);ka,kb=set(a),set(b);common=ka&kb;results[f'k{kp}']={'term_counts':[len(a),len(b)],'descriptor_support_identical':ka==kb,'common_descriptor_count':len(common),'coefficient_matches_on_common':sum(a[k]==b[k] for k in common),'coefficient_mismatches_on_common':sum(a[k]!=b[k] for k in common),'source_only_descriptors':len(ka-kb),'target_only_descriptors':len(kb-ka),'normalized_hashes':[hashlib.sha256(repr(tuple(sorted(a.items(),key=repr))).encode()).hexdigest(),hashlib.sha256(repr(tuple(sorted(b.items(),key=repr))).encode()).hexdigest()]};assert a!=b
out={'schema':'marici.benincasa.cosmology-boundary-correction-word-ambient-audit.v1','field':32003,'results':results,'normalized_words_identical':False,'literal_source_word_transport_falsified':True,'difference_source_syzygy_tested':False,'interpretation':'stable support sizes do not define coefficient-identical normalized correction words across adjacent inclusions; a higher source-syzygy comparison is required before exhausting quotient-level transport','passed':True};(R/'cosmology_boundary_correction_word_ambient_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
