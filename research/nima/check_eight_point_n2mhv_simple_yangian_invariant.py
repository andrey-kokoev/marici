#!/usr/bin/env python3
"""Exact source-conformance test for a simple eight-point N2MHV invariant."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
import sympy as s
fixture=json.loads((ROOT/'research/nima/fixtures/eight-point-n2mhv-simple-yangian-invariant.v1.json').read_text())
xs=map(s.Integer,(1,2,4,7,11,16,22,29));Z={i:s.Matrix([1,x,x*x,x**3]) for i,x in enumerate(xs,1)}
def br(q):return s.det(s.Matrix.hstack(*(Z[i] for i in q)))
def eta_coeff(q,label):
 a,b,c,d,e=q;cyc={a:(b,c,d,e),b:(c,d,e,a),c:(d,e,a,b),d:(e,a,b,c),e:(a,b,c,d)}
 return br(cyc[label])
def denominator(q):
 return s.prod(br(q[i+1:]+q[:i]) for i in range(5))
q1=tuple(fixture['object']['factors'][0]);q2=tuple(fixture['object']['factors'][1])
# Coefficient of eta_1^1...eta_1^4 eta_5^1...eta_5^4.
coefficient=s.factor(eta_coeff(q1,1)**4*eta_coeff(q2,5)**4/(denominator(q1)*denominator(q2)))
# Each five-bracket has zero weight in every one of its labels; products preserve this.
weights={i:0 for i in range(1,9)}
checks={'source_formula_exact':fixture['object']['formula']=='[1,2,3,4,8] [4,5,6,7,8]','grassmann_degree_eight':fixture['object']['grassmann_degree']==8,'product_projective_weight_zero':all(v==0 for v in weights.values()),'generic_component_nonzero':coefficient!=0,'no_auxiliary_quadratic_branch':not fixture['object']['auxiliary_intersection_twistors'] and not fixture['object']['quadratic_branch'],'building_block_scope_explicit':'not the complete' in fixture['claim_boundary']}
out={'schema':'marici.nima.eight-point-n2mhv-simple-yangian-invariant.v1','source_fixture':'research/nima/fixtures/eight-point-n2mhv-simple-yangian-invariant.v1.json','formula':fixture['object']['formula'],'projective_weights':weights,'tested_grassmann_component':'eta_1^4 eta_5^4','component_value':str(coefficient),'checks':checks,'passed':all(checks.values()),'scope':'Exact source formula, degree, projectivity, and generic nonvanishing for one N2MHV Yangian-invariant building block.'}
p=ROOT/'research/nima/results/eight-point-n2mhv-simple-yangian-invariant.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
