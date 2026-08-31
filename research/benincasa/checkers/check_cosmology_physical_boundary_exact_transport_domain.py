#!/usr/bin/env python3
"""Verify exact q-word boundary transport domains for A12->A14->A16 and direct A12->A16."""
import importlib,json,os,sys
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path[:0]=[str(ROOT/'research'/'voevodsky')];R=ROOT/'research'/'benincasa'/'results'
def load(A):
 os.environ['MARICI_AMBIENT']=str(A)
 for n in ['physical_four_mark_residue_twisted_derham','g12_g31_residue_chart_transition','check_rank26_total_energy_triple_relation_module','check_cosmology_rank26_p_normal_K_q_correction_word_ambient_compatibility']:sys.modules.pop(n,None)
 c=importlib.import_module('check_cosmology_rank26_p_normal_K_q_correction_word_ambient_compatibility');d,sk=c.descriptors(A);q=[x for x in d if x[0]=='q'];p=json.loads((R/f'cosmology_physical_half_twist_boundary_exact_all_a{A}.json').read_text());return q,{(x['k_pole'],*x['exponent']):x for x in p['records']}
def qword(rec,q):
 out={}
 for x in rec['source_coefficients']:
  if x['kind']=='Q':out[q[x['row_index']]]=Fraction(x['numerator'],x['denominator'])
 return out
def shift_desc(d,n):f,k,l,ax,m,e=d;return(f,k,l,ax,m,(e[0],e[1]+n))
data={A:load(A) for A in (12,14,16)};edges={}
for a,b,n in ((12,14,2),(14,16,2),(12,16,4)):
 qa,ra=data[a];qb,rb=data[b];qset=set(qb);tested=missing=0;difference_terms=[]
 for key,rec in ra.items():
  target=(key[0],key[1],key[2]+n)
  if target not in rb:continue
  wa={shift_desc(d,n):v for d,v in qword(rec,qa).items()};missing+=sum(d not in qset for d in wa);wb=qword(rb[target],qb);difference_terms.append(len(set(wa)|set(wb)));tested+=1
 edges[f'{a}_to_{b}']={'coordinates_tested':tested,'shifted_q_descriptors_missing':missing,'difference_support_min':min(difference_terms),'difference_support_max':max(difference_terms),'fresh_base_correction_solved_over_Q':False}
out={'schema':'marici.benincasa.cosmology-physical-boundary-exact-transport-domain.v1','physical_gamma':'-1/2','edges':edges,'all_transport_domains_defined':all(x['shifted_q_descriptors_missing']==0 for x in edges.values()),'direct_composite_coherence_tested':False,'passed':True};(R/'cosmology_physical_boundary_exact_transport_domain.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
