#!/usr/bin/env python3
"""Exact Q replay of maximal A12 q-only fresh-base shell representatives."""
import json,os,sys
from fractions import Fraction
from itertools import product
from pathlib import Path
A=int(os.environ.get('MARICI_AMBIENT','12'));os.environ['MARICI_AMBIENT']=str(A);ROOT=Path(__file__).resolve().parents[3];sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'benincasa'/'checkers'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
import check_cosmology_rank26_p_normal_K_q_correction_word_ambient_compatibility as compat
import check_cosmology_physical_half_twist_seed_exact_rational_minor as exact
R=ROOT/'research'/'benincasa'/'results';V=ROOT/'research'/'voevodsky'/'results';PS=exact.PS
def add(r,c,v):
 x=r.get(c,Fraction())+v
 if x:r[c]=x
 else:r.pop(c,None)
def solve(M,b):return exact.solve(M,b)
def pivcols(rows,p=32003):
 piv={};cols=[]
 for raw in rows:
  row={c:int(v%p) for c,v in raw.items() if v%p}
  while row:
   c=max(row);a=row[c]
   if c not in piv:
    inv=pow(a,-1,p);piv[c]={k:v*inv%p for k,v in row.items()};cols.append(c);break
   for k,v in piv[c].items():
    x=(row.get(k,0)-a*v)%p
    if x:row[k]=x
    else:row.pop(k,None)
 return cols
def qdescs(A):return [d for d in compat.descriptors(A)[0] if d[0]=='q']
def shift(d,s):f,k,l,axis,m,e=d;return(f,k,l,axis,m,(e[0]+s[0],e[1]+s[1]))
protocol=json.loads((V/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(protocol['test_point_xyz']);nx=tuple(protocol['integral_unit_normals']['nx']);td=tuple(protocol['integral_unit_normals']['p_tangent_difference']);_,columns=rees.column_packet();pack={};orig=base.PRIME
for p in PS:
 base.PRIME=p;rees.charts.GAMMA=-pow(2,-1,p)%p;special=list(rees.raw_relations(point,columns));T,_=adapter.derivative_rows(columns,point,td);dx,_=adapter.derivative_rows(columns,point,nx);nI=4*len(base.monomials_at_most(A));nK=64*len(base.monomials_at_most(A-4));pack[p]={'T':T,'S_K':special[nI:nI+nK],'Q':special[nI+nK:],'dx':dx}
base.PRIME=orig;sol=json.loads((R/'cosmology_physical_half_twist_seed_exact_rational_minor.json').read_text());cen=json.loads((R/f'cosmology_physical_half_twist_q_template_base_closure_census_a{A}.json').read_text());oldq=qdescs(14);newq={d:i for i,d in enumerate(qdescs(A))};K=[]
for kp in range(rees.charts.K_DEPTH):
 for lev in product(range(1,rees.charts.Q_DEPTH+1),repeat=len(rees.NAMES)):
  for e in base.monomials_at_most(A-4):K.append((kp,lev,e))
results={};rowcache={};qcache={}
for kp in (0,1):
 records=[]
 for rec in cen['results'][f'k{kp}']['records']:
  s=tuple(rec['shift']);gens=[(x['kind'],x['row_index']) for x in rec['source_generators']]
  src=[]
  for k,i in gens:
   if (k,i) not in rowcache:rowcache[k,i]=exact.exact_row([pack[p][k][i] for p in PS])
   src.append(rowcache[k,i])
  target=exact.exact_row([pack[p]['dx'][nI+K.index((kp,(1,1,2,1,1),s))] for p in PS]);corrected=dict(target)
  for item in sol['results'][f'k{kp}']['source_coefficients']:
   if item['kind']!='Q':continue
   qi=newq[shift(oldq[item['row_index']],s)];a=Fraction(item['numerator'],item['denominator'])
   if qi not in qcache:qcache[qi]=exact.exact_row([pack[p]['Q'][qi] for p in PS])
   for c,v in qcache[qi].items():add(corrected,c,-a*v)
  cols=pivcols(src);assert len(cols)==len(src);M=[[r.get(c,Fraction()) for r in src] for c in cols];b=[corrected.get(c,Fraction()) for c in cols];co=solve(M,b);recon={}
  for a,row in zip(co,src):
   for c,v in row.items():add(recon,c,a*v)
  assert recon==corrected;records.append({'shift':list(s),'source_rows':len(src),'full_corrected_target_reconstruction':True,'max_denominator':max(x.denominator for x in co)})
 results[f'k{kp}']={'shifts_solved':len(records),'source_rows_min':min(x['source_rows'] for x in records),'source_rows_max':max(x['source_rows'] for x in records),'maximum_denominator':max(x['max_denominator'] for x in records),'all_full_corrected_target_reconstructions':True,'records':records}
out={'schema':'marici.benincasa.cosmology-physical-half-twist-q-shell-exact-family.v1','physical_gamma':'-1/2','ambient':A,'results':results,'scope':f'all q-template shifts through degree {A-7} at A{A}','passed':True};(R/f'cosmology_physical_half_twist_q_shell_exact_family_a{A}.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
