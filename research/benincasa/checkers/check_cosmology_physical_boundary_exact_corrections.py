#!/usr/bin/env python3
"""Solve exact physical T+S_K correction words for one vertical boundary edge."""
import importlib,json,os,sys
from fractions import Fraction
from pathlib import Path
F=int(os.environ.get('MARICI_FROM','12'));A=int(os.environ.get('MARICI_TO','14'));assert A-F in (2,4);os.environ['MARICI_AMBIENT']=str(A)
ROOT=Path(__file__).resolve().parents[3];sys.path[:0]=[str(ROOT/'research'/'benincasa'/'checkers'),str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
import check_cosmology_rank26_p_normal_lower_quartile_source_dag as dag
import check_cosmology_rank26_p_normal_K_q_correction_word_ambient_compatibility as compat
import check_cosmology_physical_half_twist_seed_exact_rational_minor as exact
import check_cosmology_rank26_p_normal_K_q_exact_base_representative_solves as solver
R=ROOT/'research'/'benincasa'/'results';V=ROOT/'research'/'voevodsky'/'results';PS=exact.PS;P=32003
def add(r,c,v):
 x=r.get(c,Fraction())+v
 if x:r[c]=x
 else:r.pop(c,None)
def load_words(B):
 os.environ['MARICI_AMBIENT']=str(B)
 for n in ['physical_four_mark_residue_twisted_derham','g12_g31_residue_chart_transition','check_rank26_total_energy_triple_relation_module','check_cosmology_rank26_p_normal_K_q_correction_word_ambient_compatibility']:sys.modules.pop(n,None)
 c=importlib.import_module('check_cosmology_rank26_p_normal_K_q_correction_word_ambient_compatibility');d,sk=c.descriptors(B);q=[x for x in d if x[0]=='q'];p=json.loads((R/f'cosmology_physical_half_twist_boundary_exact_all_a{B}.json').read_text());return q,{(x['k_pole'],*x['exponent']):x for x in p['records']}
def word(rec,q):return {q[x['row_index']]:Fraction(x['numerator'],x['denominator']) for x in rec['source_coefficients'] if x['kind']=='Q'}
def shift(d,n):f,k,l,ax,m,e=d;return(f,k,l,ax,m,(e[0],e[1]+n))
qf,wf=load_words(F);qa,wa=load_words(A);os.environ['MARICI_AMBIENT']=str(A)
# Reload target modules after descriptor inspection.
for n in ['physical_four_mark_residue_twisted_derham','g12_g31_residue_chart_transition','check_rank26_total_energy_triple_relation_module','check_cosmology_rank26_p_normal_raw_relation_adapter']:sys.modules.pop(n,None)
base=importlib.import_module('physical_four_mark_residue_twisted_derham');rees=importlib.import_module('check_rank26_total_energy_triple_relation_module');adapter=importlib.import_module('check_cosmology_rank26_p_normal_raw_relation_adapter')
protocol=json.loads((V/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(protocol['test_point_xyz']);td=tuple(protocol['integral_unit_normals']['p_tangent_difference']);_,columns=rees.column_packet();pack={};orig=base.PRIME
for p in PS:
 base.PRIME=p;rees.charts.GAMMA=-pow(2,-1,p)%p;sp=list(rees.raw_relations(point,columns));T,_=adapter.derivative_rows(columns,point,td);nI=4*len(base.monomials_at_most(A));nK=64*len(base.monomials_at_most(A-4));pack[p]={'T':T,'S_K':sp[nI:nI+nK],'Q':sp[nI+nK:]}
base.PRIME=P;T=pack[P]['T'];SK=pack[P]['S_K'];piv={};nodes={};creation=[]
for kind,rows in [('T',T),('S_K',SK)]:
 for i,r in enumerate(rows):dag.add_pivot(r,piv,nodes,creation,(kind,i))
qmap={d:i for i,d in enumerate(qa)};cache={};records=[];n=A-F
for key,fr in sorted(wf.items()):
 target=(key[0],key[1],key[2]+n)
 if target not in wa:continue
 diff={}
 for d,a in word(fr,qf).items():
  qi=qmap[shift(d,n)];row=exact.exact_row([pack[p]['Q'][qi] for p in PS])
  for c,v in row.items():add(diff,c,a*v)
 for d,a in word(wa[target],qa).items():
  qi=qmap[d];row=exact.exact_row([pack[p]['Q'][qi] for p in PS])
  for c,v in row.items():add(diff,c,-a*v)
 mod={c:int(v.numerator*pow(v.denominator,-1,P)%P) for c,v in diff.items()};rem,tr=dag.trace(mod,piv);assert not rem;pending={}
 for p,a in tr:dag.add_value(pending,p,a)
 origins=[]
 for p in reversed(creation):
  a=pending.pop(p,0)
  if not a:continue
  node=nodes[p];k=tuple(node['origin'])
  if k not in origins:origins.append(k)
  for q,b in node['dependencies']:dag.add_value(pending,q,a*b)
 assert not pending;rows=[]
 for k,i in origins:
  ck=(k,i)
  if ck not in cache:cache[ck]=exact.exact_row([pack[p][k][i] for p in PS])
  rows.append(cache[ck])
 cols=sorted(set(diff).union(*(r.keys() for r in rows)));coef,rank=solver.solve_rect(rows,diff,cols);recon={}
 for a,r in zip(coef,rows):
  for c,v in r.items():add(recon,c,a*v)
 assert recon==diff;records.append({'k_pole':key[0],'source_exponent':[key[1],key[2]],'target_exponent':[target[1],target[2]],'source_rows':len(rows),'rank':rank,'coefficients':[{'kind':k,'row_index':i,'numerator':a.numerator,'denominator':a.denominator} for (k,i),a in zip(origins,coef)]})
base.PRIME=orig;out={'schema':'marici.benincasa.cosmology-physical-boundary-exact-corrections.v1','physical_gamma':'-1/2','from_ambient':F,'to_ambient':A,'record_count':len(records),'all_full_reconstructions':True,'records':records,'passed':True};(R/f'cosmology_physical_boundary_exact_corrections_a{F}_to_a{A}.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'from':F,'to':A,'records':len(records),'rows_min':min(x['source_rows'] for x in records),'rows_max':max(x['source_rows'] for x in records),'passed':True},indent=2))
