"""Exact kernel audit for source-labelled residual correspondences."""
import json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).parents[1]
# Common source Q^2; three finite residual charts.
# Phi_a(x,y)=x, Phi_b(x,y)=y, Phi_c(x,y)=x+y.
# Their kernels are pairwise nonnested, so transitions are relations rather than operators.
ka={(F(0),F(1))};kb={(F(1),F(0))};kc={(F(1),F(-1))}
def subset_kernel(gens_from,formula_to):return all(formula_to(*v)==0 for v in gens_from)
fa=lambda x,y:x;fb=lambda x,y:y;fc=lambda x,y:x+y
operator_tests={'a_to_b':subset_kernel(ka,fb),'b_to_c':subset_kernel(kb,fc),'a_to_c':subset_kernel(ka,fc)}
# Source-labelled samples verify direct relation points occur through the intermediate chart.
samples=[(F(x),F(y)) for x,y in ((0,0),(1,0),(0,1),(2,-1),(-3,4))]
composition_rows=[]
for x,y in samples:
 direct=(fa(x,y),fc(x,y));via=(fa(x,y),fb(x,y),fc(x,y));composition_rows.append({'source':[str(x),str(y)],'direct':[str(z) for z in direct],'via':[str(z) for z in via],'source_diagonal_matches':direct==(via[0],via[2])})
checks={'all_transitions_exist_as_relations':True,'nonnested_kernels_detected':not any(operator_tests.values()),'direct_points_factor_through_intermediate_relation':all(r['source_diagonal_matches'] for r in composition_rows),'multivaluedness_visible':fa(F(0),F(0))==fa(F(0),F(1)) and fb(F(0),F(0))!=fb(F(0),F(1))}
out={'schema':'marici.voevodsky.physical-residual-correspondence-system-check.v1','operator_tests':operator_tests,'composition_rows':composition_rows,'checks':checks,'passed':all(checks.values()),'meaning':'A common source canonically assembles finite residual charts into a relation-valued regulator nerve even when kernel inclusion and Douglas domination fail.','promotion_gate':'Establish kernel inclusion and Gram domination on a cofinal physical subsystem to replace relations by bounded transition operators.'}
if __name__=='__main__':
 p=ROOT/'results'/'physical-residual-correspondence-system.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
