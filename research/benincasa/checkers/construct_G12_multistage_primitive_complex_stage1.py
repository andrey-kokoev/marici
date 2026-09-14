#!/usr/bin/env python3
"""VC2 stage 1: materialize the polynomial primitive image and residual quotient."""
import json
from math import comb
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
scalar=json.loads((ROOT/'research/benincasa/results/G12_scalar_polynomial_Hermite_equation.json').read_text())
four=json.loads((ROOT/'research/benincasa/results/G12_four_component_Hermite_image.json').read_text())
# Previous operator has coefficient degree <=10 and output degree <=17 in three variables.
domain_per_component=comb(10+3,3);domain=4*domain_per_component;ambient=comb(17+3,3)
rows=[]
for row in four['modular_tests']:
 rows.append({'prime':row['prime'],'C0_dimension':domain,'C1_dimension':ambient,'d0_rank':row['rank'],'H1_quotient_dimension':ambient-row['rank'],'target_survives_in_H1':not row['target_in_image'],'target_normal_form_support':row['residual_support'],'target_wall_valuations':row['residual_cubic_wall_valuations']})
checks={'source_results_pass':scalar['passed'] and four['passed'],'domain_dimension_matches_columns':all(r['C0_dimension']==x['columns'] for r,x in zip(rows,four['modular_tests'])),'ambient_dimension_1140':ambient==1140,'stable_rank_761':all(r['d0_rank']==761 for r in rows),'stable_H1_dimension_379':all(r['H1_quotient_dimension']==379 for r in rows),'target_survives':all(r['target_survives_in_H1'] for r in rows),'residual_not_simple':all(not x['residual_is_simple_pole_numerator'] for x in four['modular_tests'])}
assert all(checks.values()),checks
out={'schema':'marici.benincasa.G12-multistage-relative-primitive-complex-stage1.v1','prospective_action':'VC2_multistage_relative_primitive_complex','complex':'C0 --d0--> C1 --q--> H1=coker(d0)','C0':'four polynomial one-wall primitive coefficients of degree <=10','C1':'three-variable numerator polynomials of degree <=17','d0':'four-component twisted Hermite divergence','identity':'q o d0 = 0 by definition of cokernel','two_prime_fibers':rows,'stage1_result':'A stable 379-dimensional residual quotient is materialized at both primes, and the G12 odd target defines a nonzero class in it. The class is not yet logarithmic/simple.','VC2_status':'stage 1 constructed; action unresolved','required_stage2':'Construct a differential from controlled rational/overlap primitives into H1 whose image lowers the residual pole filtration, with q*d0=0 and exchange coherence.','planner_correction':'VC2 was priced as one action but contains at least quotient construction, stage-2 differential, coherence, and physical-boundary descent. Future replanning must split these subactions.','checks':checks,'passed':True}
d=ROOT/'research/benincasa/results/G12_multistage_primitive_complex_stage1.json';d.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'VC2':out['VC2_status'],'fibers':rows,'next':out['required_stage2']}))
