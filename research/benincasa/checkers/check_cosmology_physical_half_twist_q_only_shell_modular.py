#!/usr/bin/env python3
"""Test q-only shifted rational seeds against fresh physical T+S_K closures on the A12 top interior shell."""
import importlib,json,os,sys
from fractions import Fraction
from itertools import product
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')];R=ROOT/'research'/'benincasa'/'results';V=ROOT/'research'/'voevodsky'/'results';A=12;PS=(32003,32009)
def run(p):
 os.environ['MARICI_AMBIENT']=str(A);os.environ['MARICI_FIELD_PRIME']=str(p)
 for n in list(sys.modules):
  if n in ('physical_four_mark_residue_twisted_derham','g12_g31_residue_chart_transition','check_rank26_total_energy_triple_relation_module','check_cosmology_rank26_p_normal_raw_relation_adapter','check_cosmology_rank26_p_normal_K_canonical_q_lifts'):sys.modules.pop(n)
 base=importlib.import_module('physical_four_mark_residue_twisted_derham');charts=importlib.import_module('g12_g31_residue_chart_transition');rees=importlib.import_module('check_rank26_total_energy_triple_relation_module');adapter=importlib.import_module('check_cosmology_rank26_p_normal_raw_relation_adapter');lifts=importlib.import_module('check_cosmology_rank26_p_normal_K_canonical_q_lifts');charts.GAMMA=-pow(2,-1,p)%p
 protocol=json.loads((V/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(protocol['test_point_xyz']);nx=tuple(protocol['integral_unit_normals']['nx']);td=tuple(protocol['integral_unit_normals']['p_tangent_difference']);_,cols=rees.column_packet();special=list(rees.raw_relations(point,cols));T,_=adapter.derivative_rows(cols,point,td);dx,_=adapter.derivative_rows(cols,point,nx);nI=4*len(base.monomials_at_most(A));nK=64*len(base.monomials_at_most(A-4));SK=special[nI:nI+nK];Q=special[nI+nK:]
 qd=[]
 for qi,name in enumerate(rees.NAMES):
  for kp in range(charts.K_DEPTH+1):
   for lev in product(range(1,charts.Q_DEPTH+1),repeat=len(rees.NAMES)):
    if lev[qi]==charts.Q_DEPTH:continue
    for e in base.monomials_at_most(A-1):qd.append((name,kp,lev,e))
 qmap={d:i for i,d in enumerate(qd)};K=[]
 for kp in range(charts.K_DEPTH):
  for lev in product(range(1,charts.Q_DEPTH+1),repeat=len(rees.NAMES)):
   for e in base.monomials_at_most(A-4):K.append((kp,lev,e))
 rat=json.loads((R/'cosmology_canonical_seed_five_prime_reconstruction.json').read_text());out={}
 for kp in (0,1):
  piv={}
  for row in T+SK:lifts.insert(row,piv)
  terms=rat['results'][f'k{kp}']['terms'];passed=0
  for s in [(i,5-i) for i in range(6)]:
   ti=nI+K.index((kp,(1,1,2,1,1),s));row=dict(dx[ti])
   for x in terms:
    d=x['descriptor'];key=(d[0],d[1],tuple(d[2]),(d[3][0]+s[0],d[3][1]+s[1]));qi=qmap[key];n,den=x['rational'];a=n*pow(den,-1,p)%p
    for c,v in Q[qi].items():lifts.add(row,c,a*v)
   assert not base.reduce_row(row,{c:dict(v[0]) for c,v in piv.items()});passed+=1
  out[f'k{kp}']=passed
 return out
results={str(p):run(p) for p in PS};body={'schema':'marici.benincasa.cosmology-physical-half-twist-q-only-shell-modular.v1','ambient':A,'shell_degree':5,'primes':list(PS),'results':results,'all_12_per_prime_zero':all(v=={'k0':6,'k1':6} for v in results.values()),'exact_rational_replay':False,'passed':True};(R/'cosmology_physical_half_twist_q_only_shell_modular.json').write_text(json.dumps(body,indent=2)+'\n');print(json.dumps(body,indent=2))
