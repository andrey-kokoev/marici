"""General ambient-degree profile of graded nx K residuals modulo T+S_K and with S_IBP."""
from __future__ import annotations
import json,os,sys
from collections import Counter
from itertools import product
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import g12_g31_residue_chart_transition as charts
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
import check_cosmology_rank26_p_normal_K_family_necessity as family
RES=ROOT/'research'/'voevodsky'/'results'; A=rees.AMBIENT; OUT=RES/f'cosmology_rank26_p_normal_K_residual_ambient_a{A}.json'
def count(n):return len(base.monomials_at_most(n))
def classify(target,pivots,desc):
 non=[]; rr=[]
 for i,row in enumerate(target):
  r=base.reduce_row(row,pivots)
  if r:non.append(i);rr.append(r)
 rp={};rank=family.add_basis(rr,rp); poles=Counter(desc[i][0] for i in non); patterns=Counter(desc[i][1] for i in non); exps=Counter(desc[i][2] for i in non)
 return {'nonabsorbed_rows':len(non),'residual_rank':rank,'pole_counts':{str(k):v for k,v in sorted(poles.items())},'distinct_level_patterns':len(patterns),'level_patterns':[{'levels':list(k),'count':v} for k,v in patterns.items()],'distinct_exponents':len(exps),'all_exponents_once_per_occupied_pole':all(v==len(poles) for v in exps.values())}
def main():
 assert A in (12,16) and base.PRIME==32003
 protocol=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text()); point=tuple(protocol['test_point_xyz']); nx=tuple(protocol['integral_unit_normals']['nx']); td=tuple(protocol['integral_unit_normals']['p_tangent_difference'])
 _,columns=rees.column_packet(); special=list(rees.raw_relations(point,columns)); tangent,_=adapter.derivative_rows(columns,point,td); dx,_=adapter.derivative_rows(columns,point,nx)
 nI=4*count(A); nK=64*count(A-4); nQ=240*count(A-1); assert len(special)==nI+nK+nQ
 Kslice=slice(nI,nI+nK); target=dx[Kslice]; desc=[]
 for kp in range(charts.K_DEPTH):
  for levels in product(range(1,charts.Q_DEPTH+1),repeat=len(rees.NAMES)):
   for exp in base.monomials_at_most(A-4):desc.append((kp,levels,exp))
 assert len(desc)==nK
 profiles={}
 for name,rows in {'T_plus_S_K':tangent+special[Kslice],'T_plus_S_K_IBP':tangent+special[Kslice]+special[:nI]}.items():
  piv={};family.add_basis(rows,piv);profiles[name]=classify(target,piv,desc)
 expected=count(A-4); assert profiles['T_plus_S_K']['nonabsorbed_rows']==2*expected and profiles['T_plus_S_K_IBP']['nonabsorbed_rows']==expected
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-K-residual-ambient-profile.v1','status':'ambient_residual_profile_verified','field':base.PRIME,'ambient_relation_degree':A,'family_row_counts':{'IBP':nI,'K':nK,'q':nQ},'profiles':profiles,'expected_monomials_degree_at_most_A_minus_4':expected,'decision':'The degree-14 residual support pattern transports to this ambient degree.' ,'limitations':['single prime','one ambient degree per result','rank values remain finite-cutoff data'],'passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
