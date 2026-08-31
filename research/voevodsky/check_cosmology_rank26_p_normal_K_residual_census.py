"""Classify nx K-derivative residuals modulo graded source-family bases."""
from __future__ import annotations
import json,sys
from collections import Counter
from itertools import product
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import g12_g31_residue_chart_transition as charts
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
import check_cosmology_rank26_p_normal_K_family_necessity as family
RES=ROOT/'research'/'voevodsky'/'results'; OUT=RES/'cosmology_rank26_p_normal_K_residual_census.json'
def K_descriptors():
 out=[]
 for kp in range(charts.K_DEPTH):
  for levels in product(range(1,charts.Q_DEPTH+1),repeat=len(rees.NAMES)):
   for exp in base.monomials_at_most(rees.AMBIENT-4):out.append({'k_pole':kp,'q_levels':levels,'exponent':exp})
 assert len(out)==4224; return out
def build(rows):
 piv={}; family.add_basis(rows,piv); return piv
def classify(target,pivots,desc):
 non=[]; residual_rows=[]
 for i,row in enumerate(target):
  r=base.reduce_row(row,pivots)
  if r:non.append(i); residual_rows.append(r)
 rank_piv={}; rank=family.add_basis(residual_rows,rank_piv); poles=Counter(); levels=Counter(); exps=Counter(); level_patterns=Counter()
 for i in non:
  d=desc[i]; poles[d['k_pole']]+=1; exps[d['exponent']]+=1; level_patterns[d['q_levels']]+=1
  for name,v in zip(rees.NAMES,d['q_levels']):levels[(name,v)]+=1
 return {'nonabsorbed_rows':len(non),'residual_quotient_rank':rank,'k_pole_counts':{str(k):v for k,v in sorted(poles.items())},'exponent_counts':{str(k):v for k,v in sorted(exps.items())},'marked_level_marginals':{f'{n}:{l}':v for (n,l),v in sorted(levels.items())},'distinct_level_patterns':len(level_patterns),'level_patterns':[{ 'levels':list(k),'count':v} for k,v in sorted(level_patterns.items())],'row_indices':non}
def main():
 assert rees.AMBIENT==14 and base.PRIME==32003
 protocol=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text()); point=tuple(protocol['test_point_xyz']); nx=tuple(protocol['integral_unit_normals']['nx']); tangent_dir=tuple(protocol['integral_unit_normals']['p_tangent_difference'])
 _,columns=rees.column_packet(); special=list(rees.raw_relations(point,columns)); tangent,_=adapter.derivative_rows(columns,point,tangent_dir); dx,_=adapter.derivative_rows(columns,point,nx); target=dx[480:4704]; desc=K_descriptors()
 bases={
  'T_plus_S_K':tangent+special[480:4704],
  'T_plus_S_K_IBP':tangent+special[480:4704]+special[:480]
 }
 censuses={name:classify(target,build(rows),desc) for name,rows in bases.items()}
 assert censuses['T_plus_S_K']['nonabsorbed_rows']==132 and censuses['T_plus_S_K_IBP']['nonabsorbed_rows']==66
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-K-residual-census.v1','status':'graded_K_residual_quotients_classified','field':base.PRIME,'ambient_relation_degree':14,'censuses':censuses,'decision':'Residual row counts and quotient ranks are separated and typed by pole, marked levels, and monomial exponent.','limitations':['single prime','degree 14','classification precedes explicit q-lift coefficients'],'passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps({**out,'censuses':{k:{x:y for x,y in v.items() if x!='row_indices'} for k,v in censuses.items()}},indent=2))
if __name__=='__main__':main()
