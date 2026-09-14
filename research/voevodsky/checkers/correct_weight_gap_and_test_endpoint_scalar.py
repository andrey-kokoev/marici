#!/usr/bin/env python3
"""Correct the stripped-weight comparison and test a constant endpoint scalar."""
import json
from fractions import Fraction as F
from pathlib import Path
R=Path(__file__).resolve().parents[3];B=R/'research/benincasa'
full=json.loads((B/'soft-endpoint-complete-source-weights.json').read_text())
old=json.loads((R/'research/voevodsky/results/endpoint_to_base_soft_label_falsifier.json').read_text())
def neg(r):return (r+1)/(2*r*(r-1)**2*(r+3))
def pos(s):return (s+1)/(4*s*(s-1)**2*(s+3))
# Rational points r^2+s^2=10 corresponding to kappa=+/-11/25.
pairs=[(F(9,5),F(13,5)),(F(13,5),F(9,5))]
rows=[]
for r,s in pairs:
 k=(s*s-r*r)/8;ratio=pos(s)/neg(r)
 rows.append({'kappa':str(k),'r':str(r),'s':str(s),'positive_over_negative':str(ratio)})
checks={'complete_source_packet_passes':full['status']=='pass','both_weights_minus_four':full['p_degrees']=={'negative_residue':-4,'positive_full_boundary':-4,'difference':0},'old_weight_gap_was_three':old['checks']['ports_need_weight_three_transition'],'rational_points_obey_collision_relation':all(r*r+s*s==10 for r,s in pairs),'samples_inside_open_kappa':all(abs((s*s-r*r)/8)<1 for r,s in pairs),'endpoint_ratio_not_constant':len({x['positive_over_negative'] for x in rows})==2}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.endpoint-weight-gap-erratum-and-scalar-test.v1','supersedes':'the weight-gap claim only in endpoint_to_base_soft_label_falsifier.json','correction':'After retaining the full marked rational source coefficient at xi=+1, both physical endpoint germs have p-degree -4. The alleged weight-three obstruction came from comparing the negative full residue to a coefficient-stripped positive CM period.','p_degrees':full['p_degrees'],'exact_same-family_samples':rows,'constant_scalar_comparison_exists':False,'reason':'Even after the grading correction, the ratio of the positive and negative physical germs varies with kappa. Thus no kappa-independent scalar identifies the endpoint lines. A genuine Gauss-Manin transport operator, not a weight shift or constant normalization, is required.','remaining_constructor':'Compute parallel transport of the moving a-cycle period I(t,kappa) from t=0 to t=2 in the marked relative connection and compare its endpoint germs.','checks':checks,'passed':True}
d=R/'research/voevodsky/results/endpoint_weight_gap_erratum_and_scalar_test.json';d.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'correct_weight_gap':0,'ratios':[x['positive_over_negative'] for x in rows],'constant_scalar':False}))
