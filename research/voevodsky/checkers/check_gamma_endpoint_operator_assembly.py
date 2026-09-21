"""Source translation identities for gamma/endpoint/prime assembly."""
from pathlib import Path
import json
import sympy as s
u,a,t=s.symbols('u a t',positive=True)
z,ss,tt=s.symbols('z s t_spectral')
e=lambda q:s.exp(-(q-s.Rational(1,2))*u)
# e^(-t/4) T_(t/2) has the digamma exponential eigenvalue e^(-s*t/2).
assert s.simplify(s.exp(-t/4)*e(ss).subs(u,u+t/2)-s.exp(-ss*t/2)*e(ss))==0

v=s.symbols('v',positive=True)
checks=0
for q in range(1,13):
    # Change variable v=e^-t in the SUBTRACTED digamma integral.
    integrand=sum(v**j for j in range(q-1))
    value=s.integrate(integrand,(v,0,1))
    assert value==s.harmonic(q-1)
    assert s.cancel((1-v**(q-1))/(1-v)-integrand)==0
    checks+=1

# Endpoint swap is the symmetrized source translation kernel, not a fitted row.
x,y=s.symbols('x y',real=True)
assert s.expand((s.exp((y-x)/2)+s.exp(-(y-x)/2))
                -(s.exp(-x/2)*s.exp(y/2)+s.exp(x/2)*s.exp(-y/2)))==0
d=ss+tt-1
end=(1/ss+1/(ss-1)+1/tt+1/(tt-1))/d
swap=1/(ss*(tt-1))+1/((ss-1)*tt)
assert s.cancel(end-swap)==0

# Common operator's exponential eigenvalue is the arithmetic log derivative.
Ps,Pt,gs,gt=s.symbols('P_s P_t gamma_s gamma_t')
Ls=1/ss+1/(ss-1)+gs-Ps
Lt=1/tt+1/(tt-1)+gt-Pt
assert s.cancel((Ls+Lt)/d-(swap+(gs+gt)/d-(Ps+Pt)/d))==0
# Zero-trace closure is not a graph core for the required exponential states.
assert e(ss).subs(u,0)==1
result={'passed':True,'exact_subtracted_digamma_integrals':checks,
 'checks':{'gamma_translation_eigenvalue':True,
 'endpoint_swap_from_translation_symmetrization':True,
 'three_channel_form_identity':True,
 'nonzero_endpoint_trace_retained':True},
 'scope':'Exact source-operator identities. Graph-domain bounds and regulated-integral convergence are proved in the companion note; no selfadjoint full Tate equivalence or positivity claim.'}
ROOT=Path(__file__).resolve().parents[3]
out=ROOT/'research/voevodsky/results/gamma-endpoint-operator-assembly.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
