"""Passive covariance is weaker than a numerically invariant speed boundary."""
from pathlib import Path
import json
import hashlib
import sympy as S
ROOT=Path(__file__).resolve().parents[1]
x,t,w,v,u=S.symbols('x t w v u',real=True)
L=S.symbols('L',positive=True)
k=S.symbols('k',real=True)
# For t>=0 the finite medium-relative cone is (x-w*t)^2 <= L^2*t^2.
original=(x-w*t)**2-L**2*t**2
transformed=((x-v*t)-(w-v)*t)**2-L**2*t**2
assert S.expand(transformed-original)==0
assert S.expand((x-v*t)-u*t-(x-(v+u)*t))==0
for sign in (1,-1):
    assert S.expand((w+sign*L)-v-((w-v)+sign*L))==0
# The boundary is covariant but its coordinate velocity need not stay L.
assert S.simplify((L-v)-L)==-v
fixed_shift=S.factor((L+v)/(1+k*L*v)-L)
assert S.simplify(fixed_shift-v*(1-k*L**2)/(1+k*L*v))==0
assert S.simplify(fixed_shift.subs(k,1/L**2))==0
inputs=[Path(__file__),ROOT/'finite-horizon-frame-covariance-selection.md',ROOT/'future-probe-causal-speed-conjecture.md']
result={
 'schema':'marici.nima.time-linkage-covariance-audit.v1',
 'classification':'passive_probe_cone_covariance_does_not_by_itself_force_a_frame_independent_numeric_speed',
 'countermodel':'C_w: t>=0 and |x-w*t|<=L*t; xprime=x-v*t, wprime=w-v transports the same finite cone covariantly',
 'stronger_conditional':'Within (u+v)/(1+k*u*v), requiring the SAME boundary L as a fixed point yields k=1/L^2; k is not the Hamiltonian action-phase kappa',
 'scope':'Symbolic countermodel to equating passive naturality with fixed-boundary universality, not a counterexample to the correctly stated conditional fixed-point theorem or a physical source realization.',
 'input_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs}
}
(ROOT/'results/time-linkage-covariance-audit.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
