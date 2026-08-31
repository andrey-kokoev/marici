"""Explain the 10,080 nonzero marked-q p-normal derivative rows by wall support."""
from __future__ import annotations
import json, sys
from itertools import product
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; sys.path.insert(0,str(ROOT/'research'/'benincasa'))
import physical_four_mark_residue_twisted_derham as base
import g12_g31_residue_chart_transition as charts
RES=ROOT/'research'/'voevodsky'/'results'; OUT=RES/'cosmology_rank26_p_normal_marked_q_support.json'

def poly_diff(a,b):
 keys=set(a)|set(b); return {k:(a.get(k,0)-b.get(k,0))%base.PRIME for k in keys if (a.get(k,0)-b.get(k,0))%base.PRIME}
def directional_q(point,direction):
 _,q0=base.fiber_data(*point); shifted=tuple(a+b for a,b in zip(point,direction)); _,q1=base.fiber_data(*shifted)
 return {name:poly_diff(q1[name],q0[name]) for name in charts.SOURCE_NAMES}
def main():
 complexity=json.loads((RES/'cosmology_rank26_p_normal_degree14_complexity_two_prime.json').read_text()); assert complexity['passed']
 point=(3,6,-3); nx=(1,0,0); ny=(0,1,0); tangent=(1,-1,0)
 derivatives={'nx':directional_q(point,nx),'ny':directional_q(point,ny),'p_tangent':directional_q(point,tangent)}
 support={d:[name for name,p in packet.items() if p] for d,packet in derivatives.items()}
 assert support=={'nx':['g2','g23'],'ny':['g1','g31'],'p_tangent':['g1','g2','g23','g31']}
 assert derivatives['nx']['g2']==derivatives['nx']['g23']=={(0,0):base.PRIME-1}
 assert derivatives['ny']['g1']==derivatives['ny']['g31']=={(0,0):base.PRIME-1}
 A=14; monomials=len(base.monomials_at_most(A-1)); levels_per_mark=charts.Q_DEPTH**(len(charts.SOURCE_NAMES)-1); rows_per_mark=(charts.K_DEPTH+1)*levels_per_mark*monomials
 assert (monomials,levels_per_mark,rows_per_mark)==(105,16,5040)
 predicted={'nx':len(support['nx'])*rows_per_mark,'ny':len(support['ny'])*rows_per_mark}
 assert predicted=={'nx':10080,'ny':10080}
 for prime in ('32003','32009'):
  marked=complexity['summary']['marked_q_multiplication_relations']
  assert marked['nx'][prime]['nonzero_input_rows']==predicted['nx'] and marked['ny'][prime]['nonzero_input_rows']==predicted['ny']
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-marked-q-support.v1','status':'marked_q_nonzero_row_count_explained_exactly_by_active_wall_support','point':list(point),'directions':{'nx':list(nx),'ny':list(ny),'p_tangent':list(tangent)},'directional_wall_support':support,'directional_q_derivatives':{d:{name:{str(k):v for k,v in poly.items()} for name,poly in packet.items() if poly} for d,packet in derivatives.items()},'degree14_count_factorization':{'monomials_degree_at_most_13':monomials,'other_mark_level_choices':levels_per_mark,'k_pole_levels':charts.K_DEPTH+1,'rows_per_active_mark':rows_per_mark,'nx_active_marks':2,'ny_active_marks':2,'predicted_nonzero_rows_each_normal':10080},'two_prime_observed_nonzero_rows_each_normal':10080,'decision':'The 15,120 zero marked-q derivative rows per normal are structurally inactive walls. The 10,080 active rows come from exactly two moving marks and still require nontrivial S+T reduction.','limitations':['explains support count, not reduction coefficients','does not explain IBP or K absorption','finite presentation count'],'passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2))
if __name__=='__main__':main()
