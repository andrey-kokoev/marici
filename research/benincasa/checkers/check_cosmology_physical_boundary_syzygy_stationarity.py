#!/usr/bin/env python3
"""Test stationarity of exact complete-word transport syzygies across adjacent boundary edges."""
import importlib,json,os,sys
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path[:0]=[str(ROOT/'research'/'voevodsky')];R=ROOT/'research'/'benincasa'/'results'
def load(A):
 os.environ['MARICI_AMBIENT']=str(A)
 for n in ['physical_four_mark_residue_twisted_derham','g12_g31_residue_chart_transition','check_rank26_total_energy_triple_relation_module','check_cosmology_rank26_p_normal_K_q_correction_word_ambient_compatibility']:sys.modules.pop(n,None)
 c=importlib.import_module('check_cosmology_rank26_p_normal_K_q_correction_word_ambient_compatibility');d,sk=c.descriptors(A);q=[x for x in d if x[0]=='q'];maps={'T':d,'S_K':sk,'Q':q};p=json.loads((R/f'cosmology_physical_half_twist_boundary_exact_all_a{A}.json').read_text());return maps,{(x['k_pole'],*x['exponent']):x for x in p['records']}
def shift_desc(d,n):f,k,l,ax,m,e=d;return(f,k,l,ax,m,(e[0],e[1]+n))
def word(rec,maps,n=0):
 out={}
 for x in rec['source_coefficients']:
  d=shift_desc(maps[x['kind']][x['row_index']],n);out[(x['kind'],d)]=Fraction(x['numerator'],x['denominator'])
 return out
def diff(a,b):
 out=dict(a)
 for k,v in b.items():out[k]=out.get(k,Fraction())-v
 return {k:v for k,v in out.items() if v}
data={A:load(A) for A in (12,14,16)};m12,w12=data[12];m14,w14=data[14];m16,w16=data[16];records=[]
for key,r12 in sorted(w12.items()):
 mid=(key[0],key[1],key[2]+2);end=(key[0],key[1],key[2]+4);s1=diff(word(r12,m12,4),word(w14[mid],m14,2));s2=diff(word(w14[mid],m14,2),word(w16[end],m16,0));common=set(s1)&set(s2);records.append({'k_pole':key[0],'source_exponent':[key[1],key[2]],'stationary_match':s1==s2,'first_terms':len(s1),'second_terms':len(s2),'common_terms':len(common),'coefficient_matches_on_common':sum(s1[k]==s2[k] for k in common)})
out={'schema':'marici.benincasa.cosmology-physical-boundary-syzygy-stationarity.v1','physical_gamma':'-1/2','coordinates_tested':len(records),'stationary_matches':sum(x['stationary_match'] for x in records),'stationary_syzygy_recurrence':all(x['stationary_match'] for x in records),'records':records,'decision':'The adjacent exact source-syzygy cells are cutoff-dependent.' if not all(x['stationary_match'] for x in records) else 'The tested adjacent source-syzygy cells are stationary.','passed':True};(R/'cosmology_physical_boundary_syzygy_stationarity.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))
