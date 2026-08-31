#!/usr/bin/env python3
"""Validate descriptor-addressable exact boundary word interfaces at A12/A14/A16."""
import hashlib,json,os,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path[:0]=[str(ROOT/'research'/'voevodsky')];R=ROOT/'research'/'benincasa'/'results'
summary={}
for A in (12,14,16):
 os.environ['MARICI_AMBIENT']=str(A)
 for n in ['physical_four_mark_residue_twisted_derham','g12_g31_residue_chart_transition','check_rank26_total_energy_triple_relation_module','check_cosmology_rank26_p_normal_K_q_correction_word_ambient_compatibility']:
  sys.modules.pop(n,None)
 import importlib
 compat=importlib.import_module('check_cosmology_rank26_p_normal_K_q_correction_word_ambient_compatibility');d,sk=compat.descriptors(A);q=[x for x in d if x[0]=='q'];maps={'T':d,'S_K':sk,'Q':q}
 pack=json.loads((R/f'cosmology_physical_half_twist_boundary_exact_all_a{A}.json').read_text());h=hashlib.sha256();terms=0
 for rec in sorted(pack['records'],key=lambda x:(x['k_pole'],x['exponent'])):
  h.update(f"target:{rec['k_pole']}:{rec['exponent']};".encode())
  for x in rec['source_coefficients']:
   desc=maps[x['kind']][x['row_index']];h.update(f"{x['kind']}:{repr(desc)}:{x['numerator']}/{x['denominator']};".encode());terms+=1
 summary[str(A)]={'targets':len(pack['records']),'source_terms':terms,'descriptor_coefficient_sha256':h.hexdigest(),'all_indices_descriptor_resolved':True}
out={'schema':'marici.benincasa.cosmology-physical-boundary-exact-word-interface.v1','physical_gamma':'-1/2','summary':summary,'direct_composite_coherence_tested':False,'next_gate':'apply the established boundary coordinate transport to these descriptor-coefficient words and compare direct A12-to-A16 against the A12-to-A14-to-A16 composite','passed':True};(R/'cosmology_physical_boundary_exact_word_interface.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
