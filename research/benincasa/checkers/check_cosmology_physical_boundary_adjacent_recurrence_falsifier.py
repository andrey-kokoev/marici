#!/usr/bin/env python3
"""Test whether adjacent exact boundary correction cells obey a stationary vertical recurrence."""
import importlib,json,os,sys
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path[:0]=[str(ROOT/'research'/'voevodsky')];R=ROOT/'research'/'benincasa'/'results'
def descs(A):
 os.environ['MARICI_AMBIENT']=str(A)
 for n in ['physical_four_mark_residue_twisted_derham','g12_g31_residue_chart_transition','check_rank26_total_energy_triple_relation_module','check_cosmology_rank26_p_normal_K_q_correction_word_ambient_compatibility']:sys.modules.pop(n,None)
 c=importlib.import_module('check_cosmology_rank26_p_normal_K_q_correction_word_ambient_compatibility');return c.descriptors(A)
def shift(d):f,k,l,ax,m,e=d;return(f,k,l,ax,m,(e[0],e[1]+2))
def word(rec,d,sk,transport=False):
 out={}
 for x in rec['coefficients']:
  q=(d if x['kind']=='T' else sk)[x['row_index']];q=shift(q) if transport else q;out[(x['kind'],q)]=Fraction(x['numerator'],x['denominator'])
 return out
d14,sk14=descs(14);d16,sk16=descs(16);a=json.loads((R/'cosmology_physical_boundary_exact_corrections_a12_to_a14.json').read_text());b=json.loads((R/'cosmology_physical_boundary_exact_corrections_a14_to_a16.json').read_text());A={(x['k_pole'],*x['source_exponent']):x for x in a['records']};B={(x['k_pole'],*x['source_exponent']):x for x in b['records']};records=[]
for key,x in sorted(A.items()):
 y=B[(key[0],key[1],key[2]+2)];u=word(x,d14,sk14,True);v=word(y,d16,sk16);common=set(u)&set(v);records.append({'k_pole':key[0],'source_exponent':[key[1],key[2]],'literal_match':u==v,'transported_terms':len(u),'next_terms':len(v),'common_terms':len(common),'coefficient_matches_on_common':sum(u[k]==v[k] for k in common)})
out={'schema':'marici.benincasa.cosmology-physical-boundary-adjacent-recurrence-falsifier.v1','physical_gamma':'-1/2','coordinates_tested':len(records),'stationary_matches':sum(x['literal_match'] for x in records),'stationary_adjacent_correction_recurrence':all(x['literal_match'] for x in records),'records':records,'decision':'A stationary transported adjacent correction word is not established.' if not all(x['literal_match'] for x in records) else 'All adjacent correction words obey the tested stationary recurrence.','passed':True};(R/'cosmology_physical_boundary_adjacent_recurrence_falsifier.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))
