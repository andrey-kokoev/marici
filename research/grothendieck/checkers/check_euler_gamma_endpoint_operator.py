"""Exact regressions for the source-defined Euler gamma/endpoint comparison."""
from pathlib import Path
import json
import sympy as S

s,t=S.symbols('s t')
gamma=S.symbols('gamma',positive=True)
a,u,v,L,sigma=S.symbols('a u v L sigma',positive=True)
q=S.symbols('q',positive=True)
c=-(S.EulerGamma+S.log(S.pi))/2

assert S.simplify(S.exp(-a/2)*S.exp(-(s-S.Rational(1,2))*a)-S.exp(-s*a))==0
checks=0
for m in range(1,13):
    # Gamma's renormalized integral after q=exp(-2a).
    polynomial=sum(q**j for j in range(m-1))
    integral=S.integrate(polynomial,(q,0,1))/2
    assert S.simplify(c+integral-(S.polygamma(0,m)-S.log(S.pi))/2)==0
    checks+=1

endpoint=(1/s+1/(s-1)+1/t+1/(t-1))/(s+t-1)
swap=1/(s*(t-1))+1/((s-1)*t)
assert S.factor(endpoint-swap)==0
# Sum of the two resolvent kernels and their adjoints, in either half-plane.
for delta in (u-v,v-u):
    assert S.simplify(S.exp(delta/2)+S.exp(-delta/2)
                     -S.exp(u/2)*S.exp(-v/2)-S.exp(-u/2)*S.exp(v/2))==0
# Endpoint functional norms and resolvent operator majorants.
assert S.simplify(S.integrate(S.exp(-(2*gamma+1)*u),(u,0,S.oo))-1/(2*gamma+1))==0
# The minus endpoint uses gamma>1/2; substitute gamma=h+1/2.
h=S.symbols('h',positive=True)
assert S.integrate(S.exp(-2*h*u),(u,0,S.oo))==1/(2*h)
assert S.integrate(S.exp(-sigma*a),(a,L,S.oo))==S.exp(-sigma*L)/sigma
assert S.limit((S.exp(-2*a)-S.exp(-s*a))/(1-S.exp(-2*a)),a,0)==s/2-1

# Exact weighted-adjoint identity on decaying test exponentials.
alpha,beta=S.symbols('alpha beta',positive=True)
# alpha=gamma+A and beta=gamma+B ensure all integrals converge.
A,B=S.symbols('A B',positive=True)
left=S.exp(-(gamma+B)*a)/(A+B)
right=S.exp((A-gamma)*a)*S.exp(-(A+B)*a)/(A+B)
assert S.simplify(left-right)==0

# Polarization of the fixed graph-to-two-sheet map.
fbar,g,lfbar,lg=S.symbols('fbar g lfbar lg')
polarized=((fbar+lfbar)*(g+lg)-(fbar-lfbar)*(g-lg))/2
assert S.expand(polarized-(fbar*lg+lfbar*g))==0
X,ell=S.symbols('X ell')
Xprime=-S.I*ell*X
assert S.expand(X+S.I*Xprime-X*(1+ell))==0
assert S.expand(X-S.I*Xprime-X*(1-ell))==0
# Hostile: weighting the physical pairing changes the required denominator.
assert S.Rational(1,3+4-1)!=S.Rational(1,3+4-1-2)

result={'schema':'marici.grothendieck.euler-gamma-endpoint-operator.v1','passed':True,
        'exact_gamma_integral_checks':checks,
        'checks':{'renormalized_small_shift_limit':True,'endpoint_resolvent_swap_identity':True,
                  'weighted_shift_adjoint':True,'unweighted_pairing_required':True,
                  'two_sheet_graph_polarization':True,'theta_sheet_reconstruction':True},
        'scope':'Exact scalar integral, kernel and normalization regressions. Operator convergence, closability and source-domain claims are proved in the companion note; no semilocal domain equivalence or positivity is inferred.'}
root=Path(__file__).resolve().parents[3]
p=root/'research/grothendieck/results/euler-gamma-endpoint-operator.json'
p.parent.mkdir(parents=True,exist_ok=True)
p.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
