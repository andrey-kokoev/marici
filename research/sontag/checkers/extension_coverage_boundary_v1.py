"""Exact symbolic coverage/regime obstruction; no physical metric claim."""
import json
from pathlib import Path
import sympy as S
ROOT=Path(__file__).resolve().parents[3]
r,delta=S.symbols('r delta',real=True)
x=(1+r)/2
V=S.Matrix([[1,1],[x,x*x]])
d=S.Matrix([1,-1])
response=V*d
checks={
 'fixed_difference_response':response.applyfunc(S.simplify)==S.Matrix([0,(1-r*r)/4]),
 'nonzero_fixed_component_difference':d.dot(d)==2,
 'response_escapes_at_identity_probe':S.limit(response[1],r,1,dir='-')==0,
 'interior_determinant_formula':S.simplify(V.det()+(1-r*r)/4)==0,
 'regime_endpoint_bound':S.simplify((1-delta/2)*(delta/2)-delta/4)==delta*(1-delta)/4,
}
rows=[]
for n in (2,4,8,16,32,64):
    rn=1-S.Rational(1,n)
    z=S.simplify(response[1].subs(r,rn))
    rows.append({'n':n,'target_ratio':str(rn),'after_reading_difference':str(z),
                 'squared_inverse_ratio':str(2/z**2)})
checks['positive_interior_sequence']=all(S.sympify(row['after_reading_difference'])>0 for row in rows)
checks['inverse_ratio_grows']=all(S.sympify(a['squared_inverse_ratio'])<S.sympify(b['squared_inverse_ratio']) for a,b in zip(rows,rows[1:]))
a,b,Q,R=S.symbols('a b Q R',real=True)
checks['arbitrary_finite_word_induction_step']=S.expand(R**2*(Q**2*a)+R**4*(Q**4*b)-(R*Q)**2*a-(R*Q)**4*b)==0
out={'schema':'marici.sontag.extension-coverage-boundary.v1',
 'scope':'fixed mathematical vocabularies, finite-word induction and exact-reading Euclidean regime hostile',
 'checks':{k:bool(v) for k,v in checks.items()},'passed':all(checks.values()),'hostile_sequence':rows,
 'rejected_candidate':'uniform stable two-reading identification over all interior safe target ratios',
 'not_rejected':'exact discrete target reachability', 'shared_net_modified':False}
p=ROOT/'research/sontag/results/extension-coverage-boundary-v1.json'
p.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
raise SystemExit(0 if out['passed'] else 1)
