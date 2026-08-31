#!/usr/bin/env python3
"""Compare exact direct A12->A16 boundary corrections with adjacent composites."""
import importlib,json,os,sys
from fractions import Fraction
from pathlib import Path
os.environ['MARICI_AMBIENT']='16';ROOT=Path(__file__).resolve().parents[3];sys.path[:0]=[str(ROOT/'research'/'benincasa'/'checkers'),str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
import check_cosmology_rank26_p_normal_K_q_correction_word_ambient_compatibility as compat
import check_cosmology_physical_half_twist_seed_exact_rational_minor as exact
R=ROOT/'research'/'benincasa'/'results';V=ROOT/'research'/'voevodsky'/'results';PS=exact.PS
def add(d,k,v):
 x=d.get(k,Fraction())+v
 if x:d[k]=x
 else:d.pop(k,None)
def descs(A):
 os.environ['MARICI_AMBIENT']=str(A)
 for n in ['physical_four_mark_residue_twisted_derham','g12_g31_residue_chart_transition','check_rank26_total_energy_triple_relation_module','check_cosmology_rank26_p_normal_K_q_correction_word_ambient_compatibility']:sys.modules.pop(n,None)
 c=importlib.import_module('check_cosmology_rank26_p_normal_K_q_correction_word_ambient_compatibility');return c.descriptors(A)
def shift(d):f,k,l,ax,m,e=d;return(f,k,l,ax,m,(e[0],e[1]+2))
d14,sk14=descs(14);d16,sk16=descs(16);maps={'T':{d:i for i,d in enumerate(d16)},'S_K':{d:i for i,d in enumerate(sk16)}};old={'T':d14,'S_K':sk14}
a=json.loads((R/'cosmology_physical_boundary_exact_corrections_a12_to_a14.json').read_text());b=json.loads((R/'cosmology_physical_boundary_exact_corrections_a14_to_a16.json').read_text());direct=json.loads((R/'cosmology_physical_boundary_exact_corrections_a12_to_a16.json').read_text());A={(x['k_pole'],*x['source_exponent']):x for x in a['records']};B={(x['k_pole'],*x['source_exponent']):x for x in b['records']};D={(x['k_pole'],*x['source_exponent']):x for x in direct['records']}
# Exact A16 source rows.
os.environ['MARICI_AMBIENT']='16'
for n in ['physical_four_mark_residue_twisted_derham','g12_g31_residue_chart_transition','check_rank26_total_energy_triple_relation_module','check_cosmology_rank26_p_normal_raw_relation_adapter']:sys.modules.pop(n,None)
base=importlib.import_module('physical_four_mark_residue_twisted_derham');rees=importlib.import_module('check_rank26_total_energy_triple_relation_module');adapter=importlib.import_module('check_cosmology_rank26_p_normal_raw_relation_adapter');protocol=json.loads((V/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(protocol['test_point_xyz']);td=tuple(protocol['integral_unit_normals']['p_tangent_difference']);_,cols=rees.column_packet();pack={}
for p in PS:
 base.PRIME=p;rees.charts.GAMMA=-pow(2,-1,p)%p;sp=list(rees.raw_relations(point,cols));T,_=adapter.derivative_rows(cols,point,td);nI=4*len(base.monomials_at_most(16));nK=64*len(base.monomials_at_most(12));pack[p]={'T':T,'S_K':sp[nI:nI+nK]}
cache={};records=[];strict=0
for key,x in D.items():
 comp={}
 for item in A[key]['coefficients']:
  kind=item['kind'];idx=maps[kind][shift(old[kind][item['row_index']])];add(comp,(kind,idx),Fraction(item['numerator'],item['denominator']))
 mid=(key[0],key[1],key[2]+2)
 for item in B[mid]['coefficients']:add(comp,(item['kind'],item['row_index']),Fraction(item['numerator'],item['denominator']))
 dw={(i['kind'],i['row_index']):Fraction(i['numerator'],i['denominator']) for i in x['coefficients']};strict+=comp==dw;syz=dict(comp)
 for k,v in dw.items():add(syz,k,-v)
 value={}
 for (kind,i),coef in syz.items():
  if (kind,i) not in cache:cache[kind,i]=exact.exact_row([pack[p][kind][i] for p in PS])
  for c,v in cache[kind,i].items():add(value,c,coef*v)
 assert not value;records.append({'k_pole':key[0],'source_exponent':[key[1],key[2]],'literal_match':comp==dw,'syzygy_terms':len(syz),'exact_source_syzygy_zero':True})
out={'schema':'marici.benincasa.cosmology-physical-boundary-exact-composition.v1','physical_gamma':'-1/2','rows_tested':len(records),'strict_coefficient_matches':strict,'syzygy_only_matches':len(records)-strict,'all_exact_source_syzygies_zero':True,'records':records,'passed':True};(R/'cosmology_physical_boundary_exact_composition.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))
